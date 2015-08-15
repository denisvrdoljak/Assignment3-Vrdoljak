import time, tweepy, sys

    
count = 0

try:
    conn=pymongo.MongoClient()
    print "Connected!"
except pymongo.errors.ConnectionFailure, e:
    print "Connection failed : %s" % e 

db_tweets2_db = conn['db_restT']

dbtweets2coll = db_tweets2_db.my_collection
dbtweets2coll
dbtweets2coll.count()

count=0

jsonfile = "newtweets1.json"

jsonfile = open("/Users/denisvrdoljak/Berkeley/W205/Asn3_Work/newtweets1.json")
jsondata = jsonfile.read()
jsonfile.close()
for i in range(1):
    for tweet in jsondata.split("\n"):
        #print tweet[:20]
        if tweet == "":
            continue
        try:
            dbtweets2coll.insert(json.loads(tweet))
            count +=1
        except:
            pass

    print "Number of tweets: ",count
    print "Number of tweets in DB: ",dbtweets2coll.count()
    #dbtweetscoll.remove()
    #dbtweetscoll.count()
    conn.close()
    