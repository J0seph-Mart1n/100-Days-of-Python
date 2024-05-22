from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3872988635&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
time.sleep(5)
sign_up_button = driver.find_element(By.XPATH, '/html/body/div[2]/a[1]')
sign_up_button.click()
time.sleep(5)
email = driver.find_element(By.NAME, "session_key")
password = driver.find_element(By.NAME, "session_password")
email.send_keys("jmkl0987@gmail.com")
password.send_keys("yourpassword")

sign_up = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_up.send_keys(Keys.ENTER)
time.sleep(5)

# jobs = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
# jobs.click()
# time.sleep(5)

easy_apply = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
easy_apply.click()
time.sleep(5)

phone_no = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3872988635-117831882-phoneNumber-nationalNumber"]')
phone_no.send_keys("yournumber")
time.sleep(5)

next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
next_button.click()
time.sleep(5)

next_button2 = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
next_button2.click()
time.sleep(5)

select = driver.find_element(By.XPATH, '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3872988635-117831866-multipleChoice"]/option[4]')
select.click()
time.sleep(5)

experience = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3872988635-117831946-numeric"]')
experience.send_keys('2')
time.sleep(5)

review_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Review your application']")
review_button.click()
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
submit_button.click()
time.sleep(5)



