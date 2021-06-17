virtual environment name: testenv




/////// commands i have used and things i had done
opened vscode terminal inside shopping website
1.pip install virtualenv
2.virtualenv testenv

3. cd testenv/Scripts && activate
4. cd ../../         ---to go back to the  project

5.pip install django       -----(inside testenv)
6.django-admin startproject myweb     ----------(my whole project name is myweb in which i can create various apps)

(a new folder named my web created inside shopping website folder
in which there were 3 files [another myweb folder with few files, db.sqlite3, manage.py ]

so i just copied everything inside myweb folder which is present inside shopping website and paste that inside shopping website folder
--basically done a folder up!)


changed my directory to shopping website
7. python manage.py runserver       ----to start my server

8. python manage.py startapp website    ----(website is the name of our application)