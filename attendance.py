from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

# init selenium
browser = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
browser.get("xxxxx.com/login.aspx?")
actions = ActionChains(browser)

#logging in
username = browser.find_element_by_id("musername")
username.send_keys("xxxxx")
password = browser.find_element_by_id("mpassword")
password.send_keys("xxxx")
button = browser.find_element_by_id("login")
button.click()

# The signout button does not have id or anything like that so, manually pressing it
actions.send_keys(Keys.TAB)
actions.perform()
time.sleep(1)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(1)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(1)

# quitting browser and turning pc of
browser.quit()
time.sleep(2)
os.system('shutdown -s')