import asyncio
from xtempmail import Email, extension
import logging
from xtempmail import mail
from xtempmail.mail import EmailMessage
import requests
import selenium.webdriver
requests.get('https://google.com',params={'a':1})
log = logging.getLogger('xtempmail')
log.setLevel(logging.INFO)
# browser = webdriver.Chrome('./chromedriver.exe')
def main(mail_addr):
    mail_app = Email(name=mail_addr, ext=extension[1])
    @mail_app.on.message()
    def get(data):
        # parse the data
        print(data.text)
        
    mail_app.listen_new_message(interval=2)
    
