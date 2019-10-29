# Neighbourhood Watch App
This is an app developed with django with the aim of getting a better understanding of django framework.

# Description
This is a simple that allows user to create accounts and login to them with their credentials. The site also supports uploading of projects one has done and their live links. Logged in users are able to view projects posted by other users on the home page of site and click on the project's image to view more detaials of the project, rate the projects based on design, content and usability and also make a review on a the projects.

# Set Up and Installations
Prerequisites Ubuntu Software Python3.6 Postgres python virtualenv

1. Clone the project repo by running <git clone https://github.com/Gideon-Muriithi/neighbourhood_watch>.

2. Create virtual environment by running <python3.6 -m venv pip virtual> while in the dirctory of the cloned project. Activate the virtual environment by running <source virtual/bin/activate>.

3. Install all the dependencies necessarry for running the application using this command: pip install-r requirements.txt

4. Create a database: psql then create the databse using this command: CREATE DATABASE awwards

5. Run migrations using these respective commmands: python3.6 manage.py makemigrations images then: python3.6 manage.py migrate

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