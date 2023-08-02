from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

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
    driver.get("http://automated.pythonanywhere.com/")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    outpout = text.split(": ")
    return float(outpout[1])

def write_file(text):
    """Write input text into a text file"""
    name = dt.now().strftime('%Y-%m-%d.%H-%M-%S')
    filename = f"{name}.txt"
    with open(filename, 'w') as file:
        file.write(text)

def main():
    driver = get_driver()
    while True:
        time.sleep(2)
        element = driver.find_element(By.XPATH,"/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        write_file(text)

print(main())
