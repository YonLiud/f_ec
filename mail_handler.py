import asyncio
from xtempmail import Email, extension
import logging
from xtempmail import mail
from xtempmail.mail import EmailMessage
import requests
import selenium.webdriver as wb
requests.get('https://google.com',params={'a':1})
log = logging.getLogger('xtempmail')
log.setLevel(logging.INFO)

def main(mail_addr):
    mail_app = Email(name=mail_addr, ext=extension[1])
    @mail_app.on.message()
    def get(data):
        message = str(data.text)
        # get a part of the message that contains a link "https://gov.eclipse-rp.net/ucp.php?"
        url = message[message.find('https://gov.eclipse-rp.net/ucp.php?'):]
        url = url[:url.find('\n')]
        browser = wb.Chrome('./chromedriver.exe')
        browser.get(url)
        
        # wait for 30 seconds  for the page to load
        browser.implicitly_wait(30)
        exit()
        
    mail_app.listen_new_message(interval=2)
    
