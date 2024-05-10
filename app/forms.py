from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class CreateRequest(FlaskForm):
	body = StringField('Body', validators=[DataRequired()])
	artist_user = StringField('Artist')
  	submit = SubmitField('Submit request')
	
	# Validates username of artist if provided
	def validate_artistUser(self, artist): 
		if artist.data:
			artUser = User.query.filter_by(artist_user=artist.data).first() 
			if not artUser: 
				raise ValidationError("Please type in an existing username.")
       		if not artUser.open:
            		raise ValidationError("This artist is not accepting requests.”)
