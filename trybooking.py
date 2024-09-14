from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://events.humanitix.com/eus-presents-jurassic-ball-2023/tickets')

while True:

    input = driver.find_element(By.CSS_SELECTOR, "#select-tickets-646317a9382c3e70d3b44038")
    active = input.is_enabled()

    if active:
        input.send_keys(10)
        while True:
            try:
                button = driver.find_element(By.CSS_SELECTOR,
                    "#app > div:nth-child(2) > div > article > div.columns.two-cols > div > div > div:nth-child(2) > div.action-bar > button")
                button.click()
            except:
                pass

    if active:
        input.send_keys(10)

    else:
        driver.refresh()



            #driver.refresh()


#search_box = driver.find_element(By.CSS_SELECTOR, '#sticky-bottom-btn > div button')
time.sleep(500000)



