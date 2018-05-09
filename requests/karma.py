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
    'x-access-token': str(token),
    'x-key': str(key),
    'x-org': '37',
    }


sleep(5)
print get_karma_point(headers)
sleep(5)
print create_comment(headers)
sleep(5)
print tag_user(headers)
