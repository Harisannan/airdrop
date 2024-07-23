import os
import time
import random

def input_url():
    while True:
        user_input = input("Masukkan URL (atau ketik 'stop' untuk berhenti): ")
        if 'stop' in user_input:
            print('stopped')
            break
        elif '    ' in user_input:
            print(''''
            
            1. buat komentar
            2. buat quote tweet
            
            ''')
            opsi1 = input('masukkan pilihanmu')
            if opsi1 == '1':
                user_input = input('masukkan url(hanya post twitter/x)')
                try:
                    base_url, status_part = user_input.split("/status/")
                    modified_url = f"https://x.com/intent/tweet?in_reply_to={status_part}&text="
                    os.system('clear')
                    os.system('cls')
                    tambahan = input('ada tambahan? [y/n] >>> ')
                    if tambahan == 'y':
                        while True :
                            list_name_data = ["api_id", "api_hash", "phone_number", "telegram_username", "twitter_username", "twitter_link",
                              "medium_username", "medium_link", "reddit_username", "reddit_link", "facebook_username",
                              "facebook_link", "instagram_usernane", "instagram_link", "email", "bsc_wallet", "sol_wallet",
                              "tron_wallet", "youtube_username", "youtube_link", "id", "discord"]
                            n_data = 0
                            for i in list_name_data :
                                print(f'{n_data}. {i}')
                                n_data = n_data+1
                            print('[99] tamabahan custom')
                            print('[D] done')
                            print('[C] clear all')
                            append_option = input('masukkan pilihan >>>')
                            if append_option == '99':
                                modified_url = f'{modified_url}{input('masukkan tambahan >>> ')}%20'
                            elif append_option == 'D':
                                break
                            elif append_option == 'C':
                                modified_url = f"https://x.com/intent/tweet?in_reply_to={status_part}&text="
                            else:
                                modified_url = f'{modified_url}{list_name_data[int(append_option)]}%20'
                    else:
                        os.system('clear')
                        os.system('cls')
                    print('''
                    1. comment + tag 3
                    2. comment + tag 5
                    3. tag3
                    4. tag5
                    ''')

                    opsi2 = input('masukkan pilihan >>> ')
                    if opsi2 == '1':
                        modified_url = modified_url+'commenttag3'
                    elif opsi2 == '2':
                        modified_url = modified_url+'commenttag5'
                    elif opsi2 == '3':
                        modified_url = modified_url+'tagthree'
                    elif opsi2 == '4':
                        modified_url = modified_url+'tagfive'
                    else :
                        None

                except ValueError:
                    print("URL tidak valid untuk modifikasi.")
                with open('url.txt', 'a') as write_data:
                    write_data.write(modified_url+'\n')
                    write_data.close()

            elif opsi1 == '2':
                user_input = input('masukkan url(hanya post twitter/x)')
                try:
                    modified_url = f"https://twitter.com/intent/tweet?url={user_input}&text="
                    os.system('clear')
                    os.system('cls')
                    tambahan = input('ada tambahan? [y/n] >>> ')
                    if tambahan == 'y':
                        while True :
                            list_name_data = ["api_id", "api_hash", "phone_number", "telegram_username", "twitter_username", "twitter_link",
                              "medium_username", "medium_link", "reddit_username", "reddit_link", "facebook_username",
                              "facebook_link", "instagram_usernane", "instagram_link", "email", "bsc_wallet", "sol_wallet",
                              "tron_wallet", "youtube_username", "youtube_link", "id", "discord", "cmc"]
                            n_data = 0
                            for i in list_name_data :
                                print(f'{n_data}. {i}')
                                n_data = n_data+1
                            print('[99] tamabahan custom')
                            print('[D] done')
                            print('[C] clear all')
                            append_option = input('masukkan pilihan >>>')
                            if append_option == '99':
                                modified_url = f'{modified_url}{input('masukkan tambahan')}%20'
                            elif append_option == 'D':
                                break
                            elif append_option == 'C':
                                modified_url = f"https://x.com/intent/tweet?in_reply_to={status_part}&text="
                            else:
                                modified_url = f'{modified_url}{list_name_data[int(append_option)]}%20'
                    else:
                        os.system('clear')
                        os.system('cls')
                    print('''
                    1. quote + tag 3
                    2. quote + tag 5
                    3. tag3
                    4. tag5
                    ''')

                    opsi2 = input('masukkan pilihan >>> ')
                    if opsi2 == '1':
                        modified_url = modified_url+'quotetag3'
                    elif opsi2 == '2':
                        modified_url = modified_url+'quotetag5'
                    elif opsi2 == '3':
                        modified_url = modified_url+'tag3'
                    elif opsi2 == '4':
                        modified_url = modified_url+'tag5'
                    else :
                        None

                except ValueError:
                    print("URL tidak valid untuk modifikasi.")
                with open('url.txt', 'a') as write_data:
                    write_data.write(modified_url+'\n')
                    write_data.close()

            else:
                print('ynkts')
        else:
            with open('url.txt','a') as write_data:
                write_data.write(user_input+'\n')
                write_data.close()

