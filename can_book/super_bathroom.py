import json
import time

import requests


# 20205255 e0579afa544ebd4bbdcefa9181ed7247
def login(number: str, password: str) -> (str, str):
    login_data = f"{{\"code\": \"{number}\", \"password\": \"{password}\"}}"

    login_headers = {
        "Host": "ligong.deshineng.com:8082",
        "Content-Length": f"{len(login_data)}",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "http://ligong.deshineng.com:8082",
        "Referer": "http://ligong.deshineng.com:8082/brmclg/login.html?v=12&func=null&sn=null",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }

    login_req = requests.post(f'http://ligong.deshineng.com:8082/brmclg/api/logon/login?time={int(time.time())}',
                              headers=login_headers,
                              data=login_data)

    login_response = login_req.content.decode('utf-8')
    token = json.loads(login_response)['data']['token']
    loginid = json.loads(login_response)['data']['loginid']
    return token, loginid


def bookorder(token: str, loginid: str, bookstatusid: str):
    bookorder_data = "{}"

    bookorder_headers = {
        "Host": "ligong.deshineng.com:8082",
        "Content-Length": f"{len(bookorder_data)}",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "token": f"{token}",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "loginid": f"{loginid}",
        "Content-Type": "application/json",
        "Origin": "http://ligong.deshineng.com:8082",
        "Referer": "http://ligong.deshineng.com:8082/brmclg/html/main.html?v=3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }

    bookorder_req = requests.post(
        f'http://ligong.deshineng.com:8082/brmclg/api/bathRoom/bookOrder?time={int(time.time())}&bookstatusid={bookstatusid}',
        headers=bookorder_headers, data=bookorder_data)

    # print(bookorder_req.content.decode('utf-8'))


def getall_bathroom(token: str, loginid: str) -> list:
    listbook_data = "{}"
    listbook_headers = {
        "Host": "ligong.deshineng.com:8082",
        "Content-Length": f"{len(listbook_data)}",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "token": f"{token}",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "loginid": f"{loginid}",
        "Content-Type": "application/json",
        "Origin": "http://ligong.deshineng.com:8082",
        "Referer": "http://ligong.deshineng.com:8082/brmclg/html/main.html?v=3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }

    listbook_req = requests.post(
        f'http://ligong.deshineng.com:8082/brmclg/api/bathRoom/listBookStatus?time={int(time.time())}&bathroomid=16',
        headers=listbook_headers, data=listbook_data)

    book_list: list = json.loads(listbook_req.content.decode('utf-8'))['data']['bookStatusList']
    return book_list


token, loginid = login('20205255', 'e0579afa544ebd4bbdcefa9181ed7247')
allbathroom = getall_bathroom(token, loginid)
for i in allbathroom:
    remain = int(i['remain'])
    id = i['id']
    period = i['period']
    print(f'ID: {id}, 时间段: {period} 剩余:{remain}')
