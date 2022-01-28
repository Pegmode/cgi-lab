#!/usr/bin/env python3
#code taken from lab demo
import os, json

# #show all environment variables in browser
# print("Content-Type: text/plain")#content header for browser
# print()
# print(os.environ)

# #PRINT ENV VARIBLES AS JSON
# print("Content-Type: application/json") #expect json
# print()
# print(json.dumps(dict(os.environ), indent = 2))#use ident format


#PRINT QUERY PARAMETER DATA IN HTML
# print("Content-Type: text/html")#let browser know to expect html
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

#print user browser info
print("Content-Type: text/html")#let browser know to expect html
print()
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")

