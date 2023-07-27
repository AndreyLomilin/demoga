import time

from pages.webtables import Webtables



def test_webtables(browser):
    page = Webtables(browser)
    page.visit()        # вход на страницу
    assert page.btn_add.exist()     # проверка наличия кнопки
    page.btn_add.click()     #  клик по кнопке

    assert page.modal_dialogs.exist()   #  проверка наличия модального окна

    page.btn_submit_modal_dialogs.click()
    assert page.modal_dialogs.exist()

    first_name = 'Andrej'
    last_name = 'Lom'
    user_email = 'Lom@kvfjjkf.rt'
    age = '29'
    salary = '0'
    deparmen = 'it'

    page.first_name_input.send_keys(first_name)
    page.last_name_input.send_keys(last_name)
    page.user_email_input.send_keys(user_email)
    page.age_input.send_keys(age)
    page.salary_input.send_keys(salary)
    page.department_input.send_keys(deparmen)
    time.sleep(2)
    page.btn_submit_modal_dialogs.click_force()
    assert not page.modal_dialogs.exist()

    # с таблицей не получается проверка, надо реализовать наверно цикл, массив...


    page.btn_edit.click()
    assert page.modal_dialogs.exist()














