import os
import requests
import json
import string
import csv
from random import choice
from time import sleep

from skip_emails import skip_email_list

def home(host, api_key, headers):
    home_api = host
    r = requests.get(home_api, headers=headers)
    print "Home-Api-Response: %s" %(r.status_code)

def list_projects(host, api_key, headers):
    list_project_api = host + "projects.json"
    r = requests.get(list_project_api, headers=headers)
    print "List-Project-Api-Response: %s" %(r.status_code)

def get_random_project(host, api_key, headers):
    list_project_api = host + "projects.json"
    r = requests.get(list_project_api, headers=headers).json()

    projects = r.get("projects")
    random_project = choice(projects)
    pid = random_project.get("id")
    random_project_api = host + "projects/{}.json".format(pid)
    response = requests.get(random_project_api, headers=headers)
    print "Get-Project-Api-Status: %s" %(response.status_code)

def create_project(host, api_key, headers):
    create_project_api = host + "projects.json"
    project_name = 'PyRequestLib-' + ''.join(choice(string.ascii_letters + string.digits) for i in range(5))
    project_identifier = ''.join(choice(string.ascii_lowercase) for i in range(3))

    project = {"name":project_name, "identifier":project_identifier}
    data = json.dumps({"project": project})
    response = requests.post(create_project_api, data=data, headers=headers)
    print "Create-project-Api-Response %s" %(response.status_code)

def delete_projects(host, api_key, headers):
    projects_api = host + "projects.json"
    response = requests.get(projects_api, headers=headers).json()
    projects = response.get("projects")

    for project in projects:
        pid = project.get("id")
        print "I am here %s" %(pid)
        delete_project_api = host + "projects/{}.json".format(pid)
        response = requests.delete(delete_project_api, headers=headers)
        print "Project: %s, Delete-Api-Status: %s" %(pid, response.status_code)


def list_issues(host, api_key, headers):
    list_issues_api = host + "issues.json"
    response = requests.get(list_issues_api, headers=headers)
    print "List-Issues-Api-Status: %s" %(response.status_code)

def get_random_issue(host, api_key, headers):
    get_random_issue_api = host + "issues.json"
    response = requests.get(get_random_issue_api, headers=headers).json()
    issues = response.get("issues")
    if issues:
        random_issue = choice(issues)
        issue_id = random_issue.get("id")
        api = host + "issues/{}.json".format(issue_id)
        response = requests.get(api, headers=headers)
        print "Get-Issue-Api-Status: %s" %(response.status_code)
    else:
        print "No Issue found"

def create_issue(host, api_key, headers):
    upload_header = {'X-Redmine-API-Key': api_key, 'Content-Type': 'application/octet-stream'}

    # upload file
    content = open("file.txt", "rw").read()
    upload_api = host + "uploads.json"
    response = requests.post(upload_api, data=content, headers=upload_header).json()
    token = response.get("upload").get("token")
    upload = {"token":token, "filename":"file.txt"}

    # get pid
    projects_api = host + "projects.json"
    response = requests.get(projects_api, headers=headers).json()
    projects = response.get("projects")
    random_project = choice(projects)
    pid = random_project.get("id")

    # create issue body
    subject = 'Issue-' + ''.join(choice(string.ascii_letters + string.digits) for i in range(5))
    description = 'Description-Via-Py-' + ''.join(choice(string.digits) for i in range(3))

    issue = {"project_id": pid,
            "subject": subject,
            "description": description,
            "uploads": [upload],
            "assigned_to_id": 1}

    data = json.dumps({"issue": issue})
    issues_api = host + "issues.json"
    response = requests.post(issues_api, data=data, headers=headers)
    print "Create-Issue-Api-Status: %s" %(response.status_code)

def delete_issues(host, api_key, headers):
    issues_api = host + "issues.json"
    response = requests.get(issues_api, headers=headers).json()
    issues = response.get("issues")

    for issue in issues:
        iid = issue.get("id")
        if iid not in [22, 21]:
            api = host + "issues/{}.json".format(iid)
            response = requests.delete(api, headers=headers)
            print "Delete-Issue-Api-Status: %s" %(response.status_code)

