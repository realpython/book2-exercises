# XML Parsing 3


from xml.etree import ElementTree as et
import requests

# retrieve an xml document from a web server
xml = requests.get("http://www.w3schools.com/xml/cd_catalog.xml")

with open("test.xml", "wb") as code:
    code.write(xml.content)

doc = et.parse("test.xml") 

# outputs the album, artist and year of each CD to the screen
for element in doc.findall("CD"):
    print "Album: ", element.find("TITLE").text
    print "Artist: ", element.find("ARTIST").text
    print "Year: ", element.find("YEAR").text, "\n"
