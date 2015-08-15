import time, tweepy, sys

"""
## authentication
username = '' ## put a valid Twitter username here
password = '' ## put a valid Twitter password here
#auth     = tweepy.auth.BasicAuthHandler(username, password)
"""

auth_MODE = "AWS"
UTILS_FOLDER = "DenisUtils"
S3_Bucket = "denisvrdoljak-w205-asn2"

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

#print locals()
import boto
from boto.s3.connection import *

s3conn = S3Connection(aws_access_key_id, aws_secret_access_key)
s3bucket = s3conn.get_bucket(S3_Bucket)

for eachkey in s3bucket.list():
    print "Found:\n/t",eachkey

    tweets_string = eachkey.get_contents_as_string()
    tweets_string += '\n'
    count = 0
    
    try:
        conn=pymongo.MongoClient()
        print "Connected!"
    except pymongo.errors.ConnectionFailure, e:
        print "Connection failed : %s" % e 
    
    db_tweets_db = conn['db_tweets']
    
    dbtweetscoll = db_tweets_db.my_collection
    dbtweetscoll
    dbtweetscoll.count()
    count=0
    for tweet in tweets_string.split('\n'):
        if tweet == "":
            continue
        try:
            dbtweetscoll.insert(json.loads(tweet))
            count +=1
        except:
            pass

    print "Number of tweets: ",count
    print "Number of tweets in DB: ",dbtweetscoll.count()
    
#    conn.close()