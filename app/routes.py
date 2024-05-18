from flask import render_template, flash, redirect, url_for, request
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Request, Reply
from app.forms import LoginForm, RegistrationForm, CreateRequest, EditProfileForm, CreateReply
from urllib.parse import urlsplit
from datetime import datetime, timezone

@main.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()

@main.route('/') 
@main.route('/index') 
@login_required
def index():
    return render_template("index.html")

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route('/submit-request', methods=['GET', 'POST'])
@login_required
def submitRequest():
    form = CreateRequest()
    if form.validate_on_submit():
        if form.artist_user.data:
            artist = User.query.filter_by(username=form.artist_user.data).first()
            if artist == None:
                flash('This user does not exist.')
                return redirect(url_for('main.submitRequest'))
            else:
                request = Request(body=form.body.data, user_id=current_user.id, artist_id= artist.id)
        else:
            request = Request(body=form.body.data, user_id=current_user.id, artist_id= None)
        db.session.add(request)
        db.session.commit()
        flash('Request submitted successfully.')
        return redirect(url_for('main.submitRequest'))
    return render_template('createRequest.html', form=form)

@main.route('/public-requests', methods=['GET'])
def public_requests():
    public_requests = Request.query.filter(Request.artist_id.is_(None)).all()
    return render_template('generalBoard.html', public_requests=public_requests)

@main.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    requests = Request.query.all()
    replies = Reply.query.all()

    # Temporary data used for testing
    '''
    requests = [
        {'author': {'username': 'susan'}, 'body': 'Test post #1', 'artist': {'username': 'john'}},
        {'author': user, 'body': 'Test post #2'},
        {'author': {'username': 'john'}, 'body': 'Test post #3', 'artist': {'username': 'bubble'}}
    ]
    
    replies = [
        {'artist': user, 'body':'/img/cat.png', 'parent':1 },
        {'artist': {'username': 'bubble'}, 'body':'/img/tired.png', 'parent':2 }
    ]
    '''
    return render_template('user.html', user=user, requests=requests, replies=replies)

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
  form = EditProfileForm(current_user.username)
  if form.validate_on_submit():
    current_user.username = form.username.data
    current_user.bio = form.bio.data
    current_user.open = form.status.data == 'open'
    db.session.commit()
    flash('Your changes have been saved.')
    return redirect(url_for('main.edit_profile'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.bio.data = current_user.bio
  return render_template('edit_profile.html', title='Edit Profile', form=form)

@main.route('/requests/<request_id>')
@login_required
def requests(request_id):
    form = CreateReply()
    if form.validate_on_submit():
        reply = Reply(body=form.data.body, request_id=request_id, artist_id=current_user.id)
        db.session.add(reply)
        db.session.commit()
        flash('Your reply has been posted.')
        return redirect(url_for('main./requests/<request_id>'))
    requests = Request.query.filter_by(request_id=request_id).first_or_404()
    replies = Reply.query.filter_by(request_id=request_id)
    return render_template('requests.html', requests=requests, replies=replies,  form=form)


@main.route('/reply/<request_id>', methods=['POST', 'GET'])
@login_required
def send_reply(request_id):
    form = CreateReply()
    req = Request.query.filter_by(request_id=request_id).first_or_404()
    if form.validate_on_submit():
        body = form.body.data
        if body:
            reply = Reply(body=body, artist_id=current_user.id, request_id=req.request_id)
            db.session.add(reply)
            db.session.commit()
            flash('Your reply has been sent.')
            return redirect(url_for('main.requests', request_id=request_id))
        else:
            flash('Reply cannot be empty.')
            return redirect(url_for('main.requests', request_id=request_id))
    return render_template('requests.html', form=form, req=req)
