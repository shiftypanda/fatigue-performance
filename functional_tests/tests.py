from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewParticipantTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_login_confirm_a_shift_and_(self):

        # Kate has heard about the research study and decided she wants to take
        # part and goes to it's homepage

        self.browser.get(self.live_server_url)

        # She notices the page title and header mention fatigue and performance


        # She is invited to login to her participant account


        # She types in her username and password and succesffully logs in

        #






    def test_can_start_questions_then_start_cogtests(self):



    def test_can_start_and_complete_cogtests_then_is_thanked_for_her_time(self):

        
