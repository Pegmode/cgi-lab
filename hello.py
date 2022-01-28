#!/usr/bin/env python3


import os, json


#show all environment variables in browser
print("Content-Type: text/plain")#content header for browser
print()
print(os.environ)