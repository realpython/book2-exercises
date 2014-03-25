# XML Parsing 1


from xml.etree import ElementTree as et

# parses the file
doc = et.parse("cars.xml") 

# outputs the first MODEL in the file
print doc.find("CAR/MODEL").text
