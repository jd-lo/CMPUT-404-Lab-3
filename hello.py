#!/usr/bin/env python3

import os
import json

import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
#print(os.environ)
print(json.dumps(dict(os.environ), indent = 2))
#print(f"<p>HTTP_USER_AGENT={dict(os.environ['HTTP_USER_AGENT'])}</p>")

