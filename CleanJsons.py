import json
from bson import BSON

jsonfile = "tweets.json"
newjsonfile = "tweets2.json"

jsonfile = open(jsonfile)
jsondata = jsonfile.read()

warriors = "#warriors"
nbafinals = "#nbafinals"

open(newjsonfile,'w').close()
newjsonfile = open(newjsonfile,'wa')


for line in jsondata.split("\n"):
    #print type(line)
    #raw_input(line)
    if line != "":
        newjsonfile.write(line)
newjsonfile.close()
