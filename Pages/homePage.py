from opensourcecms.Locators.locators import Locators



class HomePage():
    def __init__(self, browser):
        self.browser = browser
        self.logout_linkText = Locators.logout_linkText

    def logout(self):
        self.browser.find_element_by_link_text(self.logout_linkText).click()