import random
import requests
import json

def paint(headers):
    color = ['#811E9F','#3690EA']
    while True:
        url = 'https://notpx.app/api/v1/repaint/start'
        payload = {"pixelId":random.randint(24,1000000),"newColor":random.choice(color)}

        response = requests.post(url, headers=headers, json=payload)
        print(response.text)
        print('mengetap.....')
        if 'insufficient charges amount' in response.text :
            print('saldo tap tape entek mas')
            break
        else :
            continue



headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": f"initData {input('masukkan user==>> ')}",
    "Content-Length": "40",
    "Content-Type": "application/json",
    "Origin": "https://app.notpx.app",
    "Priority": "u=1, i",
    "Referer": "https://app.notpx.app/",
    "Sec-Ch-Ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

paint(headers)