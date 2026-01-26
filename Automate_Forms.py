import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#set Up

print("Starting browser...")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    url = "https://www.selenium.dev/selenium/web/web-form.html"
    print(f'Navigating to this {url}')
    driver.get(url)
    
    #fill
    text_box = driver.find_element(By.NAME,'my-text')
    text_box.send_keys('Automated Python Input')
    print("Filled Text Input")
    
    password_box = driver.find_element(By.NAME,'my-password')
    password_box.send_keys('Secretpassword123')
    print("Filled Password")
    
    text_area = driver.find_element(By.NAME, 'my-textarea')
    text_area.send_keys("Welcome to my channel")
    print("Filled the text area")
    
    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button')
    submit_btn.click()
    print("Clicked Submit!!")
    
    #wait
    time.sleep(3)
    print("Form Submitted Successfully")
    
except Exception as e:
    print(f"An error occured {e}")
    
finally:
    driver.quit()
    print('Browser Closed!')