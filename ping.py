# Packages
import os
import subprocess
import datetime
import re
from sendgrid import SendGridAPIClient #sendgrid will need to be imported (run 'py -m pip install sendgrid' in new terminal window)
from sendgrid.helpers.mail import Mail
from tabulate import tabulate #tabulate will need to be imported (run 'py -m pip install tabulate' in command prompt)

# Files
import settings
import locations
from locations import get_locations
from settings import *

not_active_endings = []
locations = get_locations()

def check_ping(ending):
    host = settings.IP_PRE + ending
    response = subprocess.Popen(
        ['ping', '-n', '4', host], stdout=subprocess.PIPE).communicate()[0].decode('UTF-8')
    response = response.replace('\n', '')
    loss = re.findall(r'\(.*(?= loss)', response)[0]
    loss = loss[1:]
    print(host + " --> Active (" + loss + " loss)") if loss == "0%" else print(host +
                                                                               " --> Not Active (" + loss + " loss)")
    if loss != "0%":
        not_active_endings.append(ending)

def lookup_ending(ending):
    locs = [l for l in locations if l.ending == int(ending)]
    if len(locs) == 0:
        return None
    if len(locs) == 1:
        return locs[0]
    if len(locs) >= 1:
        return None

def send_email():
    today = datetime.datetime.now()
    brokenListHeaders = ["IP", "Location", "Linksys"]
    brokenListTable = []
    for ending in not_active_endings:
        loc = lookup_ending(ending)
        if loc != None and loc.ignore == False and loc.linksys == False: #Ignore Linksys routers (time out)
            brokenListTable.append(["10.10.96." + ending, loc.loc, loc.linksys])
    brokenList = tabulate(brokenListTable, brokenListHeaders, tablefmt="psql")
    print(brokenList)
    message = Mail(
        from_email=settings.FROM_EMAIL,
        to_emails=settings.TO_EMAIL,
        subject=settings.SUBJECT,
        html_content="<b>" + str(today) + "</b><br><br>An access point(s) is broken. Please see the list below.\n\n<pre>" + brokenList + "</pre>\n\nThis is an automated message. Replies will not be received."
    )
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        # print(response.status_code) These can be used to debug (202 == success)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e.message)
    return True if str(response.status_code)[:1] else False

def run():
    for i in range(settings.minEnding, settings.maxEnding):
        loc = lookup_ending(i)
        if loc != None and loc.ignore == False and loc.linksys == False:
            check_ping(str(i))
    if len(not_active_endings) == 0:
        print("No access points are down. No message needed to be sent.")
        return
    email_response = send_email()
    if email_response: 
        print("Message successful!")
    else:
        print("[Error] Message should have been sent, BUT DID NOT. Please check code.")

run()