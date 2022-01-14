import urllib.request as request
import json

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["result"]["results"]

with open("data.csv","w",encoding="utf-8") as file:
    
    for location in clist:
        site=location['stitle']
        address=location["address"].split()[1][0:3]
        longitude=location["longitude"]
        latitude=location["latitude"]
        url='https'+location["file"].split('https')[1]
       
        file.write(site+','+address+','+longitude+','+latitude+','+url+'\n')


