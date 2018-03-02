from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

class CreateRotaTest(FunctionalTest):

    def test_can_create_a_rota_shift(self):

        # Kate has heard about the research study and decided she wants to take
        # part and goes to it's homepage

        self.browser.get(self.live_server_url)

        # She notices the page title and header mention fatigue and performance

        # She is invited to enter a new rota shift

        # The browser refreshes and the new rota shift time is displayed

        # She is asked to confirm dates that this rota will be taking place


    def test_can_confirm_a_rota_shift(self):
