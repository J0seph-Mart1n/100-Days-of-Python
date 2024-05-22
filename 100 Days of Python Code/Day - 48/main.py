from selenium import webdriver
from selenium.webdriver.common.by import By
# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get(url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(price.text)
driver.get(url="https://www.python.org")
search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# # Search by ID
# button = driver.find_element(By.ID, "submit")
# print(button.size)
# # Search by CSS Selector
# doc_attri = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_attri.text)
# # Search by XPATH
# icon = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[5]/p[2]/a[2]')
# print(icon.text)
# # Printing the dates of upcoming events
upcoming_event_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
upcoming_event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for n in range(len(upcoming_event_dates)):
    events[n] = {
        "Date": upcoming_event_dates[n].text,
        "Name": upcoming_event_names[n].text
    }
print(events)
driver.close() # Closes the main tab
# driver.quit() # Closes the entire browser
