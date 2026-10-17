from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange


class BookForm(FlaskForm):
    title = StringField('Tytuł książki', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    year = IntegerField('Rok wydania', validators=[
        DataRequired(),
        NumberRange(min=0, max=2026)
    ])
    is_read = BooleanField('Oznacz jako przeczytaną')