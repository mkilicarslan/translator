from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, SubmitField
from wtforms.validators import InputRequired
from ...constants.languages import Languages


class TranslateForm(FlaskForm):
    text = TextAreaField("Text",  validators=[InputRequired(message="Text can't be blank")])
    lang_from = SelectField("From",  choices=Languages)
    lang_to = SelectField("To",  choices=Languages)
    # submit = SubmitField('Submit')
