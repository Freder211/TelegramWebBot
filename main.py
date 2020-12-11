import configparser
import json
import asyncio

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
    PeerChannel
)

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

async def main(phone):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    me = await client.get_me()

    user_input_channel = input("Enter channel URL or ID: ")

    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel

    CIAORAGA_by_Michele_Molteni = await client.get_entity(entity)

    offset = 0
    limit = 100
    all_participants = []

    while True:
        participants = await client(GetParticipantsRequest(
            CIAORAGA_by_Michele_Molteni, ChannelParticipantsSearch(''), offset, limit,
            hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)

    all_user_details = []
    for participant in all_participants:
        all_user_details.append(
            {"id": participant.id, "first_name": participant.first_name, "last_name": participant.last_name,
             "user": participant.username, "phone": participant.phone, "is_bot": participant.bot})

    with open('data.json', 'w') as outfile:
        json.dump(all_user_details, outfile)

with client:
    client.loop.run_until_complete(main(phone))
    
    



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