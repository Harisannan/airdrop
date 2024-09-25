import requests
import time





def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


def keep_alive():
    url_get_point = 'https://www.aeropres.in/api/atom/v1/userreferral/getpoint?appid=66eef700a8811d119f44304d'
    url_keep_alive = 'https://www.aeropres.in/chromeapi/dawn/v1/userreward/keepalive'

    payload = {"username":"harisannanda01@gmail.com","extensionid":"fpdkjdnhkakefebpekbdhillbhonfjjp","numberoftabs":0,"_v":"1.0.9"}



    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'Authorization': 'Berear 2056b72d0eb33beb2a6d2d39c67296afa677fc1f271efaf0d84b5d50cd08aee410c07f2f8a6510b58ab067551517964a9b712a207a15ea4f311b2b0364b0fd4bb30cc4bd27c4a2f1bd2964411b774e86428ab78ff4ba4a8533250451638628b6fe3b728586bdfb8b2e1761440b1493f92519a18994611fe0d8d7a0cfebeb6db6ef3212703a03115424026909bb7479237864e5f8834dd1e57b7864fe2359df0ee85d3250849ecb52846bd03be886004e2f10eaf837bb96f9facbd81eca6b90226307fae2c2079ed3b0f0bde22bb41ee66cd4eb592b36c7b732ce6ab331237dafcd0b7c20b40b115204fccb8047f62f2018ec3c63108fe11e20230897c1956a36',
        'content-length': '118',
        'content-type': 'application/json',
        'Origin': 'chrome-extension://fpdkjdnhkakefebpekbdhillbhonfjjp',
        'priority': 'u=1, i',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }


    session = requests.Session()


    response_keep_alive = session.post(url_keep_alive, headers=headers, json=payload, verify=False)
    if 'message' in response_keep_alive.text :
        interval = 30
    else :
        interval = 0

    return interval

while True:
    next_time = keep_alive()

    countdown(next_time)