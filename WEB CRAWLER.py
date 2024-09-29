import requests, time, sys, lxml, re

print()
print()
print()
print()
print()
print()
print()
print()
print()
# domain = input("enter domain: ")
domain = "https://urbanshade.org"
if domain[:7] != "http://" and domain[:8] != "https://":
    domain = "http://"+domain
web = requests.get(domain)
if web.ok != True:
    print("could not connect to web")
    print("status code: ", web.status_code)
    exit(1)

if web.status_code != 200:
    print("Warning, status code not 200. Status Code: ", web.status_code)


content = web.text[web.text.find(">", web.text.find("<body"))+1:web.text.find("</body>")-1]
print(content)