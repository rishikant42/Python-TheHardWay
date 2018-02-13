import os
from random import choice
from locust import HttpLocust, TaskSet, task

from bs4 import BeautifulSoup


class MyTaskSet(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        response = self.client.get("login/")
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        auth_token = soup.body.find(id="login-form").find(attrs={"name":"authenticity_token"})['value']
        username = "XXXXX"
        password = "XXXX"
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.client.post("login/", {"username": username, "password": password, "authenticity_token":auth_token}, headers=headers)
        print "Login-Api-Status: %s" % (response.status_code)

    @task
    def home(self):
        response = self.client.get("")
        print "Home-Api-Status: %s" %(response.status_code)

    @task
    def project(self):
        response = self.client.get("projects/")
        print "Project-Api-Status: %s" %(response.status_code)

    @task
    def activity(self):
        response = self.client.get("activity/")
        print "Activity-Api-Status: %s" %(response.status_code)

    @task
    def issues(self):
        response = self.client.get("issues/")
        print "Issues-Api-Status: %s" %(response.status_code)

    @task
    def gantt(self):
        response = self.client.get("issues/gantt")
        print "Gantt-Api-Status: %s" %(response.status_code)

    @task
    def calendar(self):
        response = self.client.get("issues/calendar")
        print "Calendar-Api-Status: %s" %(response.status_code)

    @task
    def news(self):
        response = self.client.get("news")
        print "News-Api-Status: %s" %(response.status_code)

    @task
    def admin(self):
        response = self.client.get("admin")
        print "Admin-Api-Status: %s" %(response.status_code)

    # @task
    def create_issue(self):
        response = self.client.get("projects/applebug/issues/new")
        #cookies = response.cookies
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        auth_token = soup.body.find(id="content").find(attrs={"name":"authenticity_token"})['value']
        headers = {'content-type': 'multipart/form-data'}
        response = self.client.post("projects/applebug/issues", {"issue[subject]": "BugByLocust", "issue[description]": "I am locust", "authenticity_token":auth_token, "project_id": "applebug"}, headers=headers)
        print "Message: %s" % (response.status_code)


class WebsiteUser(HttpLocust):
    host = "http://127.0.0.1:8888/"
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 9000
