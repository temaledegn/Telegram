from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import InputPeerEmpty
from telethon import TelegramClient
import asyncio
loop = asyncio.get_event_loop()
import telethon.sync
from telethon import TelegramClient
from telethon.sync import TelegramClient

loop = asyncio.get_event_loop()


api_id =917309
api_hash = '40aa9c3a4ef3f8f52bda1b7c0280d5bb'
phone_number = '+251924221803'
channel_username = 'aricchen_group'


client = TelegramClient('session1', api_id, api_hash)
client.start()
participants = client.get_participants(channel_username)
usernames=[]
firstnames=[]
lastnames =[]
if len(participants):
    for x in participants:

        if x.username:
            username=x.username
            print(username)
        else:
            username=" "
        if x.first_name:
            firstname=x.first_name
            print(firstname)
        else:
            firstname=" "
        if x.last_name:
            lastname=x.last_name
        else:
         lastname=""