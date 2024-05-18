from unittest import TestCase
from app import create_app, db
from app.config import TestConfig
from app.models import User

class BasicUnitTests(TestCase):
    
    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password(self):
        s = User(username="john")
        s.set_password("bubbles")
        db.session.add(s)
        db.session.commit()
        self.assertTrue(s.check_password("bubbles"))
        self.assertFalse(s.check_password("rumbles"))
