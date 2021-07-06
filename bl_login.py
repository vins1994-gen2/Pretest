from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()

    driver.get("https://bukalapak.com/login")
    el1 = driver.find_element(By.ID, "user_session_username")
    el1.send_keys("jeremitotti666@gmail.com")
    el2 = driver.find_element(By.ID, "user_session_password")
    el2.send_keys("enamenam6")
    el3 = driver.find_element(By.CLASS_NAME, "js-btn-menu-login")
    el3.click()
finally:
      print("done")