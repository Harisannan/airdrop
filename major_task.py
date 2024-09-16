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


def swipe_coin():
    url = "https://major.bot/api/swipe_coin/"

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

def durov():
    url = "https://major.bot/api/durov/"

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