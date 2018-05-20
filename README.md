
This API local server developed using python-django web framework. This project is code with python3.


1. install python3, virtualenv for local environment.

2. setup local environment with virtualenv <br />
    "virtualenv -p python3 venv"

3. activate your local environment<br />
    "source venv/bin/activate"

4. create local mysql database. If not, you can modify at <project>/friend_management/settings.py<br />
    database_name: friend_management<br />
    database_user: root<br />
    database_password: root<br />

5. go to project direcotry and run command below to install all project local requirements library.<br />
    a. "pip install -r requirements.txt"

6. go to project directory that has manage.py and run command below to create DB tables.<br />
    a. "python manage makemigrations"<br />
    b. "python manage migrate"

7. run at local server with command below at 127.0.0.1:8000.<br />
    a. "python manage runserver"
    
<br />
Project API.<br />
1. http://127.0.0.1:8000/friend/add_friend          POST method<br />
2. http://127.0.0.1:8000/friend/friend_list         POST method<br />
3. http://127.0.0.1:8000/friend/common_friend_list  POST method<br />
4. http://127.0.0.1:8000/friend/subscribe_update    POST method<br />
5. http://127.0.0.1:8000/friend/block_friend        POST method<br />
6. http://127.0.0.1:8000/friend/send_message        POST method
