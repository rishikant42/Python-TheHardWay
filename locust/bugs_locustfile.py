import os
import string
import json
from random import choice
from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task(6)
    def home(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("", headers=headers)
        print "Home-Api-Status: %s" %(response.status_code)

    @task(2)
    def list_projects(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("projects.json/", headers=headers)
        print "List-Project-Api-Status: %s" %(response.status_code)

    @task(3)
    def get_project(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("projects.json/", headers=headers).json()

        projects = response.get("projects")
        random_project = choice(projects)
        pid = random_project.get("id")
        api = "projects/{}.json".format(pid)
        response = self.client.get(api, headers=headers)
        print "Get-Project-Api-Status: %s" %(response.status_code)

    @task(1)
    def create_project(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key, 'Content-Type': 'application/json'}
        project_name = 'Locust-' + ''.join(choice(string.ascii_letters + string.digits) for i in range(5))
        project_identifier = ''.join(choice(string.ascii_lowercase) for i in range(3))

        project = {"name":project_name, "identifier":project_identifier}
        data = json.dumps({"project": project})
        response = self.client.post("projects.json/", data, headers=headers)
        print "Create-project-Api-Response %s" %(response.status_code)

    # @task
    def delete_project(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("projects.json/", headers=headers).json()
        projects = response.get("projects")

        for project in projects:
            pid = project.get("id")
            api = "projects/{}.json".format(pid)
            response = self.client.delete(api, headers=headers)
            print "Delete-Project-Api-Status: %s" %(response.status_code)

    @task(2)
    def list_issues(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("issues.json/", headers=headers)
        print "Issues-Api-Status: %s" %(response.status_code)

    @task(3)
    def get_issue(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("issues.json/", headers=headers).json()
        issues = response.get("issues")
        random_issue = choice(issues)
        issue_id = random_issue.get("id")
        api = "issues/{}.json".format(issue_id)
        response = self.client.get(api, headers=headers)
        print "Get-Issue-Api-Status: %s" %(response.status_code)

    @task(4)
    def create_issue(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key, 'Content-Type': 'application/octet-stream'}

        # upload file
        content = open("file.txt", "rw").read()
        response = self.client.post("uploads.json/", content, headers=headers).json()
        token = response.get("upload").get("token")
        upload = {"token":token, "filename":"file.txt"}

        # get pid
        headers = {'X-Redmine-API-Key': api_key, 'Content-Type': 'application/json'}
        response = self.client.get("projects.json/", headers=headers).json()
        projects = response.get("projects")
        random_project = choice(projects)
        pid = random_project.get("id")

        # create issue body
        subject = 'Issue-' + ''.join(choice(string.ascii_letters + string.digits) for i in range(5))
        description = 'Description-Via-Locust-' + ''.join(choice(string.digits) for i in range(3))


        issue = {"project_id": pid,
                "subject": subject,
                "description": description,
                "uploads": [upload],
                "assigned_to_id": 1}

        data = json.dumps({"issue": issue})
        response = self.client.post("issues.json/", data, headers=headers)
        print "Create-Issue-Api-Status: %s" %(response.status_code)

    # @task
    def delete_issues(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("issues.json/", headers=headers).json()
        issues = response.get("issues")

        for issue in issues:
            iid = issue.get("id")
            if iid not in [22, 21]:
                api = "issues/{}.json".format(iid)
                response = self.client.delete(api, headers=headers)
                print "Delete-Issue-Api-Status: %s" %(response.status_code)

    @task(1)
    def activity(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("activity/")
        print "Activity-Api-Status: %s" %(response.status_code)

    @task(1)
    def gantt(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("issues/gantt", headers=headers)
        print "Gantt-Api-Status: %s" %(response.status_code)

    @task(1)
    def calendar(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("issues/calendar", headers=headers)
        print "Calendar-Api-Status: %s" %(response.status_code)

    @task(1)
    def news(self):
        api_key = os.environ.get("TRACKER_CHUMBAK_API")
        headers = {'X-Redmine-API-Key': api_key}
        response = self.client.get("news", headers=headers)
        print "News-Api-Status: %s" %(response.status_code)


class WebsiteUser(HttpLocust):
    host = "https://bugs.chumbak.com/"
    # host = "http://127.0.0.1:3000/"
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 9000
