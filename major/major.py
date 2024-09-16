#query_id=AAGpXvtIAAAAAKle-0h-pQAk&user=%7B%22id%22%3A1224433321%2C%22first_name%22%3A%22%F0%9F%90%A4%20Haris%20Gra-Gra%22%2C%22last_name%22%3A%22%7C%7C%20never%20rungkad%20%F0%9F%A6%B4%22%2C%22username%22%3A%22Harisannanda%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1726455091&hash=938f6e09d4c673386286275440c60d1c5bf44dde9a40be7735773ff6bef8e67b

import json
import requests





import requests
import random
import time
a = input('no durov 1 ==> ')
b = input('no durov 2 ==> ')
c = input('no durov 3 ==> ')
d = input('no durov 4 ==> ')
bearer = input("masukkan bearer ==>> ")


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
    session = requests.Session()
    sesi_get = session.get(url, headers=headers)
    print(sesi_get.text)

    time.sleep(60)
    sesi_post = session.post(url, headers=headers_claim, json=payload)
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
    session = requests.Session()
    sesi_get = session.get(url, headers=headers)
    print(sesi_get.text)

    time.sleep(60)
    sesi_post = session.post(url, headers=headers_claim, json=payload)
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
    session = requests.Session()
    sesi_get = session.get(url, headers=headers)
    print(sesi_get.text)

    time.sleep(60)
    sesi_post = session.post(url, headers=headers_claim, json=payload)
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

    session = requests.Session()
    sesi_get = session.get(url, headers=headers)
    print(sesi_get.text)

    time.sleep(3)
    sesi_post = session.post(url, headers=header)
    print(sesi_post.text)



















query_file = open('data','r+')
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

    hold_coin(bearer_key)
    swipe_coin(bearer_key)
    durov(bearer_key)
    roulette(bearer_key)