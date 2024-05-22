from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")
cookie_clicker = driver.find_element(By.ID, "cookie")
cursor = driver.find_element(By.ID, "buyCursor")
grandma = driver.find_element(By.ID, "buyGrandma")

timeout = time.time() + 5   # [seconds]
five_minutes = time.time() + 60*5

while True:
    cookie_clicker.click()

    if time.time() > timeout:
        driver.find_element(By.ID, "buyGrandma").click()
        timeout = time.time() + 5

    if time.time() > five_minutes:
        break


cookies = driver.find_element(By.ID, "money")
print(cookies.text)

