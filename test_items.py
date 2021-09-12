import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_for_the_presence_buy_button(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket")
    time.sleep(30)
    

