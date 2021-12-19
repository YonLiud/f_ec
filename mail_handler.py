from selenium import webdriver
import clipboard




# create a new instance of the chrome driver and call it mail_handler
mail_handler = webdriver.Chrome('./chromedriver.exe')
TenMinuteMail = "https://www.10minutemail.net/"

def get_mail():
    mail_handler.get(TenMinuteMail)
    mail_handler.implicitly_wait(10)
    mail_handler.find_element_by_id("copy-button").click()
    mail_handler.implicitly_wait(10)
    return clipboard.paste()