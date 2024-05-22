from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# #Finding no of articles using XPath
# no_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # no_of_articles.click()
# print(no_of_articles.text)

# #Find element by link text
# featured_article = driver.find_element(By.LINK_TEXT, "Kurt Vonnegut")
# # featured_article.click()

# #Find the "Search" <input> by Name
# search_box = driver.find_element(By.NAME, "search")

# #Sending keyboard input to Selenium
# search_box.send_keys("Python", Keys.ENTER)

#Challenge 
driver.get(url="https://secure-retreat-92358.herokuapp.com")
#Fill the first name, last name and email
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

#Fill out the form
first_name.send_keys("Joseph")
last_name.send_keys("Martin")
email.send_keys("random@gmail.com")

#Enter the sign up button
signup_button = driver.find_element(By.TAG_NAME, "button")
signup_button.send_keys(Keys.ENTER)

# driver.close()