from flask import render_template, request, send_file
from flask_login import current_user
from . import bp
from .forms import TranslateForm
from app.helpers.aws import AWS_Translate, AWS_Polly, AWS_Transcribe
from app.constants.languages import Languages
from app.models import User, Translation
from app import db


@bp.route('/', methods=['GET', 'POST'])
def index():
    from_lang = 'en'
    to_lang = 'fr'

    form = TranslateForm()

    last_translations = current_user.get_latest_translations(10) if not current_user.is_anonymous else []

    # TODO: Error handling for incorrect input
    # Detect language
    if request.method == 'POST':
        text = form.text.data
        from_lang = form.lang_from.data
        to_lang = form.lang_to.data

        response = AWS_Translate.translate_text(
            Text=text,
            SourceLanguageCode=from_lang,
            TargetLanguageCode=to_lang
        )
        translated_text = response.get('TranslatedText')

        # Add translation to DB
        translation = Translation(
            lang_from=from_lang,
            lang_detected=from_lang,
            lang_to=to_lang,
            text_from=text,
            text_to=translated_text,
        )
        if not current_user.is_anonymous:
            translation.user_id = current_user.id
        db.session.add(translation)
        db.session.commit()
        return render_template(
            'home/index.html', title='Home', form=form, languages=Languages, from_lang=from_lang, to_lang=to_lang,
            text=text, translated_text=translated_text, last_translations=last_translations)

    form.lang_from.data = (from_lang)
    form.lang_to.data = (to_lang)
    return render_template(
        'home/index.html', title='Home', languages=Languages, form=form, from_lang=from_lang, to_lang=to_lang,
        last_translations=last_translations)


# @bp.route('/voice', methods=['GET', 'POST'])
# def text_to_speech():
#     response = AWS_Polly.synthesize_speech(VoiceId='Joanna',
#                                            OutputFormat='mp3',
#                                            Text='This is a sample text to be synthesized.')

#     with open('/tmp/speech.mp3', 'wb') as file:
#         file.write(response['AudioStream'].read())

#     job_name = "job name"
#     AWS_Transcribe.start_transcription_job(
#         TranscriptionJobName=job_name,
#         Media={'MediaFileUri': '/tmp/speech.mp3'},
#         MediaFormat='mp3',
#         LanguageCode='en-US'
#     )
#     while True:
#         status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
#         if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
#             break
#         print("Not ready yet...")
#         time.sleep(5)
#     print(status)
#     return send_file("/tmp/speech.mp3", as_attachment=True)
