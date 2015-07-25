try:
    conn=pymongo.MongoClient()
    print "Connected!"
except pymongo.errors.ConnectionFailure, e:
    print "Connection failed : %s" % e 

db_tweets2_db = conn['db_restT']
dbtweets2coll = db_tweets2_db.my_collection
dbtweets2coll.count()

db_tweets_db = conn['db_tweets']
dbtweetscoll = db_tweets_db.my_collection
dbtweetscoll.count()

print "RESTful (new) data database has\t" + str(dbtweets2coll.count()) + " tweets."
print "Retrieved data database has\t" + str(dbtweetscoll.count()) + " tweets."

len(list(dbtweets2coll.find({"retweet_count": {'$regex': '/([1-9])\+/'}})))



top30 = list(dbtweets2coll.find({"retweet_count": {'$gt': 690} }))
    #print "Lex count", len(set(lex))


top30[1].get("user")
top30[1].get("user").get("id")
#top30[1].get("user").get("_id")


db_top30 = conn['db_top30']
top30coll = db_top30.my_collection
top30coll.count()
for row in top30:
    top30coll.insert(row)
top30coll.count()

#top30file = open("Top30.txt",w)
for top in top30coll.find():
    print top.get("user").get("name"), "\tLexScore: ",getlex(top,top30coll),"\tLocation: ", top.get("user").get("location")
#    writeline = str(top.get("user").get("name")) + "\tLexScore: " + str(getlex(top)) + "\tLocation: " + str(top.get("user").get("location")))
#    top30file.write(writeline)
#top30file.close()



def getlex(tweet,db):
    lex = list()
    userid = tweet.get("user").get("id")
    for row in db.find({"user.id": userid}):
        usertext = row.get("text")
        lex += usertext.split(" ")
    return float(len(set(tweet.get("text").split(" ")))) / len(lex)

#all unique users in top30..actually top 43, 21-way tie at number 23
top30ids = [row.get("user").get("id") for row in top30]
len(top30ids)
len(set(top30ids))


for row in top30coll.find():
    lex = getlex(row, dbtweets2coll)
    rowid = row.get("_id")
#    print rowid, "\t", lex
    top30coll.update({"_id": rowid },{"$set": {u"lexscore": lex } })

for row in dbtweets2coll.find():
    print row.get("lexscore")



for row in dbtweets2coll.find():
    lex = getlex(row, dbtweets2coll)
    rowid = row.get("_id")
#    print rowid, "\t", lex
    dbtweets2coll.update({"_id": rowid },{"$set": {u"lexscore": lex } })

for row in dbtweets2coll.find():
    print row.get("lexscore")








    #(list(top30coll.find( { '_id': { '$eq': rowid } } ))

            
for row in top30coll.find():
    lex = getlex(row,top30coll)
    rowid = row.get("id")
    print rowid, "\t", lex
    print row.get("lexscore")
                        
                                    



    .top30coll.remove(
   <query>,
   {
     justOne: <boolean>,
     writeConcern: <document>
   }
   )
   
   
   top30coll.findAndModify({
    query: { '_id': rowid },
    update: { $inc: { u'lexscore': lex } },
    upsert: true
})
