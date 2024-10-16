import os
import time
import random
import requests

# Define the headers and URLs for the requests
play_game_url = "https://game-domain.blum.codes/api/v1/game/play"
claim_token_url = "https://game-domain.blum.codes/api/v1/game/claim"

bearer_code = input('masukkan bearer ==>> ')
tanya = input('sekalian nugas mas?\n\n\n\n[n]ndak\n[y]yoi\n>>>')
headers_cek_balance = {
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    'Authorization': bearer_code,
    "content-length": "0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

headers_play_game = {
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    'authorization': bearer_code,
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
    'authorization': bearer_code,
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



            start_url = "https://earn-domain.blum.codes/api/v1/tasks/3c048e58-6bb5-4cba-96cb-e564c046de58/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = "https://earn-domain.blum.codes/api/v1/tasks/3c048e58-6bb5-4cba-96cb-e564c046de58/validate"
            payload_answer = {
                "keyword": "SUPERBLUM"
            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = "https://earn-domain.blum.codes/api/v1/tasks/3c048e58-6bb5-4cba-96cb-e564c046de58/claim"

            requests.post(claim_url, headers=headers_tasks)

            start_url = "https://earn-domain.blum.codes/api/v1/tasks/835d4d8a-f9af-4ff5-835e-a15d48e465e6/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = "https://earn-domain.blum.codes/api/v1/tasks/835d4d8a-f9af-4ff5-835e-a15d48e465e6/validate"
            payload_answer = {
                "keyword": "CRYPTOBLUM"
            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = "https://earn-domain.blum.codes/api/v1/tasks/835d4d8a-f9af-4ff5-835e-a15d48e465e6/claim"

            requests.post(claim_url, headers=headers_tasks)

            start_url = "https://earn-domain.blum.codes/api/v1/tasks/53044aaf-a51f-4dfc-851a-ae2699a5f729/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = "https://earn-domain.blum.codes/api/v1/tasks/53044aaf-a51f-4dfc-851a-ae2699a5f729/validate"
            payload_answer = {
                "keyword": "HEYBLUM"
            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = "https://earn-domain.blum.codes/api/v1/tasks/53044aaf-a51f-4dfc-851a-ae2699a5f729/claim"

            requests.post(claim_url, headers=headers_tasks)

            start_url = "https://earn-domain.blum.codes/api/v1/tasks/350501e9-4fe4-4612-b899-b2daa11071fb/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = "https://earn-domain.blum.codes/api/v1/tasks/350501e9-4fe4-4612-b899-b2daa11071fb/validate"
            payload_answer = {
                "keyword": "CRYPTOSMART"
            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = "https://earn-domain.blum.codes/api/v1/tasks/b611352b-0d8c-44ec-8e0f-cd71b5922ca5/claim"

            requests.post(claim_url, headers=headers_tasks)

            start_url = "https://earn-domain.blum.codes/api/v1/tasks/b611352b-0d8c-44ec-8e0f-cd71b5922ca5/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = "https://earn-domain.blum.codes/api/v1/tasks/b611352b-0d8c-44ec-8e0f-cd71b5922ca5/validate"
            payload_answer = {
                "keyword": "BLUMERSSS"
            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = "https://earn-domain.blum.codes/api/v1/tasks/92373c2b-2bf3-44c0-90f7-a7fd146c05c5/claim"

            requests.post(claim_url, headers=headers_tasks)

            start_url = "https://earn-domain.blum.codes/api/v1/tasks/92373c2b-2bf3-44c0-90f7-a7fd146c05c5/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = "https://earn-domain.blum.codes/api/v1/tasks/92373c2b-2bf3-44c0-90f7-a7fd146c05c5/validate"
            payload_answer = {
                "keyword": "HAPPYDOGS"
            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = "https://earn-domain.blum.codes/api/v1/tasks/92373c2b-2bf3-44c0-90f7-a7fd146c05c5/claim"

            requests.post(claim_url, headers=headers_tasks)



            original_url = 'https://earn-domain.blum.codes/api/v1/tasks/d2715289-b487-43bc-bc21-18224f8f6bc3'
            start_url = f"{original_url}/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = f"{original_url}/validate"
            payload_answer = {
                "keyword": "NODOXXING"
            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = f"{original_url}/claim"

            requests.post(claim_url, headers=headers_tasks)

            original_url = 'https://earn-domain.blum.codes/api/v1/tasks/1572a605-d714-4f2c-8045-9c5f874d9c7e'
            start_url = f"{original_url}/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = f"{original_url}/validate"
            payload_answer = {
                "keyword": "memeblum"
            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = f"{original_url}/claim"

            original_url = 'https://earn-domain.blum.codes/api/v1/tasks/7067a3db-d9c5-4268-ac19-c393743e8491'
            start_url = f"{original_url}/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = f"{original_url}/validate"
            payload_answer = {
                "keyword": "WOWBLUM"

            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = f"{original_url}/claim"

            requests.post(claim_url, headers=headers_tasks)

            original_url = 'https://earn-domain.blum.codes/api/v1/tasks/30d9f351-614e-4565-a1bb-e7e94fc3dc3c'
            start_url = f"{original_url}/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = f"{original_url}/validate"
            payload_answer = {
                "keyword": "ONFIRE"

            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = f"{original_url}/claim"

            requests.post(claim_url, headers=headers_tasks)









            original_url = 'https://earn-domain.blum.codes/api/v1/tasks/d2a972a1-12ab-4c7b-a411-da056609f2bd'
            start_url = f"{original_url}/start"
            requests.post(start_url, headers=headers_tasks)
            answer_url = f"{original_url}/validate"
            payload_answer = {
                "keyword": "SOBLUM"

            }
            answer_response = requests.post(answer_url, headers=headers_tasks, json=payload_answer)

            claim_url = f"{original_url}/claim"

            requests.post(claim_url, headers=headers_tasks)




            #respon kanggo nggoleki task
            response_tasks = requests.get('https://earn-domain.blum.codes/api/v1/tasks', headers=headers_tasks).json()

            print(f"tasks response : {response_tasks}")
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
                    else:
                        pass
                    try :
                        for b in a['subTasks']:
                            if 'NOT_STARTED' in b['status']:
                                time.sleep(1)
                                print(f"id : {b['id']}")
                                print(f"Iconfilekey : {b['iconFileKey']}")
                                url_start_task = f"https://earn-domain.blum.codes/api/v1/tasks/{b['id']}/start"
                                response_start = requests.post(url_start_task, headers=headers_tasks)
                                url_claim_tasks = f"https://earn-domain.blum.codes/api/v1/tasks/{b['id']}/claim"
                                response_claim = requests.post(url_claim_tasks, headers=headers_tasks)
                            else:
                                pass
                    except KeyError:
                        continue
                data_sub_tasks = i['subSections']
                for abc in data_sub_tasks :
                    try :
                        taskssub = abc['tasks']
                        for cbd in taskssub:
                            if 'NOT_STARTED' in cbd['status']:
                                time.sleep(1)
                                print(f"id : {cbd['id']}")
                                print(f"Iconfilekey : {cbd['iconFileKey']}")
                                url_start_task = f"https://earn-domain.blum.codes/api/v1/tasks/{cbd['id']}/start"
                                response_start = requests.post(url_start_task, headers=headers_tasks)
                                url_claim_tasks = f"https://earn-domain.blum.codes/api/v1/tasks/{cbd['id']}/claim"
                                response_claim = requests.post(url_claim_tasks, headers=headers_tasks)
                            else :
                                pass
                    except KeyError:
                        continue


        # Make the request to play the game
        response_play_game = requests.post(play_game_url, headers=headers_play_game)
        print(response_play_game.text)
        # Check if the request was successful
        if response_play_game.status_code == 200:
            game_response = response_play_game.json()
            game_id = game_response.get("gameId")
            print(f"Game ID: {game_id}")
            time.sleep(random.randint(35, 40))
            random_tap_num = random.randint(160, 240)
            claim_payload = {
                "gameId": game_id,
                "points": random_tap_num
            }

            # Make the request to claim the token
            response_claim_token = requests.post(claim_token_url, headers=headers_claim_token, json=claim_payload)
            print(f"point di dapatkan : {random_tap_num}")
            # Check if the request was successful
            if response_claim_token.status_code == 200:
                claim_response = response_claim_token.text
                print("Token claimed successfully:", claim_response)
                tap_tap_count = tap_tap_count + random_tap_num
            else:
                print("Failed to claim token. Status Code:", response_claim_token.status_code)
                print("Response:", response_claim_token.text)
        # Prepare the payload for the claim token request
        else:
            print('done mas')
            print(f"total poin dari tap tap : {tap_tap_count}")
            print("nunggu claimnya error")
            time.sleep(10)
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

        response_tasks = requests.get('https://game-domain.blum.codes/api/v1/tasks', headers=headers_tasks).json()
        for i in response_tasks:
            data_task = i['tasks']
            for a in data_task:
                print(f"id : {a['id']}")
                print(f"Iconfilekey : {a['iconFileKey']}")

                url_start_task = f"https://game-domain.blum.codes/api/v1/tasks/{a['id']}/start"
                response_start = requests.post(url_start_task, headers=headers_tasks)
                print(response_start.json())

                url_claim_tasks = f"https://game-domain.blum.codes/api/v1/tasks/{a['id']}/claim"
                response_claim = requests.post(url_claim_tasks, headers=headers_tasks)
                print(response_claim.json())
    else:
        None


tap_tap()
