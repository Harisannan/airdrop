import random

import requests
import json
import os
import time
import datetime





qst = input('kerjakan tugas y/n ==>>')




def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('otw kerja lagi.....')
def cek_type_diamond(headers):
    url = "https://fintopio-tg.fintopio.com/api/hold/fast/init"
    response = requests.get(url, headers=headers).json()
    diamond_id = response['clickerDiamondState']['diamondNumber']
    next_time_diamond = response['clickerDiamondState']['timings']['nextAt']
    print(diamond_id)
    print(f"time next tap : {next_time_diamond}")


    url2 = 'https://fintopio-tg.fintopio.com/api/clicker/diamond/complete'
    payload = {
        'diamondNumber' : f'{diamond_id}'
    }
    respons2 = requests.post(url2, headers=headers, json=payload)

    return next_time_diamond
def check_in_daily(headers):
    url = "https://fintopio-tg.fintopio.com/api/daily-checkins"
    response = requests.post(url, headers=headers).json()
    print(response)



def task(headers):
    farming_claim_url = "https://fintopio-tg.fintopio.com/api/farming/claim"
    requests.post(farming_claim_url, headers=headers).json()
    url = "https://fintopio-tg.fintopio.com/api/farming/farm"
    response = requests.post(url, headers=headers).json()
    print(response)
    #lihat tugas dan klaim
    url_task = 'https://fintopio-tg.fintopio.com/api/hold/tasks'
    task_response = requests.get(url_task, headers=headers).json()
    print(task_response)
    task_ids = task_response['tasks']
    for ids in task_ids :
        task_url = f"https://fintopio-tg.fintopio.com/api/hold/tasks/{ids['id']}/start"
        print('mengerjakan tugas...')
        response_task = requests.post(task_url, headers=headers)
        print('melakukan klaim hasil tugas')
        claim_url = f"https://fintopio-tg.fintopio.com/api/hold/tasks/{ids['id']}/claim"
        claim_response = requests.post(claim_url, headers=headers).json()




n = 0
target_time = 0
query_file = open('data.txt','r+').read()
querys = query_file.split('\n')
while True :
    for query in querys :
        while True :
            try :
                if query == '' :
                    break
                else :
                    os.system('clear')
                    print(f'akun ke - {n+1}')
                    main_headers = {
                        "accept": "application/json, text/plain, */*",
                        "accept-encoding": "gzip, deflate, br, zstd",
                        "accept-language": "en-US,en;q=0.9",
                        "priority": "u=1, i",  # Note the space between comma and "i"
                        "referer": "https://fintopio-tg.fintopio.com/",
                        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": '"Windows"',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                        "webapp": "true"
                    }

                    url = f'https://fintopio-tg.fintopio.com/api/auth/telegram?{query}'

                    response = requests.get(url,headers=main_headers).json()

                    bearer_code = "Bearer "+response['token']


                    print(bearer_code)

                    headers = {
                        "accept": "application/json, text/plain, */*",
                        "accept-encoding": "gzip, deflate, br, zstd",
                        "accept-language": "en-US,en;q=0.9",
                        "authorization": bearer_code,
                        "priority": "u=1, i",  # Note the space between comma and "i"
                        "referer": "https://fintopio-tg.fintopio.com/",
                        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": '"Windows"',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                        "webapp": "true"
                    }
                    target_time = cek_type_diamond(headers)
                    check_in_daily(headers)
                    if qst == 'y' :
                        task(headers)
                    n = n+1
                    countdown(random.randint(1,60))
                    break
            except:
                print("menjalankan ulang............")
                time.sleep(2)

    now = datetime.datetime.now()

    # Format waktu lengkap dengan nama hari, tanggal, bulan, tahun, jam, menit, dan detik

    time_now = time.time()
    delta_time = f"{target_time/1000 - time_now}"
    delta_time = int(delta_time.split('.')[0]) + 1
    countdown(delta_time)
    n = 0
    target_time = 0