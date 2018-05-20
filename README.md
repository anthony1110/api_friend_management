
This API local server developed using python-django web framework. This project is code with python3.


1. install python3, virtualenv for local environment.

2. setup local environment with virtualenv
    a. "virtualenv -p python3 venv"

3. activate your local environment
    a. "source venv/bin/activate"

4. create local mysql database. If not, you can modify at <project>/friend_management/settings.py
    database_name: friend_management
    database_user: root
    database_password: root

5. go to project direcotry and run command below to install all project local requirements library.
    a. "pip install -r requirements.txt"

6. go to project directory that has manage.py and run command below to create DB tables.
    a. "python manage makemigrations"
    b. "python manage migrate"

7. run at local server with command below at 127.0.0.1:8000.
    a. "python manage runserver"


Project API.
1. http://127.0.0.1:8000/friend/add_friend          POST method
2. http://127.0.0.1:8000/friend/friend_list         POST method
3. http://127.0.0.1:8000/friend/common_friend_list  POST method
4. http://127.0.0.1:8000/friend/subscribe_update    POST method
5. http://127.0.0.1:8000/friend/block_friend        POST method
6. http://127.0.0.1:8000/friend/send_message        POST method
