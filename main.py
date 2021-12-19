import os, time, string, random
from selenium import webdriver
import spammer, mail_handler

sasg = 'https://gov.eclipse-rp.net/posting.php?mode=post&f=644'
lspd = 'https://gov.eclipse-rp.net/posting.php?mode=post&f=23'
lsems = 'https://gov.eclipse-rp.net/posting.php?mode=post&f=575'
sadoc = 'https://gov.eclipse-rp.net/posting.php?mode=post&f=707'

browser = webdriver.Chrome('./chromedriver.exe')

def get_random_string():
    length = random.randint(5, 10)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def create_user():
    browser.get("https://gov.eclipse-rp.net/ucp.php?mode=register")
    username = str(get_random_string() + "" + get_random_string()) 
    password = "Roott00r"
    email = str(get_random_string() + "@gmail.com")
    question = "Alex Donnelly"
    browser.find_element_by_id("agreed").click()
    browser.implicitly_wait(2)
    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("new_password").send_keys(password)
    browser.find_element_by_id("password_confirm").send_keys(password)
    browser.find_element_by_id("email").send_keys(email)
    browser.find_element_by_id("pf_ecrp_forum_name").send_keys("Eclipse Roleplay")
    browser.find_element_by_id("answer").send_keys(question)
    browser.find_element_by_id("submit").click()
    browser.implicitly_wait(2)
    return username, password
username, password = create_user()

while True:
    try:
        browser.implicitly_wait(2)
        spammer.create_thread(sasg, browser)
        browser.implicitly_wait(2)
        spammer.create_thread(lspd, browser)
        browser.implicitly_wait(2)
        spammer.create_thread(lsems, browser)
        browser.implicitly_wait(2)
        spammer.create_thread(sadoc, browser)
    except Exception as e:
        print("I think he pussied out again... TIME TO DO AGAIN!")
        username, password = create_user()