import time
from pages.base_page import BasePage
from components.components import WebElement

class Webtables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_dialogs = WebElement(driver, '#userForm')
        self.btn_submit_modal_dialogs = WebElement(driver, '#submit')
        self.first_name_input = WebElement(driver, '#firstName')
        self.last_name_input = WebElement(driver, '#lastName')
        self.user_email_input = WebElement(driver, '#userEmail')
        self.age_input = WebElement(driver, '#age')
        self.salary_input = WebElement(driver, '#salary')
        self.department_input = WebElement(driver, '#department')
        self.person_list = WebElement(driver, '.rt-tr-group')
        self. btn_edit = WebElement(driver, '#edit-record-1 > svg')



