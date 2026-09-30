from selenium.webdriver.common.by import By

class Login_Admin_Page:
    testbox_username_name = "username"
    testbox_password_name = "password"
    btn_login_cssSelector = "button[type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.testbox_username_name).clear()
        self.driver.find_element(By.NAME, self.testbox_username_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.testbox_password_name).clear()
        self.driver.find_element(By.NAME, self.testbox_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_login_cssSelector).click()