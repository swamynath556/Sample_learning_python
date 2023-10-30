from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from helper_functions.helper_file import helper


class sign_in:
    EMAIL = (By.XPATH, "//label[@for='ap_email']//following-sibling::input")
    PASSWORD = (By.XPATH, "//label[@for='ap_password']//ancestor::div[@class='a-section a-spacing-large']//input")
    ERROR_MSG = (By.XPATH, "//div[@class='a-section']//div[@class='a-box-inner a-alert-container']//h4")

    def __init__(self, browser):
        self.browser = browser.driver

    def fill_in_email(self, email):
        time.sleep(5)
        helper(self.browser).fill_the_value_and_click_enter(self.EMAIL,email)

    def fill_in_password(self, password):
        helper(self.browser).fill_the_value_and_click_enter(self.PASSWORD,password)
        time.sleep(10)

    def verify_error_if_email_or_password_is_wrong(self):
        assert "Incorrect phone number" == helper(self.browser).get_text(self.ERROR_MSG)
