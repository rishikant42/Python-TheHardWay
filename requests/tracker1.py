import os
import requests
import json
import string
from random import choice

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


# Local host api call
host = "http://127.0.0.1:3000/"
api_key = os.environ.get("TRACKER_LOCAL_API")

# bugs portal api call
#host = "https://bugs.chumbak.com/"
#api_key = os.environ.get("TRACKER_CHUMBAK_API")

# set required headers
headers = {'X-Redmine-API-Key': api_key, 'Content-type': 'application/json'}

# APIs
home(host, api_key, headers)
list_projects(host, api_key, headers)
get_random_project(host, api_key, headers)
create_project(host, api_key, headers)
#delete_projects(host, api_key, headers)
list_issues(host, api_key, headers)
get_random_issue(host, api_key, headers)
create_issue(host, api_key, headers)
#delete_issues(host, api_key, headers)
