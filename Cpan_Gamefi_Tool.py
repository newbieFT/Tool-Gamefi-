import requests
import json
from datetime import datetime
import time
from html2image import Html2Image
hti = Html2Image()
import base64
headers = {
    'authority': 'cryptoplanes.me',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://cryptoplanes.me/play/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'connect.sid=s%3AMqSFPFsC5jLaKJDbCbX6O8ipkWCxBGYa.0oJEOz4Xu3C6E1Bneucnw%2Bgxh9KH1hwV0sFSvjVvMRE; _ga=GA1.1.1331247338.1640225895; cf_chl_2=123fc26920b85c9; cf_chl_prog=x13; cf_clearance=dSoWKiU7d19N352Xk9mO73Y34XYNo.1VZkXqAufW8o0-1643045965-0-150; _ga_D5XDL86HEP=GS1.1.1643045962.142.1.1643046011.0',
    'if-none-match': 'W/"52c-CwWErpkkyAY2odyn+TlaEDgu5SE"',
}
response = requests.get('https://cryptoplanes.me/plane/get', headers=headers)
json_decode = json.loads(response.content)
for x in json_decode['planes']:
    if x['current_fuel'] == 0:
        print('[Đã Đua] ID Máy Bay:' + x['_id'])
    else:
        i = 0
        print('[chưa Đua] ID Máy Bay:' + x['_id'])
        print('[Đang Đua...]  - ID Máy Bay: ' +
              x['_id'])
        fuel = x['fuel']
        current_fuel = x['current_fuel']
        while i < current_fuel/15:
            i += 1
            response = requests.get('https://cryptoplanes.me/user/captcha/'+ x['_id'], headers=headers)
            print('[Đang Giải Captcha]')
            json_decode = json.loads(response.content)
            html = json_decode['data']
            hti.size = (220, 120)
            hti.screenshot(html_str=html,size = (220, 120), save_as='red_page.png')
            with open("red_page.png", "rb") as img_file:
                my_string = base64.b64encode(img_file.read())
                data = {'key': '998ddf29dd83ba99141847ef804ed4f9','method': 'base64','body': my_string}
                response = requests.post('http://2captcha.com/in.php?json=1',data=data)
                json_dua = json.loads(response.content)
                if json_dua['status'] == 1:
                    print('[ID Captcha] : '+ json_dua['request'])
                    time.sleep(20)
                    response_res = requests.get('https://2captcha.com/res.php?key=998ddf29dd83ba99141847ef804ed4f9&action=get&json=1&id='+json_dua['request'])
                    json_dua_res = json.loads(response_res.content)
                    print('[Đã Giải Captcha Thành Công] : '+ json_dua_res['request'])
                    #đua
                    data = {'id': x['_id'],'captcha': json_dua_res['request']}
                    response = requests.post('https://cryptoplanes.me/plane/training/virtual', headers=headers, data=data)
                    if response.content == 'Captcha invalid':
                        print('Captcha Sai')
                    else:
                        json_decode = json.loads(response.content)
                        print('[Đua Thành Công ] Token Cliam : '+ str(json_decode['reward']['token']))
                else:
                    print('[Lấy ID Captcha Thất Bại]')
            time.sleep(10)