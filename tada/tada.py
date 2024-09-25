import requests
import json

def login(query,login_header):
    url = "https://backend.clutchwalletserver.xyz/tada-ton/v1/auth/login"
    payload = {
        'initData' : query
    }
    response = requests.post(url, headers=login_header, json=payload).json()

    print(response)
    bearer_code = "Bearer "+response['accessToken']
    return bearer_code


def task(headers):
    url = "https://backend.clutchwalletserver.xyz/activity/v2/missions?"
    payload = {
        'missionGroupId' : 'eea00000-0000-4000-0000-000000000000',
        'excludeAutoClaimable' : 'true'
    }
    response = requests.get(url, headers=headers, json=payload).json()
    print(response)
    for i in response:
        activity = i['activityTypes']
        id = i['id']
        if activity == None:
            pass
        else :
            task_url = f"https://backend.clutchwalletserver.xyz/activity/v3/activities/{activity}"
            task_response = requests.post(task_url,headers=headers).json()
            print(task_response)
            claim_url = f"https://backend.clutchwalletserver.xyz/activity/v2/missions/{id}/claim"
            claim_response = requests.post(claim_url,headers=headers).json()
            print(claim_response)




login_headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en',
    'content-length': '342',
    'content-type': 'application/json',
    'origin': 'https://tada-mini.mvlchain.io',
    'priority': 'u=1, i',
    'referer': 'https://tada-mini.mvlchain.io/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-auth-client-id': 'TadaTonMiniApp',
    'x-auth-client-version': '1'
}


query = input("masukkan query ==>> ")
bearer = login(query, login_header=login_headers)


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en',
    'authorization': bearer,
    'content-length': '0',
    'origin': 'https://tada-mini.mvlchain.io',
    'priority': 'u=1, i',
    'referer': 'https://tada-mini.mvlchain.io/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-auth-client-id': 'TadaTonMiniApp',
    'x-auth-client-version': '1'
}
print(bearer)

task(headers)
