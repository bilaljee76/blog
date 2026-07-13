from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField(
        "Full Name",
        validators=[DataRequired(), Length(min=3, max=50)]
    )

    email = StringField(
        "Email Address",
        validators=[DataRequired(), Email()]
    )

    phone = StringField(
        "Phone",
        validators=[DataRequired(), Length(min=11, max=15)]
    )

    message = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(min=10)]
    )

    submit = SubmitField("Send Message")