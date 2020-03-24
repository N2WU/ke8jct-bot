import os
import json
import sys
import random
import time

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  
  List = ["I don't know", "watts.", "Ask brad.", "BANG!", "I don't care", "I don't know", "screw the frogs", "Sorry im busy", "bike at 7", "who has the normatecs", "Super League Champion!", "treadmill run tomorrow", "Gains-->Gone", "I don't know"]
  catchphrase = random.choice(List)
  Flag = False
    
  # We don't want to reply to ourselves! 
  if data['name'].find("Gabe") >= 0:
    msg = '^'
    send_message(msg)
    Flag = True
  if data['name'].find("Amy") >= 0:
    msg = '^'
    send_message(msg)
    Flag = True
  if data['name'].find("Payton") >= 0:
    msg = '@{}, i disagree'.format(data['name'])
    send_message(msg)
    Flag = True
  if data['name'].find("Rylie") >= 0:
    msg = '<3'
    send_message(msg)
    Flag = True
  if data['text'].endswith('?') == True and Flag==False:
    Flag = True
    msg = 'ask your team leader'
    send_message(msg)

  if data['text'].find("navy") >= 0 and Flag == False:
    msg = 'Beat Navy!'
    send_message(msg)
    
  if data['text'].find("thomas") >= 0 and Flag == False:
    msg = catchphrase
    send_message(msg)
    
  if data['text'].find("Thomas") >= 0 and Flag == False:
    msg = catchphrase
    send_message(msg)
 """
  if data['name'] != 'Bill':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    send_message(msg)
 """    
 
 return "ok", 200
  
def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  

  
def log(msg):
  print(str(msg))
  sys.stdout.flush()