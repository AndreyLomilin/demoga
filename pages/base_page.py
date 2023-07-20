from selenium.webdriver.common.by import By
import time
class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
# Переход на страницу
    def visit(self):
        return self.driver.get(self.base_url)

# Метод принимает аргумент locator и возвращает поиск элемента
#     def find_element(self,locator):
#         time.sleep(3)
#         return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url


    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False