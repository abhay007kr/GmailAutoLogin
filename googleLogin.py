from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = '/home/abhay/selenium/chromedriver'

driver=webdriver.Chrome(PATH)

driver.get("https://www.gmail.com")
google_user = driver.find_element_by_name("identifier")
google_user.send_keys("<Your username>")
nex = driver.find_element_by_id("identifierNext")
nex.click()

driver.implicitly_wait(3)
driver.find_element_by_name("password").send_keys("<Your password>")
driver.find_element_by_id("passwordNext").click()
