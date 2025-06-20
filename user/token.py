import pandas as pd
import requests
def talaba_user_token(username, password):

    login_endpoint = "https://student.kokandsu.uz/rest/v1/auth/login"

    # payload = {
    # "login": '356241101810',
    # "password": "Marjona2006"
    # }
    payload = {
    "login": f"{username}",
    "password": f"{password}"
    }
    req = requests.post(login_endpoint, data=payload)
    data = req.json()
    user_token = data["data"]["token"]

    return user_token
    
def talaba_malumot(username, password):
    user_token = talaba_user_token(username, password)
    retrieve_user_info_endpoint = "https://student.kokandsu.uz/rest/v1/account/me"
    headers = {
        "Authorization": f"Bearer {user_token}"
    }
    req = requests.get(retrieve_user_info_endpoint, headers=headers)
    df = req.json()['data']
    return df
    
def talaba_gpa(username, password):
    user_token = talaba_user_token(username, password)
    retrieve_user_info_endpoint = "https://student.kokandsu.uz/rest/v1/data/student-gpa-list"
    headers = {
        "Authorization": f"Bearer {user_token}"
    }
    req = requests.get(retrieve_user_info_endpoint, headers=headers)
    df = req.json()['data']
    if df:
        qiymat = df
    else:
        qiymat = 0
    return qiymat
    