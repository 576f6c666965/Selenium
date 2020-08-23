from opensourcecms.Locators.locators import Locators


class LoginPage():

    def __init__(self, browser):
        self.browser = browser

        self.username_text_box = Locators.username_text_box
        self.password_text_box = Locators.password_text_box
        self.login_button = Locators.login_button
    def enter_username(self, username):
        self.browser.find_element_by_id(self.username_text_box).clear()
        self.browser.find_element_by_id(self.username_text_box).send_keys(username)
    def enter_passwrod(self, password):
        self.browser.find_element_by_id(self.password_text_box).clear()
        self.browser.find_element_by_id(self.password_text_box).send_keys(password)
    def click_login_button(self):
        self.browser.find_element_by_id(self.login_button).click()
        