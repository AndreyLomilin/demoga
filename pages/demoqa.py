
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from components.components import WebElement

class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_element = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer_text = WebElement(driver, '#app > footer > span')


    # def exist_icon(self):
    #     self.driver.find_element(By.CSS_SELECTOR, '#app > header > a')
    #     try:
    #         self.find_element()
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def click_on_the_icon(self):
    #     self.driver.find_element(By.CSS_SELECTOR, '#app > header > a').click()



    # def click_on_the_btn_elements(self):
    #     self.driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.home-body > div > div:nth-child(1)').click()






