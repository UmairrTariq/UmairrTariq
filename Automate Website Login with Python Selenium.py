from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/login')

driver.find_element(By.NAME, 'username').send_keys('tomsmith')

driver.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!'+ Keys.RETURN)

driver.implicitly_wait(5)

print("Logged in Successfully")