def open_url():
    qt = ["Are you looking for a project with great potential? take a look below ", "what's this? click now..!!! ",
          "let's get early access before listing in a big market, beware of missing out ",
          "wooah there are many interesting events here, invest your capital and see in the future ",
          "big project for smart people, that's how it is ", "watch out you miss the train!!!, tut tut... ",
          "no harm in trying this project"]
    comment = ["This project is truly innovative and has immense potential ",
               "I'm impressed by the vision and dedication behind this crypto project ",
               "Kudos to the team for creating such a promising venture ",
               "The immersive nature of this project sets it apart from others in the crypto space ",
               "A truly good project that deserves attention and recognition ",
               "I can see the bright future ahead for this project ",
               "Thanks for the opportunity to be part of this exciting journey ",
               "The team's commitment to success is evident in every aspect of the project ",
               "This is more than just a project; it's a game-changer in the crypto world ",
               "I believe in the potential of this project to make a significant impact ",
               "Nice project! Looking forward to witnessing its growth and success ",
               "The thoughtfulness and detail put into this project are commendable ",
               "I'm grateful to be involved in such a promising venture ",
               "This project has all the elements of success – innovation, vision, and a dedicated team ",
               "Good things come to those who invest wisely, and this project is a testament to that ",
               "Thanks to the project team for making this airdrop opportunity possible ",
               "I'm excited to see how this project will shape the future of crypto ",
               "Wishing the project team continued success on this impressive journey ",
               "The potential for growth in this project is truly remarkable ",
               "A big thumbs up to the team for their hard work and dedication ",
               "It's projects like these that bring positive change to the crypto space ",
               "Count me in as a supporter of this fantastic initiative ",
               "This project has all the makings of a successful venture – keep it up! ",
               "I'm confident that this project will be a major player in the crypto industry ",
               "Thanks for the opportunity to participate in the airdrop – excited for what's to come! ",
               "This project embodies innovation and excellence in the crypto world ",
               "I'm looking forward to witnessing the milestones this project will achieve ",
               "Congratulations to the team for creating something truly extraordinary ",
               "The potential for success in this project is sky-high ",
               "Wishing the project team continued growth and prosperity ",
               "This is more than just a project; it's a revolution in the making ",
               "I appreciate the transparency and openness of the project team ",
               "The team's commitment to community engagement is admirable ",
               "I'm honored to be part of this journey with such a forward-thinking project ",
               "The future looks bright with this project leading the way ",
               "A great project that deserves all the positive recognition it can get ",
               "Thanks for creating an opportunity for the community to be involved – much appreciated! ",
               "The potential impact of this project on the crypto landscape is truly exciting ",
               "This project is a testament to the endless possibilities within the crypto space ",
               "I'm eager to see how this project will disrupt and innovate in the industry ",
               "The team's dedication to excellence shines through in every aspect of the project ",
               "Kudos to the team for bringing such a visionary project to life ",
               "The community support for this project is a reflection of its strong foundation ",
               "Exciting times ahead for everyone involved in this project ",
               "This project has the right mix of innovation and execution – a recipe for success ",
               "I believe in the potential of this project to leave a lasting impact ",
               "Thanks to the project team for their hard work and commitment to success ",
               "The immersive experience offered by this project is truly remarkable ",
               "This project stands out as a beacon of excellence in the crypto space ",
               "Count me among the believers in the success of this project ",
               "I'm grateful to be part of a community that supports such a promising project"]
    random.shuffle(qt)
    random.shuffle(comment)
    list_name_data = ["api_id", "api_hash", "phone_number", "telegram_username", "twitter_username", "twitter_link",
                      "medium_username", "medium_link", "reddit_username", "reddit_link", "facebook_username",
                      "facebook_link", "instagram_usernane", "instagram_link", "email", "bsc_wallet", "sol_wallet",
                      "tron_wallet", "youtube_username", "youtube_link", "id", "discord", "cmc"]
    url_file = open('url.txt', 'r+').read()
    log_akun = open('akun/account.txt', 'r+').read()
    urls = url_file.split('\n')
    account_data = log_akun.split('\n')
    modified_url = ''
    for akun in account_data:
        for url in urls:
            number_for = 0
            for data in list_name_data:
                if data in url:
                    real_data = akun.split(',')
                    # print(real_data[number_for])
                    # print(number_for)
                    modified_url = url.replace(data,real_data[number_for])
                number_for = number_for+1
    print(modified_url)






while True:
    print('''
    
        1.masukkan url
        2.open url
        3.delete semua link tersimpan
        4.exit
    
    ''')
    pilihan = input(">>> ")


    if pilihan == '1':
        input_url()
    elif pilihan == '2':
        open_url()
    elif pilihan == '3':
        f = open('url.txt','w')
        f.close()
        print('sukses menghapus')
        continue
    elif pilihan == '4':
        exit()
    else :
        print('pilihan tidak di temukan')
        time.sleep(1)
