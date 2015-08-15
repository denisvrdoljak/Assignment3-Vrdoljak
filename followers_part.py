import time, tweepy, sys
auth_MODE = "Twitter"
UTILS_FOLDER = "DenisUtils"
S3_Bucket = "denisvrdoljak-w205-asn2"

"""
## authentication
username = '' ## put a valid Twitter username here
password = '' ## put a valid Twitter password here
#auth     = tweepy.auth.BasicAuthHandler(username, password)
"""

#setConfigVars(loadConfigs(auth_MODE))
import getpass

username = getpass.getuser()
utils_path = "/users/" + username + "/" + UTILS_FOLDER
sys.path.append(utils_path)

import Keychain
keyfob = Keychain.Keychain()
#print "keysets available:", keyfob.get_config_options()
key_dictionary = keyfob.loadConfigs(auth_MODE)
print "Successful keys load? -->", keyfob.setConfigsGlobal(key_dictionary)
for key, val in key_dictionary.items():
    exec(key + "= '" + val + "'") in globals()
########################

try:
    conn=pymongo.MongoClient()
    print "Connected!"
except pymongo.errors.ConnectionFailure, e:
    print "Connection failed : %s" % e 

db_follwers2_db = conn['db_followers']
followers_db = db_follwers2_db.my_collection
followers.count()

api = tweepy.API(auth_handler=auth)

top30 = list(top30coll.find())
for row in top30:
    userid = row.get("user").get("name")
    print userid
    try:
        followers = list(tweepy.Cursor(api.followers, screen_name=userid).items())
    except:
        followers = list()
    for follower in followers:
        print "\t", follower.screen_name
    followers_db.insert({u"user": userid },{"$set": {u"follower": follower.screen_name } })

followers_db.count()
        
        followers_db.findAndModify({
            query: { u'user': userid },
            update: { $inc: { u'follower': follower } },
            upsert: true
        })