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

#to html/web browser
print("Content-Type: text/html")
print()

#load login page, print user from info
if not username and not password:#if user has not submitted form
    print(login_page())
else: #OLD LAB DEMO PART
    print(login_page())
    print("username & password {}, {}".format(username, password))

