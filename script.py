################
# Using Request #
################

import requests
import re
from datetime import datetime, timedelta
import pytz
import json
import random

syndicate1Dict = {
    "1123" : {"id" : "13922093", "pin" : "1123"},
}
       
group_url = "https://temptaking.ado.sg/group/27cd67d30abdcee200f6aa62e9984f43"
    
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

        syndicate1ID = ""

        try:
            url = "https://temptaking.ado.sg/group/MemberSubmitTemperature"
            
            healthyTempMorning = [35.9,36.0,36.1,36.2,36.3,36.4]

            healthyTempAfternoon = [36.3,36.4,36.5,36.6,36.7,36.8]


            for fourD, fourDInfo in syndicate1Dict.items():

                syndicate1ID = fourD
                
                # Random Temperature Generator
                # Between 6pm to 12pm
                if datetime.now(pytz.timezone('Asia/Kuala_Lumpur')).hour < 12 and datetime.now(pytz.timezone('Asia/Kuala_Lumpur')).hour > 6  :
                    print('bye')
                    temperature = healthyTempMorning[random.randint(0,5)]

                else :
                    meridy = 'PM'
                    temperature = healthyTempAfternoon[random.randint(0,5)]
                    

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
            print(syndicate1ID, " failed to submit their temperature")

    except:
        print("Invalid2")
        

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run()