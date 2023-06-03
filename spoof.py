import os
import sys
import time
from os import system
from time import sleep

try:
    import requests
except ImportError:
    os.system('apt-get install python3')
    os.system('pip3 install requests')

try:
	request = requests.get("https://www.google.com/search?q=cats", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] Oops, It looks like you have no Internet [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)




hprint(G + ' Starting ...')

print ("")
name = sys.argv[1]
sender = sys.argv[2]
receiver = sys.argv[3]
subject = (C + "Very Real Email" + Y + " --> " + G)
body = (C + "Send 200 bucks to riya543216@oksbi to proceed" + Y + " --> " + G)


files = {
    'sender_name': (None, name),
    'sender_email': (None, sender),
    'reciever_email': (None, receiver),
    'subject': (None, subject),
    'message': (None, body),
    'submit': (None, "submit"),
}
response = requests.post('https://chaffier-song.000webhostapp.com/send.php', files=files)
hprint(C + ' Sending email to ' + receiver + ' ...')
print("")
print(G + " " + response.text)