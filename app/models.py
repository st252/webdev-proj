from datetime import datetime, timezone
from sqlalchemy import DateTime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    # Whether a user is open (true) to requests or closed (false)
    open = db.Column(db.Boolean, nullable=False, default=False)

    # Requests they make that for others to illustrate
    # requests = db.relationship('Request', foreign_keys=[id], back_populates='author')
    # Requests others make for them to illustrate
    # jobs = db.relationship('Request', back_populates='artist')
    replies = db.relationship('Reply', back_populates='artist')

    def __repr__(self):
        return f'<User {self.username} {self.id} : Open {self.open}>'
    

class Request(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(2048), nullable=False)
    timestamp = db.Column(DateTime, index=True, default=lambda: datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # User can specify a specific artist to request, else it is shown to everyone
    artist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    # Whether the request has been completed
    complete = db.Column(db.Boolean, nullable=False, default=False)

    author = db.relationship(User, foreign_keys=[user_id])
    artist = db.relationship(User, foreign_keys=[artist_id])

    replies = db.relationship('Reply', back_populates='parent')

    def __repr__(self):
        return f'<Request from {self.user_id} to {self.artist_id}, #{self.request_id} Text: {self.body}>'

class Reply(db.Model):
    reply_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(2048), nullable=False)
    timestamp = db.Column(DateTime, index=True, default=lambda: datetime.now(timezone.utc))
    artist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    request_id = db.Column(db.Integer, db.ForeignKey('request.request_id'), nullable=False)

    # The parent is the id of the request they are replying to 
    parent = db.relationship(Request, foreign_keys=[request_id])
    artist = db.relationship(User, foreign_keys=[artist_id])

    def __repr__(self):
        return f'<Reply from {self.artist_id} to request #{self.request_id}, #{self.reply_id} Link: {self.body}>'