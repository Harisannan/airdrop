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
                response_start = requests.post(url_start_task,headers=headers_tasks)
                print(response_start.json())



                url_claim_tasks = f"https://game-domain.blum.codes/api/v1/tasks/{a['id']}/claim"
                response_claim = requests.post(url_claim_tasks, headers=headers_tasks)
                print(response_claim.json())
    else :
        None

tap_tap()