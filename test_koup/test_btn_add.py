
from pages.the_internet_herokuapp import Koup
from pages.the_internet_herokuapp_add_remove_elements import KoupAdd
def test_btn_add(browser):
    koup_page = Koup(browser)
    koupadd_page = KoupAdd(browser)
    koup_page.visit()

    # assert koup_page.link_add_remove.get_text() == 'Add/Remove Elements'
    koup_page.link_add_remove.click()
    assert koupadd_page.btn_add.get_text() == 'Add Element'
    assert koupadd_page.btn_add.get_dom_attribute('onclick') == 'Add Element()'
    for i in range(4):
        koupadd_page.btn_add.click()
    assert koupadd_page.btns_del.check_count_elements(count=4)






