from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.Michael_xpath = "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
        self.logout_button_xpath = "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"

    def click_Michael(self):
        self.driver.find_element_by_xpath(self.Michael_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

