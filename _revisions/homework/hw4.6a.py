# parse XML from Google Driving API


from xml.etree import ElementTree as et
import requests

url = "http://maps.googleapis.com/maps/api/directions/xml?origin=San+Francisco&destination=Los+Angeles&sensor=false"

# retrieve the xml
xml = requests.get(url)

with open("test.xml", "wb") as code:
    code.write(xml.content)

# parse the xml file
doc = et.parse("test.xml") 

for element in doc.findall("route/leg/step"):
    print element.find("html_instructions").text
