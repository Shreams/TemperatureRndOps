################
# Using Request #
################

import requests
import re
from datetime import datetime, timedelta
import pytz
import json
import random

section2Dict = {
    "2201" : {"id" : "8315", "pin" : "1904"},
    "2202" : {"id" : "1684907", "pin" : "0707"},
    "2203" : {"id" : "1684913", "pin" : "0807"},
    "2204" : {"id" : "8324", "pin" : "5895"},
    "2205" : {"id" : "8327", "pin" : "1299"},
    "2206" : {"id" : "8328", "pin" : "2468"},
    "2207" : {"id" : "8331", "pin" : "7590"},
    "2208" : {"id" : "8332", "pin" : "9781"},
    "2209" : {"id" : "8345", "pin" : "0000"},
    "2210" : {"id" : "8355", "pin" : "2210"},
    "2211" : {"id" : "8357", "pin" : "2211"},
    "2212" : {"id" : "1685427", "pin" : "1606"},
    "2213" : {"id" : "8370", "pin" : "2213"},
    "2214" : {"id" : "8372", "pin" : "6373"},
    "2215" : {"id" : "8375", "pin" : "2215"},
    "2216" : {"id" : "1684931", "pin" : "2216"},
}
       
group_url = "https://temptaking.ado.sg/group/2424241947e5a26be7a9c10d6720c84b"
    
group_string = 'temptaking.ado.sg/group/'

if group_url.startswith(group_string):
    group_url = 'https://' + group_url
    
if group_url.startswith('https://' + group_string) or group_url.startswith('http://' + group_string):
    try:
        req_text = str(requests.get(group_url).content.decode('utf-8'))
        
        
    except:
        print("Invalid")

    def urlParse(text):
        return text[text.find('{'):text.rfind('}') + 1]

    try:
        parsed_url = json.loads(urlParse(req_text))

        section2ID = ""

        try:
            url = "https://temptaking.ado.sg/group/MemberSubmitTemperature"
            
            healthyTempMorning = [35.9,36.0,36.1,36.2,36.3,36.4]

            healthyTempAfternoon = [36.3,36.4,36.5,36.6,36.7,36.8]

            meridies = ['AM', 'PM']
            
            # Send AM & PM Temperature when available
            for meridy in meridies:

                for fourD, fourDInfo in section2Dict.items():
                    
                    # Random Temperature Generator
                    if meridy == 'AM':
                        temperature = healthyTempMorning[random.randint(0,5)]

                    if meridy == 'PM':
                        temperature = healthyTempAfternoon[random.randint(0,5)]

                    section2ID = fourD

                    payload = {
                        'groupCode': parsed_url["groupCode"],
                        'date': datetime.now(pytz.timezone('Asia/Kuala_Lumpur')).strftime('%d/%m/%Y'),
                        'meridies': meridy,
                        'memberId': fourDInfo["id"],
                        'temperature': temperature,
                        'pin': fourDInfo["pin"]
                    }
                    
                    r = requests.post(url, data=payload)
                    print(fourD, " submitted their", meridy, "temperature")

        except Exception as e:
            print(section2ID, " failed to submit their temperature")

    except:
        print("Invalid2")
        
    