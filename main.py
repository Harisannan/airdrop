import os
import time
import random
import requests

# Define the headers and URLs for the requests
play_game_url = "https://game-domain.blum.codes/api/v1/game/play"
claim_token_url = "https://game-domain.blum.codes/api/v1/game/claim"

query_header = {
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Length": "379",
    "Content-Type": "application/json",
    "Lang": "en",
    "Origin": "https://telegram.blum.codes",
    "Priority": "u=1, i",
    "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}



query_url = 'https://user-domain.blum.codes/api/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP'

query_payload = {
    'query':'query_id=AAGng6x6AgAAAKeDrHoBCoBE&user=%7B%22id%22%3A6353093543%2C%22first_name%22%3A%22ryan%22%2C%22last_name%22%3A%22thang%20%7C%7C%20Never%20dm%20first%20%F0%9F%A6%B4%22%2C%22username%22%3A%22ryanbust%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1726496492&hash=126e05c74ae423e12acdc4b8a2dd4a183fed89a316972973d9e2603e9cb313f3'
}
response_query = requests.post(query_url, headers=query_header, json=query_payload)


print(response_query.status_code)
bearer_code = f'Bearer {response_query.text}'

print(bearer_code)


tanya = input('sekalian nugas mas?\n\n\n\n[n]ndak\n[y]yoi\n>>>')
headers_cek_balance = {
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    'Authorization' : bearer_code,
    "content-length": "0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

headers_play_game = {
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    'authorization' : bearer_code,
    "content-length": "0",
    "origin": "https://telegram.blum.codes",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

headers_claim_token = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    'authorization' : bearer_code,
    "content-length": "61",
    "content-type": "application/json",
    "origin": "https://telegram.blum.codes",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}



def tap_tap():
    tap_tap_count = 0
    while True:
        if tanya == 'y':
            headers_tasks = {
                "Authorization": bearer_code,
                "origin": "https://telegram.blum.codes",
                "priority": "u=1, i",
                "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
            }

            response_tasks = requests.get('https://earn-domain.blum.codes/api/v1/tasks', headers=headers_tasks).json()
            for i in response_tasks:
                data_task = i['tasks']
                for a in data_task:
                    if 'NOT_STARTED' in a['status']:
                        print(f"id : {a['id']}")
                        print(f"Iconfilekey : {a['iconFileKey']}")
                        url_start_task = f"https://earn-domain.blum.codes/api/v1/tasks/{a['id']}/start"
                        response_start = requests.post(url_start_task, headers=headers_tasks)
                        url_claim_tasks = f"https://earn-domain.blum.codes/api/v1/tasks/{a['id']}/claim"
                        response_claim = requests.post(url_claim_tasks, headers=headers_tasks)
                    else :
                        pass
                    for b in a['subTasks']:
                        if 'NOT_STARTED' in b['status'] :
                            time.sleep(1)
                            print(f"id : {b['id']}")
                            print(f"Iconfilekey : {b['iconFileKey']}")
                            url_start_task = f"https://earn-domain.blum.codes/api/v1/tasks/{b['id']}/start"
                            response_start = requests.post(url_start_task, headers=headers_tasks)
                            url_claim_tasks = f"https://earn-domain.blum.codes/api/v1/tasks/{b['id']}/claim"
                            response_claim = requests.post(url_claim_tasks, headers=headers_tasks)
                        else:
                            pass
        else:
            pass
        break
        # Make the request to play the game
        # response_play_game = requests.post(play_game_url, headers=headers_play_game)
        #
        # # Check if the request was successful
        # if response_play_game.status_code == 200:
        #     game_response = response_play_game.json()
        #     game_id = game_response.get("gameId")
        #     print(f"Game ID: {game_id}")
        #     time.sleep(random.randint(35,40))
        #     random_tap_num = random.randint(160, 280)
        #     claim_payload = {
        #         "gameId": game_id,
        #         "points": random_tap_num
        #     }
        #
        #     # Make the request to claim the token
        #     response_claim_token = requests.post(claim_token_url, headers=headers_claim_token, json=claim_payload)
        #     print(f"point di dapatkan : {random_tap_num}")
        #     # Check if the request was successful
        #     if response_claim_token.status_code == 200:
        #         claim_response = response_claim_token.text
        #         print("Token claimed successfully:", claim_response)
        #         tap_tap_count = tap_tap_count+random_tap_num
        #     else:
        #         print("Failed to claim token. Status Code:", response_claim_token.status_code)
        #         print("Response:", response_claim_token.text)
        #     # Prepare the payload for the claim token request
        # else:
        #     os.system('clear')
        #     print('done mas')
        #     print(f"total poin dari tap tap : {tap_tap_count}")
        #     break





tap_tap()