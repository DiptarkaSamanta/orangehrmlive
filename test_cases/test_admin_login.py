import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import read_Config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:
    admin_page_url = read_Config.get_admin_page_url()
    username = read_Config.get_username()
    password = read_Config.get_password()
    invalid_username = read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_title_verification(self, setup):
        self.logger.info("********************Test_01_Admin_Login********************")
        self.logger.info("********************verification of admin login page title********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        expected_title = "OrangeHRM"
        if actual_title == expected_title:
            self.logger.info("********************title match********************")
            assert True
        else:
            os.makedirs(".\\screenshots", exist_ok=True)
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("********************title not match********************")
            assert False

    def test_valid_admin_login(self, setup):
        self.logger.info("********************test of valid admin login********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_login_page = Login_Admin_Page(self.driver)
        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password)
        self.admin_login_page.click_login()

        # WebDriverWait visibility check (commented out):
        # dashboard_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
        # assert dashboard_element.text == "Dashboard"

        actual_dashboard_text = self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
        if actual_dashboard_text == "Dashboard":
            self.logger.info("********************dashbord text found********************")
            assert True
        else:
            os.makedirs(".\\screenshots", exist_ok=True)
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.logger.info("********************dashbord text not found********************")
            assert False

    def test_invalid_admin_login(self, setup):
        self.logger.info("********************test of invalid admin login********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_login_page = Login_Admin_Page(self.driver)
        self.admin_login_page.enter_username(self.invalid_username)
        self.admin_login_page.enter_password(self.password)
        self.admin_login_page.click_login()

        # WebDriverWait visibility check (commented out):
        # error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")))
        # assert error_message.text == "Invalid credentials"

        error_message = self.driver.find_element(By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]").text
        if error_message == "Invalid credentials":
            self.logger.info("********************invalid credentials text found********************")
            assert True
        else:
            os.makedirs(".\\screenshots", exist_ok=True)
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.logger.info("********************invalid credentials text not found********************")
            assert False