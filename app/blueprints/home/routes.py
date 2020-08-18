from flask import render_template, request, send_file
from . import bp
from .forms import TranslateForm
from ...helpers.aws import AWS_Translate, AWS_Polly
from ...constants.languages import Languages


@bp.route('/', methods=['GET', 'POST'])
def index():
    from_lang = 'en'
    to_lang = 'fr'

    form = TranslateForm()

    if request.method == 'POST':
        text = form.text.data
        from_lang = 'en'
        to_lang = 'fr'

        response = AWS_Translate.translate_text(
            Text=text,
            SourceLanguageCode=from_lang,
            TargetLanguageCode=to_lang
        )
        translated_text = response.get('TranslatedText')

        return render_template(
            'home/index.html', title='Home', form=form, languages=Languages, from_lang=from_lang, to_lang=to_lang,
            text=text, source_lang=source_lang, target_lang=target_lang, translated_text=translated_text)

    form.lang_from.data = (from_lang)
    form.lang_to.data = (to_lang)

    return render_template(
        'home/index.html', title='Home', languages=Languages, form=form, from_lang=from_lang, to_lang=to_lang)


# @bp.route('/voice', methods=['GET', 'POST'])
# def text_to_speech():
#     response = AWS_Polly.synthesize_speech(VoiceId='Joanna',
#                                            OutputFormat='mp3',
#                                            Text='This is a sample text to be synthesized.')

#     with open('/tmp/speech.mp3', 'wb') as file:
#         file.write(response['AudioStream'].read())

#     return send_file("/tmp/speech.mp3", as_attachment=True)
