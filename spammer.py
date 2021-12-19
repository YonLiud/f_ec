import os, time
from selenium import webdriver

def login(username, password, browser):
    browser.get('https://gov.eclipse-rp.net/ucp.php?mode=login&amp;redirect=index.php')
    login_element = browser.find_element_by_id('username')
    password_element = browser.find_element_by_id('password')
    submit_element = browser.find_element_by_name('login')

    login_element.send_keys(username)        #  << USERNAME_HERE
    password_element.send_keys(password)          #  << PASSWORD
    submit_element.click()

    browser.implicitly_wait(2)

def create_thread(url, browser):
    browser.get(url)
    subject_element = browser.find_element_by_id('subject')
    message_element = browser.find_element_by_id('message')
    post_button = browser.find_element_by_name('post')

    subject_element.send_keys('Hello, Friend') # << TITLE
    message_element.send_keys("""谢谢! Thank you very much! for being my mentor ECRP Staff! Please! Admit defeat, or this wave won't be the last one you see!
谢谢 again! Until next account! """) # << MESSAGE
    post_button.click()
    browser.implicitly_wait(2)
