from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://github.com")

signin_link = browser.find_element(By.CLASS_NAME, "position-relative mr-lg-3 d-lg-inline-block")
signin_link.click()

username_box = browser.find_element(By.ID, "login_field")
username_box.send_keys("username")
password_box = browser.find_element(By.ID, "password")
password_box.send_keys("password")
password_box.submit()

assert "username" in browser.page_source #This verifies that the username is in the html, to check if your logged in

browser.quit()