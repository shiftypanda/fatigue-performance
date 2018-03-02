from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class CreateRotaTest(LiveServerTestCase):

    def test_can_login_confirm_a_shift_and_(self):

        # Kate has heard about the research study and decided she wants to take
        # part and goes to it's homepage

        self.browser.get(self.live_server_url)

        # She notices the page title and header mention create a new rota


        # She is invited to login to enter the new rota


        # She types in her username and password and succesffully logs in

        #
