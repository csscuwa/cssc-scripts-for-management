import os
import sys

import xml.etree.ElementTree as ET
#Probs worth saying, ET isn't secure against malicious xml data.
#please be careful... (but as long as this script is the only thing that touches the xml, it'll be fine)

#I'll add a warning in eventually

eventsFileLocation = '.' #You'll want to change this on the server

xmlFile = open(eventsFileLocation + "/events.xml")

xmldoc = ET.parse(xmlFile)
root = xmldoc.getroot()

print(root[0].findall('item'))
