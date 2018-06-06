import os
import requests
import json
from time import sleep
from sys import argv

def login():
    api = 'https://teamchumbak.qilo.co:7011/login'
    headers = {'Content-type': 'application/json'}
    cred = {'username': argv[1],
            'password': argv[2],
            "orgId":37,
            # "loginSource":"'EMPLOYEE','HR_ADMIN','LEADERSHIP'"
            }
    data = json.dumps(cred)
    r = requests.post(api, data=data, headers=headers)
    token = r.json().get('token')
    key = json.loads(r.json().get('user'))[0]['user_id']

    return token, key


def get_karma_point(headers):
    api = 'https://talkatchumbak.qilo.co:7010/api/v1/employee/getToalKarmaByUserId'
    d = {'user_id': key}
    data = json.dumps(d)
    r = requests.post(api, data=data, headers=headers)
    karma_point = r.json().get("karma_point")
    return "Your Karma Point: {}".format(karma_point)

# print get_karma_point(h)

def create_comment(headers):
    api = 'https://talkatchumbak.qilo.co:7010/api/v1/employee/doNewPostComment'
    d = {
        "org_id":37,
        "post_id":29739,
        "comment_text":"test1",
        "created_by":key,
        "updated_by":key,
        "user_img_url":"https://qiloee.s3-ap-southeast-1.amazonaws.com/37/personal/37_15848_image.png",
        "user_id":key,
        "user_name":"anonymous user",
        "user_email":argv[1],
        "comment_tagged":0
        }
    data = json.dumps(d)
    r = requests.post(api, data=data, headers=headers)
    return r.json()

def tag_user(headers):
    api = 'https://talkatchumbak.qilo.co:7010/api/v1/employee/tagUserToPost'
    d = {
        "org_id":37,
        "post_id":29739,
        "post_type":"SOCIAL",
        "post_for":"COMMENT",
        "by_name":"anonymous user",
        "atTherate_info":[]
        }
    data = json.dumps(d)
    r = requests.post(api, data=data, headers=headers)
    return r.json()

token, key = login()

headers = {
    'Content-type': 'application/json',
    'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MzE3MjcyMDIyNDR9.ugRqgm3Xnd5jjqqad8HwcP6yLi8Wkg2fR3fpUQJCTvk',
    'x-key': '15848',
    'x-org': '37',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Referer': 'https://talkatchumbak.qilo.co/',
    'Origin': 'https://talkatchumbak.qilo.co',
    'Host': 'talkatchumbak.qilo.co:7010',
    'Cookie': 'uuid=%22licat29t1a1526990803295%22; userImgUrl=%22https%3A%2F%2Fqiloee.s3-ap-southeast-1.amazonaws.com%2F37%2Fpersonal%2F37_15801_image.png%22; qliqueSess=eyJvcmdNZXRhZGF0YSI6eyJPUkdfUkVQTFlfRU1BSUwiOiJhamF5QGNodW1iYWsuaW4iLCJPUkdfSFJfRU1BSUxfSUQiOiJhamF5QGNodW1iYWsuaW4iLCJPUkdfRU1BSUxfRlJPTV9OQU1FIjoiVGVhbSBDaHVtYmFrICIsIk9SR19OQU1FIjoiVGVhbSBDaHVtYmFrIiwiT1JHX09SSUdJTkFMX05BTUUiOiJDaHVtYmFrIiwiQ0xJRU5UU0lERV9CQVNFX1VSTCI6Imh0dHBzOi8vdGFsa2F0Y2h1bWJhay5xaWxvLmNvIiwiU0VSVkVSU0lERV9CQVNFX1VSTCI6Imh0dHBzOi8vdGFsa2F0Y2h1bWJhay5xaWxvLmNvOjcwMTAiLCJHT0FMX0NMSUVOVFNJREVfQkFTRV9VUkwiOiJodHRwczovL3RlYW1jaHVtYmFrLnFpbG8uY28iLCJHT0FMX1NFUlZFUlNJREVfQkFTRV9VUkwiOiJodHRwczovL3RlYW1jaHVtYmFrLnFpbG8uY286NzAxMSIsIk9SR19DT1JQX1NPRlRfTkFNRSI6IkNvbm5lY3Qgd2l0aCBDaHVtYmFrIiwiT1JHX1NPQ0lBTF9TT0ZUX05BTUUiOiJLbm93bGVkZ2UgU2hhcmUiLCJDTElFTlRTSURFX1NVUlZFWV9VUkwiOiJodHRwczovL3lvdXJ2b2ljZWF0Y2h1bWJhay5xaWxvLmNvIiwiU0VSVkVSU0lERV9TVVJWRVlfVVJMIjoiaHR0cHM6Ly95b3Vydm9pY2VhdGNodW1iYWsucWlsby5jbzo3MDEwIiwiU0VSVkVSU0lERV9EQVNIQk9BUkRfVVJMIjoiaHR0cHM6Ly9kYXNoYm9hcmRjaHVtYmFrLnFpbG8uY286NzAxMCIsIkNMSUVOVFNJREVfREFTSEJPQVJEX1VSTCI6Imh0dHBzOi8vZGFzaGJvYXJkY2h1bWJhay5xaWxvLmNvIiwiSVNfU0VORE1BSUxfT05fU09DSUFMIjoiTiJ9fQ==; qliqueSess.sig=RzpxziSlNWqNu-4HZBYtateB9tA'
    }


def like_comment(headers):
    api = 'https://talkatchumbak.qilo.co:7010/api/v1/employee/doLikeForPostComment'
    d = {
        "post_id":29698,
        "created_by":15848,
        "updated_by":15848,
        "comment_id":25785,
        }
    data = json.dumps(d)
    r = requests.post(api, data=data, headers=headers)
    return r.json()

sleep(5)
print like_comment(headers)
# print get_karma_point(headers)
# sleep(5)
# print create_comment(headers)
# sleep(5)
# print tag_user(headers)
