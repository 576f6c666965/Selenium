from selenium import webdriver
import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from opensourcecms.Pages.loginPage import LoginPage
from opensourcecms.Pages.homePage import HomePage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox(executable_path='geckodriver.exe')
    def test_login_valid(self):
        browser = self.browser 
        login = LoginPage(browser)
        home = HomePage(browser)

        
        browser.get("https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/auth/login")
        login.enter_username("opensourcecms")
        login.enter_password("opensourcecms")
        login.click_login_button()

        time.sleep(2)

        home.logout

        time.sleep(1)
    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print("finito")

if __name__ == "__main__":
    unittest.main()
