from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")  
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-feature=AutomationControlled")

    driver = webdriver.Chrome(options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    outpout = text.split(": ")
    return float(outpout[1])

def main():
    driver = get_driver()
    driver.find_element(By.ID,"id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID,"id_password").send_keys("automatedautomated" + Keys.ENTER)
    time.sleep(2)
    element = driver.find_element(By.ID,"displaytimer")
    return clean_text(element.text)

print(main())
