# Import necessary libraries
import os
import requests
import pprint
import json
from datetime import datetime, timedelta

pp = pprint.PrettyPrinter(indent=4)

# Load environment file, assign variables
from dotenv import load_dotenv
load_dotenv()

api_token = os.environ["API_TOKEN"]

# This example uses the PDPYRAS library for Python - https://github.com/PagerDuty/pdpyras
from pdpyras import APISession
session = APISession(api_token)

def get_current_oncall():
    # get and format current time and 30 seconds for date range param
    now = datetime.now()
    delta = timedelta(hours=2)
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    plus30seconds = datetime.now() + timedelta(seconds=30)
    plus30seconds_string = plus30seconds.strftime("%Y-%m-%dT%H:%M:%S")

    # get user on-call user within the next 30 seconds for each schedule in schedules_list
    schedules_list = session.rget('/schedules')
    for i in schedules_list:
        schedule_id = str(i['id'])
        current_oncall = session.rget('/schedules/'+schedule_id+"/users", params={'since':dt_string,'until':plus30seconds_string})
        on_call_schedule = i['name']
        if len(current_oncall) <1:
            on_call_user = "No one's on call."
        else:
            on_call_user = current_oncall[0]['name']
        print(on_call_schedule + " -- " + on_call_user)
        #pp.pprint(current_oncall)

get_current_oncall()
