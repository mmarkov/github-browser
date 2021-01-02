# github-browser
This application is simple Flask app to browse github users stored in SQLite database.

## Setup local environment

Before you start you would need prepare your local environment. Here is short instruction for setup your envrionment on OS X

1. Install PyEnv `brew install pyenv penv-virtualenv`
2. Install NPM `brew install npm`
3. Install Heroku CLI  `brew tap heroku/brew && brew install heroku`

## Server

### Setup 
One time set up:
Install Python version 3.8.6 `pyenv install 3.8.6`
Create virtual environemtn `pyenv virtualenv 3.8.6 github-browser`
Activate it and install packages
```
pyenv activate github-browser
pip install -r requirements.txt
```

Please create environment configuration in `.env` file by copying `sample.env` to `.env`
There are three main parameters to change:
```
GUNICORN_PARAMS=<command line parameters of gUnicorn default=-c gunicorn.conf.py>
DATABASE_URL=<database path in SQL Alchemy format deafult=sqlite:///users.db>
GITHUB_TOKEN=<token to access github API, you can get one through settings, value is optional>
```

Every time you want to work on `pyenv activate github-browser` and after you finish work on project `pyenv deactivate`

### Database
Before using 

`python manage.py seed -t 150`

### Server 

Start python service locally `heroku local server`
Then you may navigate to http://127.0.0.1:3001/api/users to see API response


## Client

Install npm dependencies:

```
npm install
```

