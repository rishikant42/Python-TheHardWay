### Gmail Inbox client

Python scripts that integrates with GMail API and performs some rule based operations on emails.

### Tech stack:
- Python2.7

- Mysql database

- Google API python client

### Setup:
- Create virtualenv and install project dependencies in environment from *requirements.txt* `($ pip install -r requirements.txt)`

- Enable the [Gmail API](https://developers.google.com/gmail/api/quickstart/python)

- Save Gmail API credentials as *credentials.json* in working directory.

- Update DB configuration in *script1.py* and *script2.py*. You may need to save DB-user and DB-password in *~/.bashrc (or ~/.bash_profile)* file.

- Allow Gmail to give read pemission for *script1.py* and modify permission for *script2.py*. These scripts will create *token_read.json* and *token_modify.json* respectively in working directory.

**NOTE:** *rules.json* have list of rules. Right now *script2.py* is using *rule1* specifications.
