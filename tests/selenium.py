import multiprocessing
import time
from app.config import TestConfig
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

from app import create_app, db
from app.models import User


localHost = "http://localhost:5000/"


class SeleniumTestCase(TestCase):

    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()
        multiprocessing.set_start_method("fork")
        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()

        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(localHost)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        self.server_process.terminate()
        self.driver.close()
    
    
    def test_login_fail(self):
        u = User(username="john")
        u.set_password("johnpass")
        db.session.add(u)
        db.session.commit()
        username = "jon"
        loginElement = self.driver.find_element(By.ID, "username")

        loginElement.send_keys(username)

        loginElement = self.driver.find_element(By.ID, "password")
        loginElement.send_keys("johnpass")

        submitElement = self.driver.find_element(By.ID, "submit")
        submitElement.click()

        
        messages = self.driver.find_elements(By.CLASS_NAME, "message")
        self.assertEqual(len(messages), 1, "Expected there to be a single error message when trying to login as a non-existent user")
        self.assertEqual(messages[0].text, f"Invalid username or password")
        
    '''
    def test_requests_open(self):
            u = User(username="john")
            u.set_password("johnpass")
            db.session.add(u)
            db.session.commit()
            username = "john"

            loginElement = self.driver.find_element(By.ID, "username")
            loginElement.send_keys(username)

            loginElement = self.driver.find_element(By.ID, "password")
            loginElement.send_keys("johnpass")

            submitElement = self.driver.find_element(By.ID, "submit")
            submitElement.click()

            wait = WebDriverWait(self.driver, 5)
            profileElement = wait.until(EC.element_to_be_clickable((By.ID, "profile")))
            profileElement.click()
            
            editProfileElement = wait.until(EC.element_to_be_clickable((By.ID, "edit-profile")))
            editProfileElement.click()
            time.sleep(2)
            open = wait.until(EC.element_to_be_clickable((By.ID, "status-0")))
            open.click()

            submitElement = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
            submitElement.click()
            time.sleep(2)
            self.assertTrue(u.open)

            messages = self.driver.find_elements(By.CLASS_NAME, "message")
            self.assertEqual(len(messages), 1, "Expected there to be a single message when trying to edit profile details")
            self.assertEqual(messages[0].text, f"Your changes have been saved.")
    

    def test_send_requests(self):
            u = User(username="john")
            u2 = User(username="susan")
            u.set_password("johnpass")
            db.session.add_all([u, u2])
            db.session.commit()
            username = "john"

            loginElement = self.driver.find_element(By.ID, "username")
            loginElement.send_keys(username)

            loginElement = self.driver.find_element(By.ID, "password")
            loginElement.send_keys("johnpass")

            submitElement = self.driver.find_element(By.ID, "submit")
            submitElement.click()

            wait = WebDriverWait(self.driver, 5)
            createElement = wait.until(EC.element_to_be_clickable((By.ID, "create-request")))
            createElement.click()
            
            body = wait.until(EC.element_to_be_clickable((By.ID, "body")))
            body.send_keys("I want a baseball drawing")
           
            open = wait.until(EC.element_to_be_clickable((By.ID, "artist_user")))
            open.send_keys("susan")

            submitElement = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
            submitElement.click()
            time.sleep(2)

            messages = self.driver.find_elements(By.CLASS_NAME, "error-msg")
            self.assertEqual(len(messages), 1, "Expected there to be a single message when trying request closed user")
            self.assertEqual(messages[0].text, f"[This artist is not accepting requests.]")
    '''