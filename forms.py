from flask_wtf import Form
from wtforms import TextAreaField, IntegerField, SubmitField, RadioField, SelectField

from wtforms import validators

class ContactForm(Form):
    name = TextAreaField("Name", [validators.InputRequired("Please enter your name.")])
    gender = RadioField("Gender", choices=[("M", "Male"), ("F", "Female")])
    address = TextAreaField("Address")

    email = TextAreaField("Email", [validators.InputRequired("Please enter your email"), validators.Email("Please enter your email")])

    age = IntegerField("Age")
    language = SelectField("Language", choices=[("cpp", "C++"), ("py", "Python"), ("java", "Java")])
    submit = SubmitField("Submit")