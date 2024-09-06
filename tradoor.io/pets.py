import requests
import os

url = "https://tradoor.io/points/api/v1/task/bull/pets"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": input('masukkan bearer ==>> '),
    "Cookie": input("masukkan cookie ==>> "),
    "Priority": "u=1, i",
    "Referer": "https://tradoor.io/rewards",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}




data = {
    'pets': 5000
}  # Your JSON payload here

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.json())