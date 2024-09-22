#query_id=AAGpXvtIAAAAAKle-0h-pQAk&user=%7B%22id%22%3A1224433321%2C%22first_name%22%3A%22%F0%9F%90%A4%20Haris%20Gra-Gra%22%2C%22last_name%22%3A%22%7C%7C%20never%20rungkad%20%F0%9F%A6%B4%22%2C%22username%22%3A%22Harisannanda%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1726455091&hash=938f6e09d4c673386286275440c60d1c5bf44dde9a40be7735773ff6bef8e67b

import json
import requests





import requests
import random
import time


answer_task = input('nugas mas? [y/n] ==>> ')

a = 11
b = 4
c = 12
d = 2



def daily(bearer):
    url = "https://major.bot/api/user-visits/streak/"
    url2 = "https://major.bot/api/user-visits/visit/"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": bearer,
        "Priority": "u=1, i",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }


    sesi_get = requests.get(url, headers=headers)
    sesi_get2 = requests.post(url2, headers=headers).json()
    if sesi_get2['is_increased'] == True:
        print("Daily claim done")



def hold_coin(bearer):
    url = "https://major.bot/api/bonuses/coins/"


    payload = {
        'coins' : random.randint(850,915)
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": bearer,
        "Priority": "u=1, i",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    headers_claim = {
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": bearer,
        "Content-Length": "13",  # Assuming the payload length is 13 characters (adjust if needed)
        "Content-Type": "application/json",
        "Origin": "https://major.bot",
        "Priority": "u=1, i",
        "Referer": "https://major.bot/games/hold-coin",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    sesi_get = requests.get(url, headers=headers)
    if 'blocked_until' in sesi_get.text:
        pass
    else :
        print('holding.....')
        time.sleep(60)
        sesi_post = requests.post(url, headers=headers_claim, json=payload)
        print(sesi_post.text)


def swipe_coin(bearer):
    url = "https://major.bot/api/swipe_coin/"

    payload = {
        'coins': random.randint(2800, 3000)
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": bearer,
        "Priority": "u=1, i",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    headers_claim = {
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": bearer,
        "Content-Length": "14",  # Assuming the payload length is 13 characters (adjust if needed)
        "Content-Type": "application/json",
        "Origin": "https://major.bot",
        "Priority": "u=1, i",
        "Referer": "https://major.bot/games/swipe-coin",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    sesi_get = requests.get(url, headers=headers)
    if 'blocked_until' in sesi_get.text:
        pass
    else:
        print('swipe coin.....')
        time.sleep(60)
        sesi_post = requests.post(url, headers=headers_claim, json=payload)
        print(sesi_post.text)

def durov(bearer):
    url = "https://major.bot/api/durov/"


    payload = {
        "choice_1": a,
        "choice_2": b,
        "choice_3": c,
        "choice_4": d
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": bearer,
        "Priority": "u=1, i",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    headers_claim = {
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": bearer,
        "Content-Length": "14",  # Assuming the payload length is 13 characters (adjust if needed)
        "Content-Type": "application/json",
        "Origin": "https://major.bot",
        "Priority": "u=1, i",
        "Referer": "https://major.bot/games/swipe-coin",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    sesi_get = requests.get(url, headers=headers)
    if 'blocked_until' in sesi_get.text:
        pass
    else:
        print('mengdurov.....')
        time.sleep(0)
        sesi_post = requests.post(url, headers=headers_claim, json=payload)
        print(sesi_post.text)


def roulette(bearer):
    url = "https://major.bot/api/roulette/"


    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": bearer,
        "Priority": "u=1, i",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }


    sesi_get = requests.get(url, headers=headers)
    if 'blocked_until' in sesi_get.text:
        pass
    else:
        print('mengocok rolet.....')
        sesi_post = requests.post(url, headers=headers, json=payload)
        print(sesi_post.text)



















query_file = open('data.txt','r+').read()
querys = query_file.split('\n')
for query in querys :
    url = "https://major.bot/api/auth/tg/"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    payload = {
        "init_data": query
    }


    response = requests.post(url, headers=headers, json=payload).json()

    bearer_key = f'Bearer {response['access_token']}'
    print(bearer_key)

    daily(bearer_key)
    hold_coin(bearer_key)
    swipe_coin(bearer_key)
    durov(bearer_key)
    roulette(bearer_key)




    get_task_false_url = "https://major.bot/api/tasks/?is_daily=false"
    get_task_true_url = "https://major.bot/api/tasks/?is_daily=true"
    task_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": bearer_key,
        "Priority": "u=1, i",
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }
    task_true = requests.get(get_task_true_url, headers=task_headers).json()
    task_false = requests.get(get_task_false_url, headers=task_headers).json()
    if answer_task == 'y':
        for data in task_true:
            task_id = data['id']
            url_submit_task = 'https://major.bot/api/tasks/'
            payload_task = {
                'task_id' : task_id
            }
            time.sleep(1)
            response_task = requests.post(url_submit_task, headers=task_headers, json=payload_task).json()
            try :
                print(f"mengerjakan tugas dengan id ==>> {response_task['task_id']}")
                if response_task['is_completed'] == True:
                    print("status : tugas berhasil di kerjakan")
                else:
                    print("status : tugas tidak dapat di handle")
            except KeyError:
                print(f"status tugas : {response_task['detail']}")
        for data in task_false:
            task_id = data['id']
            url_submit_task = 'https://major.bot/api/tasks/'
            payload_task = {
                'task_id' : task_id
            }
            time.sleep(1)
            response_task = requests.post(url_submit_task, headers=task_headers, json=payload_task).json()
            try:
                print(f"mengerjakan tugas dengan id ==>> {response_task['task_id']}")
                if response_task['is_completed'] == True:
                    print("status : tugas berhasil di kerjakan")
                else:
                    print("status : tugas tidak dapat di handle")
            except KeyError :
                print(f"status tugas : {response_task['detail']}")


    url_submit_task = 'https://major.bot/api/tasks/'
    payload_task = {
        "task_id": 92,
        "payload": {"code": "070624"}
    }
    time.sleep(1)
    response_task = requests.post(url_submit_task, headers=task_headers, json=payload_task).json()
    print(response_task)