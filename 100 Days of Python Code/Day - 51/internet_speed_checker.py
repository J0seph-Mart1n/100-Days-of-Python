import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import selenium

guarantee_download_speed = 200
guarantee_upload_speed = 100
twitter_email = os.environ['TWITTER_EMAIL']
twitter_password = os.environ['TWITTER_PASSWORD']
twitter_username = os.environ['TWITTER_USERNAME']

class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        # Keep chrome browser open after program finishes
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net")
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(50)
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.get(url='https://twitter.com/home?lang=en')
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a').click()
        time.sleep(2)
        email_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(twitter_email)
        time.sleep(2)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(2)
        username_input = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]')
        username_input.send_keys(twitter_username)
        time.sleep(2)
        next_button2 = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="ocfEnterTextNextButton"]')
        next_button2.click()
        time.sleep(2)
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.send_keys(twitter_password)
        time.sleep(2)
        log_in = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')
        log_in.click()
        time.sleep(5)
        tweet_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div')
        tweet_box.send_keys(f'@airtelindia My internet speed is showing a download speed of {self.down} and an upload speed of {self.up}')
        time.sleep(2)
        if float(self.up) < guarantee_upload_speed or float(self.down) < guarantee_download_speed: 
            post_button = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]')
            post_button.click()

test = InternetSpeedTwitterBot()
test.get_internet_speed()
test.tweet_at_provider()
