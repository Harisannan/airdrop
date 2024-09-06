import requests
import os
import random
import time
import socket
from colorama import init, Fore, Back
from datetime import datetime

init(autoreset=True)
pencekal = input("aktifkan mode pencekalan [y/n] => ")
path = "/sdcard/python/ponzi/akun/account_log.txt"
f = open(path, 'r+')
ff = f.read()
f_split = ff.split("\n")
n = 0
elig_check = input("mau check wd atau ndak?? \n\n[y/n]  =>  ")
sekarang = datetime.now()
tanggal_format = sekarang.strftime("%Y-%m-%d")



def generate_short_indonesian_name(words_count):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    prefixes = ['Mu', 'Bu', 'Wati', 'Sri', 'Budi', 'Tri']
    suffixes = ['wan', 'anto', 'ati', 'yah', 'sari', 'wan']

    def generate_word(use_prefix=False, use_suffix=False):
        word = ''
        if use_prefix:
            word += random.choice(prefixes)
        length = random.randint(3, 5)  # Panjang kata antara 3 dan 5 karakter
        for i in range(length):
            if i % 2 == 0:  # Huruf non vokal
                word += random.choice(consonants)
            else:  # Huruf vokal
                word += random.choice(vowels)
        if use_suffix:
            word += random.choice(suffixes)
        return word.capitalize()

    names = []
    for i in range(words_count):
        use_prefix = (i == 0)  # Gunakan awalan hanya untuk kata pertama
        use_suffix = (i == words_count - 1)  # Gunakan akhiran hanya untuk kata terakhir
        names.append(generate_word(use_prefix, use_suffix))

    return ' '.join(names)


