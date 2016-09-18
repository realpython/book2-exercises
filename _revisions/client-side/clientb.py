# Downloading a web page


import requests

r = requests.get("http://www.python.org/")

# write the content to test_request.html
with open("test_requests.html", "wb") as code:
    code.write(r.content)
