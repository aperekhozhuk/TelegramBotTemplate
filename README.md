# TelegramBotTemplate

# What is it?
I made this repository as a basic template for my future
bots written with python-telegram-bot, which should persist some data in database
(I'm using Postgres).

It has simple and clear structure which easy for understand and can be extended with your functionality.

# Project files:
* .gitignore - for ignoring environment libs, python .pyc files.
* Procfile - for deploying to Heroku.
* requirements.txt - contains list of all python libs dependencies.
* run.py - for running bot.
* app/settings.py - you can paste your settings here.
* app/database.py - database connection settings, most likely you don't need to touch them except you really know what you do.
* app/models.py - add your own database models here.
* app/views.py - add your own views (functions that are using to respond to user).
* app/bot.py - here you can add needed handlers and assign them with views from app/views.py.

# Requirements:
1) Python 3 with pip installed.
3) Postgres installed.
4) Telegram bot created with BotFather and valid token for it.
5) Heroku CLI - only for deployment to Heroku.

# Running locally:
1) Clone repository firstly:
```
git clone https://github.com/aperekhozhuk/TelegramBotTemplate && cd TelegramBotTemplate
```
2) Create virtual environment && switch into it:
```
python3 -m venv env && source env/bin/activate
```
3) Install requirements:
```
pip install -r requirements.txt
```
***Warning:*** In some cases "psycopg2" package can demand some additional software
(check in google how to install it for your OS).

4) Create new database in Postgres and construct url for it.
5) Add environment variables for your project (see app/settings.py file).

***Warning:*** You can set settings as environment variables or set it directly in file, but anyway you should keep in secrete your sensitive settings (APP_URL, DATABASE_URL, API_TOKEN), don't commit them - you can use "git stash" instead for example.

6) Create database tables:
```
python app/database.py
```
7) run bot:
```
python run.py
```

# Deploying to Heroku:
1) Sign up / sign in to Heroku.
2) Create new Heroku app.
3) Add "Heroku Postgres" add-on to your app.
4) Config environment variables in your Heroku app: (on your app page click "Settings" -> "Reveal Config vars")
```
# Your api token which you got from BotFather.
TELEGRAM_BOT_API_TOKEN
# Heroku creates it automatically by default, just ensure that it presents.
DATABASE_URL
# set it to "PRODUCTION" (default value is "DEVELOPMENT" - only for local running).
TELEGRAM_BOT_MODE
# also created automatically by Heroku but not listed in config vars.
# don't set it because it's Heroku system variable.
# If you overwrite it - you'll have problems, I promise)
PORT
# set it to link to your heroku app (don't forget back slash in the end)
TELEGRAM_BOT_APP_URL
```
5) Move to repository root folder (if you not here).
6) Login to Heroku CLI:
```
heroku login
```
7) Add heroku app repository to your remotes (replace "YourAppName" with your real heroku app name):
```
heroku git:remote -a YourAppName
```
8) Push project to heroku repository:
```
git push heroku
```
9) Create database's tables:
```
heroku run python app/database.py
```
10) Restart your dyno (because first running fails because of database schema missing)
```
heroku dyno:restart
```

# Links:
1. [How to create bot with BotFater](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
2. [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
3. [Heroku.com](https://heroku.com)
4. [How to Deploy a Telegram Bot using Heroku for FREE](https://towardsdatascience.com/how-to-deploy-a-telegram-bot-using-heroku-for-free-9436f89575d2)
5. [PostgreSQL site](https://www.postgresql.org/)
6. [Postgres cheat sheet](https://www.postgresqltutorial.com/postgresql-cheat-sheet/)
7. [SQLAlchemy Object Relational Tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
