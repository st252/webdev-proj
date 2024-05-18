from flask_wtf import FlaskForm
from wtforms import HiddenField, RadioField, StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length
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

# Validates username of artist if provided in CreateRequest
def validate_artistUser(self, artist): 
    if artist.data:
        artUser = User.query.filter_by(username=self.artist_user.data).first() 
        if not artUser: 
            raise ValidationError("Please type in an existing username.")
        if artUser.open == False:
            raise ValidationError("This artist is not accepting requests.")

class CreateRequest(FlaskForm):
    body = StringField('Body', validators=[DataRequired()])
    artist_user = StringField('Artist', validators=[validate_artistUser])
    submit = SubmitField('Submit request')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[Length(min=0, max=256)])
    status = RadioField('Request Status', choices=[('open', 'Open'), ('closed', 'Closed')])
    submit = SubmitField('Submit')


    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class CreateReply(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Send reply')

class CompleteRequest(FlaskForm):
    request_id = HiddenField('Request ID')
    submit = SubmitField('Mark as Complete')