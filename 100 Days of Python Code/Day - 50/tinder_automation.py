from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import selenium

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://tinder.com/")
time.sleep(5)
login_button = driver.find_element(By.XPATH, '//*[@id="s686923397"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()
time.sleep(5)
# more_options = driver.find_element(By.XPATH, '//*[@id="s-1041457679"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
# more_options.click()
# time.sleep(5)
facebook_button = driver.find_element(By.XPATH, '//*[@id="s-1041457679"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
facebook_button.click()
time.sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
email = driver.find_element(By.CSS_SELECTOR, '#email')
email.send_keys("jmkl0987@gmail.com")
time.sleep(3)
password = driver.find_element(By.CSS_SELECTOR, '#pass')
password.send_keys("yourpassword")
time.sleep(3)
submit = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
submit.click()
time.sleep(6)
driver.switch_to.window(base_window)
print(driver.title)

cookies_button = driver.find_element(By.XPATH, '//*[@id="s-1041457679"]/main/div[2]/div/div/div[1]/div[1]/button')
cookies_button.click()
time.sleep(5)

location_allow = driver.find_element(By.XPATH, '//*[@id="s-1041457679"]/main/div/div/div/div[3]/button[1]')
location_allow.click()
time.sleep(5)

notification_button = driver.find_element(By.XPATH, '//*[@id="s-1041457679"]/main/div/div/div/div[3]/button[2]')
notification_button.click()
time.sleep(8)

for n in range(100):

    time.sleep(3)
    try:
        like_button = driver.find_element(By.CSS_SELECTOR, 'button[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-like):a"]')
        like_button.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        not_interested = driver.find_element(By.XPATH, '//*[@id="s-1041457679"]/main/div/div[2]/button[2]')
        not_interested.click()
        time.sleep(5)
    