def list_users(host, api_key, headers):
    list_users_api = host + "users.json"
    r = requests.get(list_users_api, headers=headers)
    print "List-Users-Api-Response: %s" %(r.status_code)


def get_random_user(host, api_key, headers):
    list_users_api = host + "users.json"
    r = requests.get(list_users_api, headers=headers).json()

    users = r.get("users")
    random_user = choice(users)
    pid = random_user.get("id")
    random_user_api = host + "users/{}.json".format(pid)
    response = requests.get(random_user_api, headers=headers)
    print "Get-User-Api-Status: %s" %(response.status_code)

def create_user(host, api_key, headers, mail, firstname, lastname):
    list_users_api = host + "users.json"
    r = requests.get(list_users_api, headers=headers).json()
    users = r.get("users")
    existing_login = [i.get('login') for i in users]

    login = firstname.replace(' ', '').lower()
    if login in existing_login: login = login + ''.join(choice(string.ascii_lowercase) for i in range(3))

    user = {"login":login,
            "firstname":firstname,
            "lastname":lastname,
            "mail":mail,
            "password": "tracker@123",
            "must_change_passwd": "true"}

    data = json.dumps({"user": user, "send_information": "true"})
    create_user_api = host + "users.json"
    response = requests.post(create_user_api, data=data, headers=headers)
    if response.status_code != 201:
        print "\n\nHey Pls try to create my account again. Email: %s, Api-Response: %s\n" %(mail, response.status_code)
    else:
        print "Email: %s, Api-Response: %s" %(mail, response.status_code)

def filter_user(host, api_key, headers, emails_list):
    list_users_api = host + "users.json"
    r = requests.get(list_users_api, headers=headers).json()
    users = r.get("users")

    existing_users = [i.get('mail') for i in users]
    new_users = [email for email in emails_list if email not in existing_users]
    return new_users, existing_users


def filter_email_from_csv(incsv):
    users_email = []
    with open(incsv) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #if not row['LastName']: row['LastName']='last_name'
            #users.append({'fname': row['FirstName'], 'lname': row['LastName'], 'mail': row['UserPrincipalName']})
            users_email.append(row['UserPrincipalName'])
    return users_email

def email_firstname_map(incsv):
    email_firstname_map = {}
    with open(incsv) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email_firstname_map[row['UserPrincipalName']] = row['FirstName']
    return email_firstname_map

def email_lastname_map(incsv):
    email_lastname_map = {}
    with open(incsv) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row['LastName']: row['LastName']='lastname'
            email_lastname_map[row['UserPrincipalName']] = row['LastName']
    return email_lastname_map

# Local host api call
# host = "http://127.0.0.1:3000/"
# api_key = os.environ.get("TRACKER_LOCAL_API")

#bugs portal api call
host = "https://bugs.chumbak.com/"
api_key = os.environ.get("TRACKER_CHUMBAK_API")

# set required headers
headers = {'X-Redmine-API-Key': api_key, 'Content-type': 'application/json'}

skip_email = skip_email_list()

users_email = filter_email_from_csv('users.csv')

email_lastname_map = email_lastname_map('users.csv')

email_firstname_map = email_firstname_map('users.csv')

new_user_email, existing_user = filter_user(host, api_key, headers, users_email)

for mail in new_user_email:
    firstname = email_firstname_map.get(mail, "firstname")
    lastname = email_lastname_map.get(mail, "lastname")
    sleep(10)
    if mail not in skip_email:
        print "Hello"
        # create_user(host, api_key, headers, mail, firstname, lastname)
        print "World"


# Other Userful APIs
#home(host, api_key, headers)
#list_projects(host, api_key, headers)
#get_random_project(host, api_key, headers)
#create_project(host, api_key, headers)
#delete_projects(host, api_key, headers)
#list_issues(host, api_key, headers)
#get_random_issue(host, api_key, headers)
#create_issue(host, api_key, headers)
#delete_issues(host, api_key, headers)
#list_users(host, api_key, headers)
#get_random_user(host, api_key, headers)
#create_user(host, api_key, headers, 'rksbtp@gmail.com', 'rishi', 'kant')
