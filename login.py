#!/usr/bin/env python3
#code taken from lab demo
import cgi, cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret, os
from http.cookies import SimpleCookie

#create simple login form

#set up cgi form

s = cgi.FieldStorage()
#add input boxes
username = s.getfirst("username")
password = s.getfirst("password")


#check if correct login info was given to cgi
form_ok = username == secret.username and password == secret.password

#set up cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None

if cookie.get("username"):
    cookie_username = cookie.get("username").value

if cookie.get("password"):
    cookie_password = cookie.get("password").value

#check if cookie matches actual password/user
cookie_ok = cookie_username == secret.username and cookie_password == secret.password
#... then set username/password to cookie username/pass
if cookie_ok:
    username = cookie_username
    password = cookie_password

#to html/web browser
#set cookie
print("Content-Type: text/html")
if form_ok:
    print("Set-Cookie: username={}".format(username))
    print("Set-Cookie: password={}".format(password))
print()


#load login page/html
if not username and not password:#if user has not submitted form
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())


