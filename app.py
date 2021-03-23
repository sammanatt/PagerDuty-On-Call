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
    schedules_list = session.rget('/schedules')
    now = datetime.now()
    now_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    for i in schedules_list:
        schedule_id = str(i['id'])
        current_oncall = session.rget('/schedules/'+schedule_id+"/users", params={'since':now_string,'until':dt_string})
        pp.pprint(i['name'] + " -- " + current_oncall[0]['name'])


#get_current_oncall()

# ("%d/%m/%Y%H:%M:%S")

now = datetime.now()
delta = timedelta(hours=2)
dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
plus2 = dt_string + datetime.timedelta(hours=2)
print("curent: ", dt_string)
print("+2: "+ plus2)




# Pseudo Code
'''
Create list of schedules
Find current person on-Call
print list of on-call schedules and their corresponding personnel
'''

#items to consider
'''
Figure out how to observe local time zone
'''
