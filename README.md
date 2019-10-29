# Neighbourhood Watch App
This is an app developed with django with the aim of getting a better understanding of django framework.

# Description
This is a simple that allows user to create accounts and login to them with their credentials. Users can create profile based on neighbourhood they come from. The site also supports uploading of businesses and creating of posts. Logged in users are able to join different neighbourhoods to see posted businesses and different posts.

# Set Up and Installations
1. Prerequisites:

    ######  i. Python3.6 
     ###### ii. Postgres python 
     #####  iii. virtualenv

2. Clone the project repo by running <git clone https://github.com/Gideon-Muriithi/neighbourhood_watch>.

3. Create virtual environment by running <python3.6 -m venv pip virtual> while in the dirctory of the cloned project. Activate the virtual environment by running <source virtual/bin/activate>.

4. Install all the dependencies necessarry for running the application using this command: pip install-r requirements.txt

5. Create a database: psql then create the databse using this command: CREATE DATABASE awwards

6. Run migrations using these respective commmands: python3.6 manage.py makemigrations images then: python3.6 manage.py migrate

7. Run the app using this command: python3.6 manage.py runserver on the terminal.You can then open the app on your browser

8. Create .env file and paste the following text and fill your details where appropriate

    ##### SECRET_KEY = '<Secret_key>'
    ##### DBNAME = 'hood'
    ##### USER = ''
    ##### PASSWORD = ''
    ##### DEBUG = True
    ##### EMAIL_USE_TLS = True
    ##### EMAIL_HOST = 'smtp.gmail.com'
    ##### EMAIL_PORT = 587
    ##### EMAIL_HOST_USER = ''
    ##### EMAIL_HOST_PASSWORD = ''

9. Run initial Migration python3.6 manage.py makemigrations gram python3.6 manage.py migrate. 

10. Run the app python3.6 manage.py runserver Open terminal on localhost:8000

# Technologies used
Python 3.6 HTML Bootstrap 4 JavaScript Heroku Postgresql

# Support and contact details
For any comments, reviews or advice contact me on gideonapptests@gmail.com.

MIT License Copyright (c) Gideon Muriithi