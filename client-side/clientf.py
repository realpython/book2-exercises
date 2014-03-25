# XML Parsing 2


from xml.etree import ElementTree as et

doc = et.parse("cars.xml")

# outputs the make, model and cost of each car to the screen
for element in doc.findall("CAR"):
    print (element.find("MAKE").text + " " + 
           element.find("MODEL").text +
           ", $" + element.find("COST").text)