os.system("clear")
for i in f_split:
    if "https://blk58.com" in i:
        def check_internet_connection():
            while True:
                try:
                    # Coba buat koneksi ke server DNS (dalam hal ini, Google DNS)
                    socket.create_connection(("8.8.8.8", 53), timeout=5)
                    print("Koneksi internet aktif.")
                    break
                except OSError:
                    None


        os.system(
            "su -c 'settings put global airplane_mode_on 1 && am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true'")
        time.sleep(4)
        os.system(
            "su -c 'settings put global airplane_mode_on 0 && am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false'")


        check_internet_connection()


        # Panggil fungsi untuk mengecek koneksi

        user_agent = f_split[n + 1]
        phone_number = f_split[n + 2]
        sandi = f_split[n + 3]


        unix = time.time()
        image_url = f'https://blk58.com/api/Account/code?code_rand={unix}'

        # Mengirim permintaan GET untuk mendapatkan gambar
        response_image = requests.get(image_url)

        # Memastikan respons sukses (status code 200)
        if response_image.status_code == 200:
            # Menyimpan gambar biner ke dalam file gambar di folder /sdcard
            image_path = '/sdcard/gambar.jpg'
            with open(image_path, 'wb') as file:
                file.write(response_image.content)
            print(f'Gambar disimpan di {image_path}')

        registration_url = 'https://blk58.com/api/user/Register'

        payload_registration = {
            'dest': '',
            'username': phone_number,
            'password': sandi,
            're_password': sandi,
            'smscode': '',
            'code': input("masukkan kode >>> "),
            'code_rand': f'{unix}',
            'recommend': i.split("register/")[1],
            'lang': 'id'
        }

        headers_registration = {
            'User-Agent': user_agent,
        }
        print(phone_number)
        # Mengirim permintaan POST untuk registrasi
        response_registration = requests.post(registration_url, data=payload_registration, headers=headers_registration)
        print('Status Registrasi:', response_registration.status_code)
        print('Respon Registrasi:', response_registration.text)

        if f"Verification code error" in response_registration.text:
            continue
        elif 'Recommend code error' in response_registration.text:
            with open("/sdcard/python/ponzi/akun/account_log.txt", 'r+').read() as read:
                replac = read.replace(phone_number, "")
                replaca = replac.replace(sandi, "")
                replaci = replaca.replace(user_agent, "")
                remover = open("/sdcard/python/ponzi/akun/account_log.txt", 'w')
                remover.write(replaci)
                remover.close()
                read.cole()
        else:
            None
        print(f"user-agent : {user_agent}\n\nphone number : {phone_number}\n\nkata_sandi : {sandi}\n\n")
        if phone_number == "":
            None
        else:

            check_internet_connection()


            # Fungsi untuk mendapatkan token dari response sebelumnya
            def get_token(response_text):
                return response_text['info']['token']


            # Fungsi untuk mengumpulkan task_id dari response_task_list
            def get_task_ids(response_text):
                return [task['task_id'] for task in response_text['info']]


            # URL dan headers
            url_login = "https://blk58.com/api/User/Login"
            url_task_list = "https://blk58.com/api/task/getTaskList"
            url_receive_task = "https://blk58.com/api/task/receiveTask"
            url_task_order_list = "https://blk58.com/api/task/taskOrderlist"
            url_bank_card_info = "https://blk58.com/api/Account/getBankCardList"
            url_add_bank = "https://blk58.com/api/Account/AddBankCard"
            url_set_password = "https://blk58.com/api/user/setuserinfo"
            url_withdraw = "https://blk58.com/api/Transaction/draw"
            url_cek_experied = "https://blk58.com/api/user/getUserInfo"
            headers = {
                'User-Agent': user_agent
            }

            # Payload untuk login
            payload_login = {
                'username': phone_number,
                'password': sandi,
                'lang': 'id',
            }


            # Permintaan login
            response_login = requests.post(url_login, headers=headers, data=payload_login).json()

            # Mendapatkan token dari response login
            try:
                token = get_token(response_login)
                print("\nip : " + response_login['info']['ip'] + "\n")

                if elig_check == 'y':
                    payload_bank_info = {
                        'lang': 'id',
                        'token': token,
                    }
                    response_bank_info = requests.post(url_bank_card_info, headers=headers,
                                                       data=payload_bank_info).json()

                    payload_set_realname = {
                        'realname': generate_short_indonesian_name(2),
                        'lang': 'id',
                        'token': token
                    }
                    response_set_realname = requests.post('https://blk58.com/api/user/setuserinfo', headers=headers,
                                                          data=payload_set_realname).json()
                    payload_set_password = {
                        'n_payword': '111111',
                        'r_payword': '111111',
                        'lang': 'id',
                        'token': token
                    }
                    response_set_password = requests.post(url_set_password, headers=headers,
                                                          data=payload_set_password).json()
                    print(response_set_password['code_dec'])

                    payload_withdraw = {
                        'draw_type': 'bank',
                        'user_bank_id': '7473',
                        'draw_money': 33000,
                        'ifsc': '',
                        'drawword': 111111,
                        'bank_id': '7473',
                        'pix_value': phone_number,
                        'extend': {"pix_type": "CPF", "pix_value": phone_number, "account_type": ""},
                        'lang': 'id',
                        'token': token
                    }
                    response_withdraw = requests.post(url_withdraw, headers=headers, data=payload_withdraw).json()
                    print(f"withdraw status : {Fore.LIGHTGREEN_EX}{response_withdraw['code_dec']}\n")
                    print(f"{Back.GREEN}status progress :						   ")
                    if "Silakan hubungi manajer perekrutan" in response_withdraw['code_dec']:
                        p = ff.replace(f"{i}\n{user_agent}\n{phone_number}\n{sandi}", "\n\n\n")
                        clear_failed_account = open(path, 'w')
                        clear_failed_account.write(p)
                        clear_failed_account.close()
                    else:
                        # Payload untuk mendapatkan daftar tugas
                        payload_task_list = {
                            "token": token,
                            "status": 1,
                            "is_u": 2,
                            "page_no": 1,
                            "lang": "id",
                        }

                        # Permintaan untuk mendapatkan daftar tugas
                        response_task_list = requests.post(url_task_list, headers=headers,
                                                           data=payload_task_list).json()

                        # Mendapatkan task_id dari response_task_list
                        task_ids = get_task_ids(response_task_list)

                        # Melakukan perulangan untuk mengirim permintaan ke receiveTask
                        for task_id in task_ids:
                            payload_receive_task = {
                                'id': task_id,
                                'token': token,
                                'lang': 'id',
                            }

                            # Permintaan untuk menerima tugas
                            response_receive_task = requests.post(url_receive_task, headers=headers,
                                                                  data=payload_receive_task).json()

                            print(f"mengambil tugas dengan id => {task_id}")

                        # Mengecek apakah kata "kesuksesan" terdapat dalam response_receive_task

                        # Payload untuk mendapatkan daftar pesanan tugas
                        payload_task_order_list = {
                            'status': 1,
                            'page_no': 1,
                            'is_u': 2,
                            'lang': 'id',
                            'token': token,
                        }

                        # Permintaan untuk mendapatkan daftar pesanan tugas
                        response_task_order_list = requests.post(url_task_order_list, headers=headers,
                                                                 data=payload_task_order_list).json()

                        payload_cek_experied = {
                            'lang': 'id',
                            'token': token

                        }
                        response_url_cek_experied = requests.post(url_cek_experied, headers=headers,
                                                                  data=payload_cek_experied).json()
                        # Mendapatkan daftar order_id dari response_task_order_list
                        print(f"{Fore.LIGHTRED_EX}BALANCE : {response_url_cek_experied['info']['balance']}")
                        # Mendapatkan daftar order_id dari response_task_order_list
                        if 10 + 5 == 15:
                            try:
                                order_ids = [order['order_id'] for order in response_task_order_list['info']]

                                # ...

                                # Variabel untuk URL taskOrderSubmit
                                url_task_order_submit = "https://blk58.com/api/task/taskOrderSubmit"
                                image_for_upload = ["/upload/image/20240103/71c9d90ca32a795ab1f4d42b0fcddfde.jpg",
                                                    "/upload/image/20240103/e08098b6a4ab316f90386f2ed9f95941.jpg",
                                                    "/upload/image/20240103/c74b6d380577f5f018520e5bea3f5af4.jpg",
                                                    "/upload/image/20240103/91893922d73d0cd2a21b825b5c6914be.jpg",
                                                    "/upload/image/20240103/fecabccfa13428a79e0d563c8ea7b669.jpg",
                                                    "/upload/image/20240103/61863c523ae33139064e728365bdf01f.jpg",
                                                    "/upload/image/20240103/821e2a3277deff9b4e2271475cf6cbdc.jpg",
                                                    "/upload/image/20240103/9a7f4a03ddb01fdd63bfc1ff9cfef862.jpg",
                                                    "/upload/image/20240103/8ee51a2d69a09f323a93a7095956a7b2.jpg",
                                                    "/upload/image/20240103/b7a23ac0acfcbfcd3d6ed4ed72616aa7.jpg",
                                                    "/upload/image/20240103/e7b8d2ac50d37d19bd334dbdcba0923c.jpg",
                                                    "/upload/image/20240103/f5e1848b2ca2e1b90a016c2b17a87d12.jpg"]
                                # Melakukan perulangan untuk mengirim permintaan ke taskOrderSubmit
                                for order_id in order_ids:
                                    payload_task_order_submit = {
                                        'order_id': order_id,
                                        'examine_demo': '',
                                        'lang': 'id',
                                        'token': token,
                                    }

                                    # Permintaan untuk submit order
                                    response_task_order_submit = requests.post(url_task_order_submit, headers=headers,
                                                                               data=payload_task_order_submit).json()
                                    print(
                                        f"mengerjakan tugas dengan id => {order_id} : response : {response_task_order_submit}")
                                    image_for_upload = ["/upload/image/20240103/71c9d90ca32a795ab1f4d42b0fcddfde.jpg",
                                                        "/upload/image/20240103/e08098b6a4ab316f90386f2ed9f95941.jpg",
                                                        "/upload/image/20240103/c74b6d380577f5f018520e5bea3f5af4.jpg",
                                                        "/upload/image/20240103/91893922d73d0cd2a21b825b5c6914be.jpg",
                                                        "/upload/image/20240103/fecabccfa13428a79e0d563c8ea7b669.jpg",
                                                        "/upload/image/20240103/61863c523ae33139064e728365bdf01f.jpg",
                                                        "/upload/image/20240103/821e2a3277deff9b4e2271475cf6cbdc.jpg",
                                                        "/upload/image/20240103/9a7f4a03ddb01fdd63bfc1ff9cfef862.jpg",
                                                        "/upload/image/20240103/8ee51a2d69a09f323a93a7095956a7b2.jpg",
                                                        "/upload/image/20240103/b7a23ac0acfcbfcd3d6ed4ed72616aa7.jpg",
                                                        "/upload/image/2024010response_task_order_submit}"]
                            except KeyError:
                                print("all task done")
                    if pencekal == "n":
                        print("gaspoll!!!")
                    else:
                        input("enter")
            except KeyError:
                p = ff.replace(f"{i}\n{user_agent}\n{phone_number}\n{sandi}", "\n\n\n")
                clear_failed_account = open(path, 'w')
                clear_failed_account.write(p)
                clear_failed_account.close()
        f.close()
        f = open(path, 'r+')
        ff = f.read()
        f_split = ff.split("\n")
    n = n + 1
input("enter untuk exit")
while True:
    fraed = open("/sdcard/python/ponzi/akun/account_log.txt", "r+")
    fread = fraed.read()
    if "\n\n\n" in fread:
        replacer = fread.replace("\n\n\n", "\n\n")
        fwrite = open("/sdcard/python/ponzi/akun/account_log.txt", "w")
        fwrite.write(replacer)
        fwrite.close()

    else:
        print("rapi mas")
        break

    fraed.close()