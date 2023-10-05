
from xml.dom.minidom import parseString
import requests
import csv

retrieveTags=['TrainStatus',
              'TrainLatitude',
              'TrainLongitude',
              'TrainCode',
              'TrainDate',
              'PublicMessage',
              'Direction'
              ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)
#check it works
print (doc.toprettyxml()) #output to console