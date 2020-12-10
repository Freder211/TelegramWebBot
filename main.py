from selenium import webdriver
import configparser
import json

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Reading Configs (these parameters are saved in a different file for a security matter).
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values 
api_id = config['Telegram']['api_id'] # It reads the values from config.ini by the 'Telegram' class.
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']


# Create the client and connect
client = TelegramClient(username, api_id, api_hash) # It defines a new client with the username and the two unique codes.
client.start()
print("Client Created")
# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone) # If the user is not signed, a code request is sent to the phone.
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password = input('Password: ')) # If Telegram needs the password, it throws the exception.

""" browser = webdriver.Firefox() #crea il browser virtuale
browser.implicitly_wait(5) #aspetta ogni volta 5 secondi per il browser che carichi
browser.get('https://web.telegram.org/#/im') #va sul link assegnato

if browser.current_url=="https://web.telegram.org/#/login":
    tel = "3774345819"
    path_telefono = "//*[@id=\"ng-app\"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input"
    input_tel=browser.find_element_by_xpath(path_telefono)
    input_tel.click()
    input_tel.send_keys(tel)

    path_avanti = "/html/body/div[1]/div/div[2]/div[1]/div/a"
    avanti = browser.find_element_by_xpath(path_avanti)
    avanti.click()

    path_ok = "/html/body/div[4]/div[2]/div/div/div[2]/button[2]/span"
    ok = browser.find_element_by_xpath(path_ok)
    ok.click()

#xpath_prova = '//*[@id="main"]/div[3]/div/div/div[3]/div[last()]/div/div/div/div[1]' #xpath di prova
#msg = browser.find_element_by_xpath(last_msg_xpath).get_attribute('innerHTML') #esempio di gettarsi un messaggio da xpath

"""