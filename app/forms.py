from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from app.models import User
from flask_login import current_user
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя пользователя уже занято. Пожалуйста, выберите другое.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Такая почта уже занята. Пожалуйста, выберите другую.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Login')

    class UpdateAccountForm(FlaskForm):
        username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=20)])
        email = StringField('Email', validators=[DataRequired(), Email()])
        password = PasswordField('Новый пароль', validators=[Optional(), Length(min=6)])
        confirm_password = PasswordField('Подтверждение пароля', validators=[Optional(), EqualTo('password')])
        submit = SubmitField('Обновить')

        def validate_username(self, username):
            if username.data != current_user.username:
                user = User.query.filter_by(username=username.data).first()
                if user:
                    raise ValidationError('Имя уже занято.')

        def validate_email(self, email):
            if email.data != current_user.email:
                user = User.query.filter_by(email=email.data).first()
                if user:
                    raise ValidationError('Почта уже используется.')


class UpdateAccountForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Новый пароль', validators=[Optional(), Length(min=6)])
    confirm_password = PasswordField('Подтверждение пароля', validators=[Optional(), EqualTo('password')])
    submit = SubmitField('Обновить')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Имя уже занято.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Почта уже используется.')