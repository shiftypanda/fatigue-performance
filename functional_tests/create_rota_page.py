from selenium.webdriver.common.keys import Keys
from .base import wait



class CreateRotaPage(object):

    def __init__(self, test):
        self.test = test

    def get_username_box(self):
        self.test.browser.get_element_by_id('username')

    def get_password_box(self):
        self.test.browser.get_element_by_id('password')

    def get_participant(self, participant):
        self.test.browser.get_element_by_id('participant')
        self.test.browser.send_keys(participant)
        self.test.browser.send_keys(Keys.ENTER)
