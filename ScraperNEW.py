from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import InputPeerEmpty
from telethon import TelegramClient
import os,sys
from pymongo import MongoClient
import asyncio
loop = asyncio.get_event_loop()
import telethon.sync
from telethon import TelegramClient
from telethon.sync import TelegramClient
import configparser
import json
offset = 0
limit = 200
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
db = client['telegram-data']
#collection=db['telegram-data']
import datetime
loop = asyncio.get_event_loop()
cpass = configparser.RawConfigParser()
cpass.read('config.data')
api_id = cpass['cred']['id']
api_hash = cpass['cred']['hash']
phone = cpass['cred']['phone']
file="data.json"
with open(file, "r") as handler:
    info = json.load(handler)
channel_usernames=info["channel_username"]
group_usernames=info["group_username"]
# n=cpass['cred']['n']
n=400
#channel_name= cpass['cred']['channel_name']
#group_name=cpass['cred']['group_name']
n=int(str(n))
client =TelegramClient(phone, api_id, api_hash)
client = TelegramClient('session1', api_id, api_hash)
client.start()
#channel_usernames=channel_username.split(',')
#group_usernames=group_username.split(',')
for channel_username in channel_usernames:
    chats =client.get_messages(channel_username, limit=n) # n number of messages to be extracted
    # Get message id, message, sender id, reply to message id, and timestamp
    data_holds=[]
    if len(chats):
        for chat in chats:
            try:
                if chat.id:
                    message_id = chat.id
                else:
                    message_id = ""

                if chat.message:
                    message = chat.message
                else:
                    message = " "

                if chat.from_id:
                    sender = chat.from_id
                else:
                    sender = " "
                if chat.reply_to_msg_id:
                    reply_to = chat.reply_to_msg_id
                else:
                    reply_to = " "
                if chat.date:
                    time = chat.date
                else:
                    time = " "
                data_hold = {
                        'Message_id': message_id,
                        'Message': message,
                        'Sender_id': sender,
                        'Replay_to': reply_to,
                        'Time': str(time),

                    }
                data_holds.append(data_hold)
            except ValueError:
                continue
        post = {"date_of_scrapting": datetime.datetime.today(), "channel_username": channel_username,
                "data":data_holds}
        db.channels.insert_one(post)
    print(gr + 'Please wait.....')
    print(gr + '[+] message scraped successfully.')
gdata_holds = []
posts = {}
for group_username in group_usernames:
    chats =client.get_messages(group_username, limit=n) # n number of messages to be extracted
    # Get message id, message, sender id, reply to message id, and timestamp
    print(gr + '[+] Fetching Members...')
    #gdata_holds = []
    if len(chats):
        for chat in chats:
            try:
                if chat.id:
                    message_id=chat.id
                else:
                    message_id=""
                if chat.message:
                    message=chat.message
                else:
                    message=" "
                if chat.from_id:
                    sender=chat.from_id
                else:
                    sender=" "

                if chat.reply_to_msg_id:
                    reply_to=chat.reply_to_msg_id
                else:
                    reply_to=" "

                if chat.date:
                    time=chat.date

                else:
                    time=" "

                gdata_hold = {
                        'Message_id': str(message_id),
                        'Message': str(message),
                        'Sender_id': str(sender),
                        'Replay_to': str(reply_to),
                        'Time': str(time),

                    }
                gdata_holds.append(gdata_hold)
            except ValueError:
                continue

user_infos=[]

for group_username in group_usernames :
    participants = client.get_participants(group_username)
    #user_infos=[]
    if len(participants):
        for x in participants:
            try:
                if x.username:
                    username=x.username
                else:
                    username=" "

                if x.first_name:
                    firstname=x.first_name
                else:
                    firstname=" "
                if x.last_name:
                    lastname=x.last_name
                else:
                    lastname=""
                user_info = {
                    'User_name': username,
                    'Firstname': firstname,
                    'Lastname': lastname
                }
                user_infos.append(user_info)

            except ValueError:
                continue


post = {"group_username": group_username, "date_of_scrapting": datetime.datetime.today(),
        "group_data": gdata_holds, "group_members":user_infos}
db.groups.insert_one(post)
print(gr + 'Please wait.....')
print(gr + group_username + '[+] message scraped successfully.')