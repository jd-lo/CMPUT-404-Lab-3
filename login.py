#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()
import os
import json
from http.cookies import SimpleCookie
import secret
from templates import login_page, secret_page, after_login_incorrect

s = cgi.FieldStorage()
username = s.getfirst('username')
pw = s.getfirst('password')

form_ok = username == secret.username and pw == secret.password

#Headers
print('Content-Type: text/html')
if form_ok:
    print(f'Set-Cookie: username={username}')
    print(f'Set-Cookie: password={pw}')
print()#New line to delineate the body

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username, cookie_password = None, None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_username = cookie.get("password").value

cookie_ok = cookie_username == secret.username and cookie_password == secret.password

#Make sure we aren't storing bad values
if cookie_ok:
    username = cookie_username
    password = cookie_password

if not username and not pw:
    print(login_page())
elif username == secret.username and pw == secret.password: 
    print(secret_page(username, pw))
else:
    print(login_page())
    print(f'Username and password: {username}, {pw}')
