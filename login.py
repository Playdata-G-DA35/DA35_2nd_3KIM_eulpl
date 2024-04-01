import time
from selenium import webdriver
from selenium.webdriver.common.by import By

login_url = 'https://www.instagram.com/accounts/login'

def insta_login():
    insta_driver = webdriver.Chrome()
    print('open chrome done')

    ### login
    insta_id = 'ihman0513@gmail.com'
    insta_pw = 'ino0513'

    insta_driver.get(login_url)
    time.sleep(1)

    # send id
    input_id = insta_driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    print('select id done')
    input_id.clear()
    input_id.send_keys(insta_id)
    print('send id done')

    # send pw
    input_pw = insta_driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    print('select pw done')
    input_pw.clear()
    input_pw.send_keys(insta_pw)
    print('send pw done')

    input_pw.submit()
    print('submit done')
    time.sleep(3)

    return insta_driver