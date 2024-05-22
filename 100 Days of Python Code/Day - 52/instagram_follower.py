import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import selenium

email_id = os.environ['INSTAGRAM_EMAIL']
password = os.environ['INSTAGRAM_PASSWORD']


class InstaFollower:

    def __init__(self):
        # Keep chrome browser open after program finishes
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        time.sleep(5)
        user_id = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_id.send_keys(email_id)
        user_password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        user_password.send_keys(password)
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        submit_button.click()
        time.sleep(5)
        login_info_save = self.driver.find_element(By.CSS_SELECTOR, 'div[role="button"]')
        login_info_save.click()
        time.sleep(5)
        notification = self.driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
        notification.click()
        

    def find_followers(self):
        self.driver.get(url='https://www.instagram.com/cbum/followers/')
        time.sleep(5)
        scroll_down = self.driver.find_element(By.CSS_SELECTOR, 'div[class="_aano"]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_down)
            time.sleep(2)


    def follow(self):
        follow_button = self.driver.find_elements(By.CSS_SELECTOR, '._aano button')
        for button in follow_button:
            try:
                button.click()
                time.sleep(3)
            except selenium.common.exceptions.ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
                time.sleep(2)

insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
    
