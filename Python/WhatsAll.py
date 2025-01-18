from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

options= webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Josef Rivera/.config/google-chrome/default")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
time.sleep(10)

contact_name= 'Josef'
contact_message= 'Hola Como estas'

search_bar= driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
search_bar.send_keys(contact_name)
time.sleep(2)

contact_element= driver.find_element(By.XPATH, f'//span[contains(@title, \'{contact_name}\')]')
time.sleep(2)

contact_element.click()
time.sleep(2)

message_box= driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
message_box.send_keys(f'{contact_message}')
time.sleep(2)

message_box.send_keys(f'{Keys.ENTER}')
time.sleep(2)
