import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_for_the_presence_buy_button(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button != [], 'Button not found'
