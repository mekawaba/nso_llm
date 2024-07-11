from __future__ import print_function 
import requests
import sys
import json
import os
import time
from flask import *
from requests_toolbelt.multipart.encoder import MultipartEncoder
import functools

token = os.getenv("WEBEX_TEAMS_ACCESS_TOKEN")
ms_flag = True

app = Flask(__name__)

def post_message(room_id,txt,token):
    global ms_flag
    if ms_flag == True:
        ms_flag = False
        m = MultipartEncoder({'roomId': room_id,'text': txt})
        r = requests.post('https://api.ciscospark.com/v1/messages', data=m,headers={'Authorization': 'Bearer %s' % token,'Content-Type': m.content_type})
    else:
        time.sleep(5)
        ms_flag = True

@app.route("/panel",methods=['GET'])    
def main_page():
    return render_template("mainpage.html")


@app.route("/",methods=['POST'])   
def handle_message():
    json = request.json

    message_id = json["data"]["id"]
    user_id    = json["data"]["personId"]
    email      = json["data"]["personEmail"]
    room_id    = json["data"]["roomId"]
    bot_id     = "yourbotid"

    print(message_id, file = sys.stdout)
    print(user_id, file=sys.stdout)
    print(email, file=sys.stdout)
    print(room_id, file=sys.stdout)


    if user_id != bot_id:
        global token
        header = {"Authorization": "Bearer %s" % token}
        get_rooms_url = "https://api.ciscospark.com/v1/messages/" + message_id
        api_response = requests.get(get_rooms_url, headers=header, verify=False)
        response_json = api_response.json()
        message = response_json["text"]
        print(message, file= sys.stdout)
        if message == "Hi" or message == "bot Hi":
            post_message(room_id,"hello world!",token)

        return "Success"
    else:
        return "Pass"


term_output_json = os.popen('curl http://127.0.0.1:4040/api/tunnels').read() 
tunnel_info = json.loads(term_output_json)
public_url = tunnel_info['tunnels'][0]['public_url']

#Webhook記録
header = {"Authorization": "Bearer %s" % token, "content-type": "application/json"}
requests.packages.urllib3.disable_warnings() #SSL警告の削除
post_message_url = "https://api.ciscospark.com/v1/webhooks"

payload = {
    "resource": "messages",
    "event": "all",
    "targetUrl": public_url,
    "name": "BotDemoWebHook"
}

api_response = requests.post(post_message_url, json=payload, headers=header, verify=False) #webhook記録

if api_response.status_code != 200:
    print('Webhook registration Error !')
    exit(0)

if __name__ == '__main__':
    app.run(host='localhost', use_reloader=True, debug=True)