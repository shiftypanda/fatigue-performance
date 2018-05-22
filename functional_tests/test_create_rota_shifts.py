from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest
from .create_rota_page import CreateRotaPage

RESEARCHER = 'kate'
RESEARCHERPASS = 'secretcode'

class CreateRotaTest(FunctionalTest):

    def test_can_create_a_shift_for_one_user(self):

        # Kate is a researcher and she is trying to enter a shift for a participant
        # She is invited to log into the site
        self.browser.get(self.live_server_url)

        create_rota_page = CreateRotaPage()
        create_rota_page.get_username_box.send_keys(RESEARCHER)
        create_rota_page.get_username_box.send_keys(ENTER)
        create_rota_page.get_password_box.send_keys(RESEARCHERPASS)
        create_rota_page.get_password_box.send_keys(ENTER)
        # Once succesfuly logged in Kate is presented with current active particpants

        # She selects one participant x and looks to enter new shift for today
        create_rota_page.get_participant(participant='participant x')
        # The browser refreshes and the new rota shift time is displayed

        # She is asked to confirm dates that this rota will be taking place


    def test_can_confirm_a_rota_shift(self):

        # Participant x(Dave) logins in to site

        # Dave is shown his expected shift for today

        # Dave is asked to confirm if this is correct

        # He confirms yes this shift is correct

        # Browser reloads thanking him for confimring shift is correct

        self.fail('Write me')
