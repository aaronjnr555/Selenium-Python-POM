from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.login_button_xpath =  "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"

    def open_site(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_xpath).click()




        