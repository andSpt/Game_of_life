from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange, InputRequired, DataRequired


class Dimensions_world_Form(FlaskForm):
    width = IntegerField('Введите ширину мира', validators=[NumberRange(min=5, max=100, message="Ширина мира должна быть в диапазон от 5 до 100" ),
                                                            InputRequired('Вы не ввели ширину мира'),
                                                            DataRequired("Введите целое положительное число")])
    height = IntegerField('Введите высоту мира', validators=[NumberRange(min=5, max=100, message="Высота мира должна быть в диапазон от 5 до 100"),
                                                             InputRequired('Вы не ввели высоту мира'),
                                                             DataRequired("Введите целое положительное число")])
    submit = SubmitField('Submit')