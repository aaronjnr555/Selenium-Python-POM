from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import unittest
from SampleProjects.POMProjectDemo.Pages.LoginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.HomePage import HomePage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_Michael()
        homepage.logout_button_xpath()

        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # time.sleep(1)
        #
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # time.sleep(1)
        #
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # time.sleep(1)
        #
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
        # time.sleep(2)
        #
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()
        # time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Completed')

