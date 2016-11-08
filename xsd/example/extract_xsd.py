import xml.etree.ElementTree as etree
import os

path = os.getcwd()
path = os.path.join(path, 'example/1.xsd')
xml_string = open(path).read()
root = etree.fromstring(xml_string)

s = 0
for element in root.iter():
    # print "Tag:%s\nAttrib:%s\nText:%s" % (element.tag, element.attrib,
    # element.text)
    if element.attrib.has_key('XYZ'):
        print element.attrib['XYZ'].split(',')
        s = s + 1

print s
