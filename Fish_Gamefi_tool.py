import requests
import json
from datetime import datetime
import time
wallet = "0x3ed3411a5AE2724c40aCE934Ded8b40AF11F8A44"
private = "d3224013b7544f7693cf9b0aaec03f6399f3ffcb5d0c427bb8cb730ce65f7851"

def check_can(key):
    headers = {
    'authority': 'api.fishcrypto.io',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': 'application/json, text/plain, */*',
    'authorization': key,
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://play.fishcrypto.io',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://play.fishcrypto.io/',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    }
    headers_2 = {
    'authority': 'api.fishcrypto.io',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'authorization': key,
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://play.fishcrypto.io',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://play.fishcrypto.io/',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    }
    params = (
    ('limit', '999'),
    ('offset', '0'),
    )
    response = requests.get(
        'https://api.fishcrypto.io/available-rods', headers=headers, params=params)
    json_decode = json.loads(response.content)
    print('Tab 1')
    for x in json_decode['data']:
        for xzz in range(1, 8):
            data_cau = '{"rodId":"'+x['id']+'","position":'+str(xzz)+'}'
            response = requests.post(
                'https://api.fishcrypto.io/pick-up-rod', headers=headers_2, data=data_cau)
            json_decode_cau = json.loads(response.content)
            if json_decode_cau['status'] == 'success':
                print("Đã Đặt Câu")
                break
        time.sleep(2)
    response_fr = requests.get(
        'https://api.fishcrypto.io/user-parent', headers=headers_2)
    json_decode_fr = json.loads(response_fr.content)
    if json_decode_fr['data']:
        response_can_fw = requests.get('https://api.fishcrypto.io/available-borrow-rods/' +
                                       json_decode_fr['data']['id']+'?limit=999&offset=0', headers=headers_2)
        json_decode_can_fw = json.loads(response_can_fw.content)
        if json_decode_can_fw['data']:
            for xzz in range(1, 4):
                data_cau = '{"rodId":"' + json_decode_can_fw['data'][0]['id'] +'","position":'+str(xzz)+'}'
                response = requests.post(
                    'https://api.fishcrypto.io/pick-up-friend-rod', headers=headers_2, data=data_cau)
                json_decode_cau = json.loads(response.content)
                if json_decode_cau['status'] == 'success':
                    print("Đã Đặt Cần Câu Bạn ID " +json_decode_can_fw['data'][0]['id'])
                    break
                time.sleep(3)
    response_frs = requests.get(
        'https://api.fishcrypto.io/f1s?limit=999&offset=0', headers=headers_2)
    json_decode_frs = json.loads(response_frs.content)
    for x in json_decode_frs['data']:
        response_can_fw = requests.get(
            'https://api.fishcrypto.io/available-borrow-rods/'+x['id']+'?limit=999&offset=0', headers=headers_2)
        json_decode_can_fw = json.loads(response_can_fw.content)
        if json_decode_can_fw['data']:
            for xzz in range(1, 4): 
                    data_cau = '{"rodId":"' + json_decode_can_fw['data'][0]['id'] +'","position":'+str(xzz)+'}'
                    response = requests.post('https://api.fishcrypto.io/pick-up-friend-rod', headers=headers_2, data=data_cau)
                    json_decode_cau = json.loads(response.content)
                    if json_decode_cau['status'] == 'success':
                        print("Đã Đặt Cần Câu Bạn ID " +json_decode_can_fw['data'][0]['id'])
                        break
                    time.sleep(3)
    print("Đang Claim - Bán Cá")
    data = '{}'
    response = requests.post(
        'https://api.fishcrypto.io/claim-all-reward', headers=headers_2, data=data)
    # bán cá
    response_fish = requests.get(
        'https://api.fishcrypto.io/my-fishes?limit=200&offset=0', headers=headers_2)
    json_decode = json.loads(response_fish.content)
    for x in json_decode['data']:
        data = '{}'
        response = requests.post(
            'https://api.fishcrypto.io/sell-fish/'+x['id'], headers=headers_2, data=data)
        time.sleep(2)
    response_me = requests.get(
        'https://api.fishcrypto.io/me', headers=headers_2)
    json_decode = json.loads(response_me.content)
    print('Balance Coin ' + str(json_decode['data']['balance']))
    if json_decode['data']['baitCount'] <= 50:
        json_data = {}
        requests.post('https://api.fishcrypto.io/buy-bait', headers=headers_2, json=json_data)
    print("==============================================================")
    print("Kiểm Tra Lại Sau 120s")
    time.sleep(120)
    login()
def login():
    headers = {
    'authority': 'api.fishcrypto.io',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'accept': 'application/json, text/plain, */*',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://play.fishcrypto.io',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://play.fishcrypto.io/',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    }
    json_data = {'walletAddress': wallet,}
    response = requests.post('https://api.fishcrypto.io/login', headers=headers, json=json_data)
    json_data = json.loads(response.content)
    data_login = "Otp code: "+json_data['data']['verifyCode']
    private_key_hex = private
    msg = data_login
    json_data_sing = {'data': msg,'private_key': private_key_hex}
    response_sing = requests.post('https://skg-tienplaygirl.herokuapp.com/', data=json_data_sing)
    json_data_sing = json.loads(response_sing.content)
    headers = {
    'authority': 'api.fishcrypto.io',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'accept': 'application/json, text/plain, */*',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://play.fishcrypto.io',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://play.fishcrypto.io/',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    }
    json_data = {
    'walletAddress': wallet,
    'sign': json_data_sing['signature'],
    }
    response = requests.post('https://api.fishcrypto.io/verify-login', headers=headers, json=json_data)
    jsonz = json.loads(response.content)
    check_can(jsonz['data']['access_token'])
login()