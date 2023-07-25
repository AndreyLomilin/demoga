import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('Andrej')
    form_page.last_name.send_keys('Lom')
    form_page.user_email.send_keys('test@test.ru')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('89213332211')

    form_page.hobbies.click_force()
    form_page.current_address.send_keys('Home')

    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()


def test_state_city(browser):
    form_page = FormPage(browser)
    form_page.visit()
    form_page.state_form.exist()
    form_page.state_form.click_force()
    form_page.select_state.send_keys(Keys.RETURN)
    form_page.city_form.exist()
    form_page.city_form.click_force()
    form_page.select_city.send_keys(Keys.RETURN)
    assert not form_page.state_form.get_text == ' '
    assert not form_page.city_form.get_text == ' '

