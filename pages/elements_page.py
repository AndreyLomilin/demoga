from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements/'
        super().__init__(driver, self.base_url)

        self.text_element = WebElement(driver, 'div.pattern-backgound.playgound-header > div')

        self.icon = WebElement(driver, '#app > header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')

        self.text_field = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')









