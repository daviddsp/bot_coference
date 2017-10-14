#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to send timed Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Alarm Bot example, sends a message after a set time.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, Job
from graphqlclient import GraphQLClient
from pprint import pprint
from time import gmtime, strftime

import logging
import json
import datetime 
import threading
import time
import sys

#Variable env
#name Bot
nameBot = "" 
#token TG
tokenTelegram = ""
#minutes pre alert messages
minutesInterval = ""

if sys.argv[1]:
    nameBot = sys.argv[1]

if sys.argv[2]:
    tokenTelegram = sys.argv[2]

if sys.argv[3]:
    minutesInterval = sys.argv[3]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def query():
    client = GraphQLClient('https://api-starsconf.synaptic.cl/graphql.?')
    result = client.execute('''
	{
  		allTalks{
            id
            name
            timeSlot {
                date
                start
                end
    
            }
            speaker {
                name
            }
            room
            category
            isPlaceholder
        } 
	}
	''')
    return result.encode("utf-8")



def main():
    updater = Updater(tokenTelegram)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()

    test(bot, update)

def start(bot, update):
    q_conference = query()
    item_dict = json.loads(q_conference)

    while True:
        for val in item_dict["data"]["allTalks"]:
            
            #Validate placeholder is true
            if val["isPlaceholder"] == True:

                #Validate speaker null
                if not (val["speaker"] is not None):
                    val["speaker"] = {u'name': u'No se especifica'}
                
                #Validate category null
                if (val["category"] == ""):
                    val["category"] = 'No se especifica'
                #Validate room A_ to A
                if val["room"] == "A_":
                    val["room"] = "A"

                now = datetime.datetime.now()
                dateNow = now.strftime("%Y-%m-%d")
                hourNow = now.strftime("%H:%M:%S")
                now_plus_10 = now + datetime.timedelta(minutes = int(minutesInterval)) #sum 10 minutes
                
                if dateNow in val["timeSlot"]["date"]: #if date now 
                    if hourNow in val["timeSlot"]["start"]:
                        bot.send_message(nameBot, 
                        text="*La Charla actual es : *"+ val["name"] + "\n"
                        "*Category: *"+ val["category"] + "\n"
                        "*Speakers: *"+ val["speaker"]["name"] + "\n"
                        "*Fecha: *"+ val["timeSlot"]["date"] + "\n"
                        "*Hora fin: *"+ val["timeSlot"]["end"] + "\n"
                        "*Sala: *"+ val["room"]+ "\n",
                        parse_mode="MARKDOWN")
                    elif now_plus_10.strftime("%H:%M:%S") in val["timeSlot"]["start"]: #if exist hours + 10 min is true conference
                        bot.send_message(nameBot, 
                        text="*La proxima charla es: *"+ val["name"] + "\n"
                        "*Category: *"+ val["category"] + "\n"
                        "*Speakers: *"+ val["speaker"]["name"] + "\n"
                        "*Fecha: *"+ val["timeSlot"]["date"] + "\n"
                        "*Hora: *"+ val["timeSlot"]["start"] + "* hasta *" + val["timeSlot"]["end"] + "\n"
                        "*Sala: *"+ val["room"]+ "\n",
                        parse_mode="MARKDOWN")
        time.sleep(2)                    

if __name__ == '__main__':
    
    main()
    