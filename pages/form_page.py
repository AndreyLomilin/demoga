import random

from pages.base_page import BasePage
from components.components import WebElement
from random import randint

class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')

        self.hobbies = WebElement(driver, f'label[for="hobbies-checkbox-{random.randint(1,3)}"]')
        self.current_address = WebElement(driver, '#currentAddress')

        self.state_form = WebElement(driver, '#state')
        self.city_form = WebElement(driver, '#city')
        self.select_state = WebElement(driver, '#react-select-3-input')
        self.select_city = WebElement(driver, '#react-select-4-input')

        self.form = WebElement(driver, '#userForm')

