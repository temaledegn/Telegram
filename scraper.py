from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import InputPeerEmpty
from telethon import TelegramClient
import asyncio
import os, sys
import configparser
import json
offset = 0
limit = 200
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    print(f"""
{re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
{re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

            version : 3.1
youtube.com/channel/UCnknCgg_3pVXS27ThLpw3xQ
        """)

cpass = configparser.RawConfigParser()
cpass.read('config.data')
loop = asyncio.get_event_loop()
try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client =TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('cls')
    banner()
    print(re+"[!] run python3 setup.py first !!\n")
    sys.exit(1)

client.start()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('cls')
    banner()
    client.sign_in(phone, input(gr+'[+] Enter the code: '+re))

os.system('cls')
banner()
chats = []
last_date = None
chunk_size = 200
groups=[]
channels=[]
result =client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
for chat in chats:
    try:
        if True:

            if len(str(chat.id))==9:
                groups.append(chat)
            else:
                channels.append(chat)
    except:
        continue
choose=" "
while choose != "group" and choose != "channel":
    choose = input("Type with correct  spelling group or channel: ").lower()
    if choose != "group" and choose != "channel":
        print("You must check the spelling type group or channel")
if choose == "group":
    chat=0
    print(re+'Choose the number from the above a group to scrape: ')
    for i in groups:
        print(gr + '[' + str(chat) + ']', i.title, i.id, i.photo,i.participants_count )
        chat += 1
    op=input(re+'Enter a number: ')
    if op == '':
        print(gr+'Ok. skipping...')
        time.sleep(1)
        sys.exit()
    else:
        pass
    opt = int(op)
    print('')
    n =int(input("please enter the number that want to scraping from the group"))
    chats =client.get_messages(groups[opt], limit=n)
    message_id =[]
    message =[]
    sender =[]
    reply_to =[]
    time = []
    print(gr+'[+] Fetching Message ...')
    if len(chats):
        for chat in chats:
            message_id.append(chat.id)
            print(chat.id)
            message.append(chat.message)
            print(chat.message)
            sender.append(chat.from_id)
            print(chat.from_id)
            reply_to.append(chat.reply_to_msg_id)
            print(chat.reply_to_msg_id)
            time.append(chat.date)
            print(chat.date)
    target_group = groups[opt]
    my_filter = ChannelParticipantsSearch('')
    all_participants = []
    mem_details = []

    yesChoice = ['yes', 'y']
    noChoice = ['no', 'n']
    input = input("Would you like to [+] Fetching Members...? (y/N) ").lower()

    # Check if our answer is in one of two sets.
    if input in yesChoice:
        all_participants = client.get_participants(target_group, aggressive=True)
        for user in all_participants:
            try:
                if user.username:
                    username = user.username
                    print(username)
                else:
                    username = ""
                if user.first_name:
                    firstname = user.first_name
                else:
                    firstname = ""
                if user.last_name:
                    lastname = user.last_name
                else:
                    lastname = ""
                    print(lastname)
                new_mem = {
                    'uid': user.id,
                    'username': username,
                    'firstname': firstname,
                    'lastname': lastname,
                    'access_hash': user.access_hash
                }
                mem_details.append(new_mem)
            except ValueError:
                continue
        with open('Group_members.txt', 'w') as w:
            json.dump(mem_details, w)
        print(gr + 'Please wait.....')
        done = input(gr + '[+] Members scraped successfully.')

    elif input in noChoice:
        # exit game
        exit
    else:
        print(re+"Invalid input.\nExiting.")
        exit


if choose == "channel":
    chat = 0
    print(re + 'Choose a channel to scrape: ')
    for i in channels:
        print(gr + '[' + str(chat) + ']', i.title, i.id, i.photo, i.username, i.access_hash, i.participants_count)
        chat += 1
    op = input(re + 'Enter a number: ')
    if op == '':
        print(gr + 'Ok. skipping...')
        time.sleep(1)
        sys.exit()
    else:
        pass
    opt = int(op)
    print('')
    n = int(input("please enter the number scraping from the channel"))
    Chats = client.get_messages(channels[opt], limit=n)
    data_holds = []
    print(gr + '[+] Fetching Members...')
    if len(chats):
        for chat in Chats:
            print(chat)
            try:
                if chat.id:
                    message_id=chat.id
                else:
                    message_id=""
                if chat.message:
                    message=chat.message
                    print(message)
                else:
                    message=" "
                if chat.from_id:
                    sender=chat.from_id
                    print(sender)
                else:
                    sender=" "
                if chat.reply_to_msg_id:
                    reply_to=chat.reply_to_msg_id
                    print(reply_to)
                else:
                    reply_to=" "
                if chat.media:
                    media=chat.media
                    print(media)
                else:
                    media=" "
                if chat.date:
                    time=chat.date
                    print(time)
                else:
                    time=" "
                data_hold={
                    'Message_id': message_id,
                    'Message': message,
                    'Sender_id':sender,
                    'Replay_to':reply_to,
                    'Time':str(time),


                }
                data_holds.append(data_hold)
            except ValueError:
                continue
        with open('channel_scraping.txt', 'w') as W:
            json.dump(data_holds, W)
        print(gr + 'Please wait.....')
        done = input(gr + '[+] message scraped successfully.')


