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

    subject_element.send_keys('Dexter DeShawn NonRP Appeal') # << TITLE
    message_element.send_keys("I apologize for the inconvenience of me not giving a fuck") # << MESSAGE
    post_button.click()
    browser.implicitly_wait(2)
