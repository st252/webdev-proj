from app import db
from app.models import *

john = User(username='john')
susan = User(username='susan', open=True)
base = User(username='base')
bubble = User(username='bubble')
john.set_password('johnpass')
bubble.set_password('tea')
susan.set_password('susanpass')
base.set_password('ball')

request1 = Request(body='An ocean scenery.', user_id=1, artist_id=2)
request2 = Request(body='A big apple tree.', user_id=2)


db.session.add_all([john, susan, base, bubble, request1, request2])


request3 = Request(body='Test post with id 3: I want a drawing of a cat!', user_id=4, artist_id=1)
request4 = Request(body='Test post #4 from user "bubble". I want a drawing of Kirby', user_id=4)
request5 = Request(body='Test post #5 from user "john" to "bubble". A tired person ', user_id=1, artist_id=4)
request6 = Request(body='Test post #6 from user "susan" to "john": A penguin, feel free to draw however you like.', user_id=2, artist_id=1)
reply1 = Reply(body='/img/cat.png', request_id=3, artist_id=1)
reply2 = Reply(body='/img/tired.png', request_id=5, artist_id=4)

db.session.add_all([request3, request4, request5, reply1, reply2])

request7 = Request(body='A cow frolicking in the fields.', user_id=4)
request8 = Request(body='Please draw me a cool car!', user_id=1)
replyCar1 = Reply(body='/img/susan-car.png', request_id=8, artist_id=2)
replyCar2 = Reply(body='/img/cool-car.png', request_id=8, artist_id=4)
replyTree1 = Reply(body='/img/john-tree.png', request_id=2, artist_id=1)

db.session.add_all([request7, request8, replyCar1, replyCar2, replyTree1])
db.session.commit()
