import requests
import json
import time
from html2image import Html2Image
hti = Html2Image()
import base64

headers = {
    'authority': 'api.b-aoe.io',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJiYW9lYWNjLWp3dCIsInN1YiI6eyJpZCI6OTIzNCwidXNlck5hbWUiOiIiLCJzdGF0dXMiOiIwIiwiZXRoQWRkcmVzcyI6IjB4NDdFMjFhODc0MTUxOTBkYWJGMTc2ZjkwRDQ3YzEzQzg4NWQxRTdBMiIsIndhbGxldEFkbWluIjoiMCIsInBzV2hpdGVsaXN0IjowLCJwc1RyYW5zZmVyIjowLCJwc1BhY2thZ2UiOjAsInByaXZhdGVWZXN0aW5nIjowLCJpZG9WZXN0aW5nIjowLCJhcGlVcmwiOiJodHRwczpcL1wvYXBpLmItYW9lLmlvIiwiZmNtX2VuYWJsZSI6IjEiLCJ3YWxsZXQiOiJtZXRhbWFzayJ9LCJpYXQiOjE2NDczMjQ1OTcsImV4cCI6MTY0NzM0NjE5N30.ayhV-0BB808uctZCxzidzCphss9DtdurkhZNFUUZVk0',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://b-aoe.io',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://b-aoe.io/',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
}

def run():
    response = requests.get('https://api.b-aoe.io/game/me/robot/list', headers=headers)
    json_decode = json.loads(response.content)
    for x in json_decode['robots']:
        if x['remainTurn'] == 0:
            print('[Đã Đua] ID RoBot:' + x['robotId'])
        else:
            i = 0
            print('[Chưa Đua] RoBot:' + x['robotId'])
            print('[Đang Đua...]  - ID RoBot: ' + x['robotId'])
            fuel = x['remainTurn']
            current_fuel = x['remainTurn']
            while i < current_fuel/15:
                i += 1
                data = '{"robotId":'+x['robotId']+',"captcha":null}'
                response = requests.post('https://api.b-aoe.io/game/play/ready-auto', headers=headers, data=data)
                print('[Đang Giải Captcha]')
                json_decode = json.loads(response.content)
                captcha = json_decode['autoPlay']['capcha']
                data = {'key' : '998ddf29dd83ba99141847ef804ed4f9', 'method' : 'base64', 'body' : captcha[22:]}
                response = requests.post('http://2captcha.com/in.php?json=1', data=data)
                json_dua = json.loads(response.content)
                if json_dua['status'] == 1 :
                    print('[ID Captcha] : ' + json_dua['request'])
                    time.sleep(20)
                    response_res = requests.get(
                        'https://2captcha.com/res.php?key=998ddf29dd83ba99141847ef804ed4f9&action=get&json=1&id=' +
                        json_dua['request'])
                    json_dua_res = json.loads(response_res.content)
                    print('[Đã Giải Captcha Thành Công] : ' + json_dua_res['request'])
                    # đua
                    data = '{"robotId":'+x['robotId']+',"captcha":"'+json_dua_res['request']+'"}'
                    response = requests.post('https://api.b-aoe.io/game/play/auto', headers=headers, data=data)
                    json_decode = json.loads(response.content)
                    print(response.content)
                else :
                    print('[Lấy ID Captcha Thất Bại]')
                time.sleep(10)

for i in range(0, 3):
    run()