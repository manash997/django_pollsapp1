# django_pollsapp1:
Django app for polling.This app can be used to generate polls and surveys as per requirement.
The admin can add questions as well as provide multiple options for the user to choose their answers from.

#app design:
The app begins with a home page where the new user can choose the signup option to register.Signup allows choosing a username(unique),password etc.
Once the registration is complete,the user can go for signin option and login with his credentials.
Successful login redirects the user to the app where he can view and answer multiple poll questions as set by the admin.

#admin panel:
Admin panel of the app allows exclusive access to superuser where he can view the information about registered users and also create or delete poll questions and options.

#Installation:
prerequisite:Create an empty folder and open it on vscode or any ide.
-set up new terminal on ide with cmd chosen

1)Create virtual env using cmd
go to terminal and type: py -3 -m venv "virtualenvname"  //without quotes choose a name for virtual environment eg. py -3 -m venv test
                       : virtualenvname/Scripts/activate  //eg. test/Scripts/activate

2)install django on virtual env:pip install django

3)Download the code from github repository
On terminal type:git clone https://github.com/manash997/django_pollsapp1.git

or download from the url:https://github.com/manash997/django_pollsapp1.git

4)Change current directory to django_pollsapp1 using command:cd django_pollsapp1 
-if downloaded from url type:cd completepath //specify the complete path of the code folder django_pollsapp1 



5)$ python manage.py runserver  //This is to run the app on localhost

6)Create username ,password etc.

7)login on app

8)To use the admin panel one needs to create superuser:
$ python manage.py create superuser
//after creating superuser it can be accessed on url:/admin








