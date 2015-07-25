import time, tweepy, sys

"""
## authentication
username = '' ## put a valid Twitter username here
password = '' ## put a valid Twitter password here
#auth     = tweepy.auth.BasicAuthHandler(username, password)
"""

auth_MODE = "Twitter"
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



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


#api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
api = tweepy.API(auth)

#q=["Warriors","NBAFinals2015"]
q=["#greece","#euro"]
##q += " since: 2015-04-01 until: 2015-04-17"
##= urllib.quote_plus(sys.argv[1])  # URL encoded query

# Additional query parameters:
since = "2015-05-01"
until= "2015-05-17"
# Just add them to the 'q' variable: q since: 2014-01-01 until: 2014-01-02"
tweetfp = open("newtweets.json",'a')
tcount=0
maxid = 999999999999999999

import json
tweetlist = list()
"""
for tweet in tweepy.Cursor(api.search,q=q,max_id=maxid-1).items(3):
   # FYI: JSON is in tweet._json
    print "Tweet #" + str(tcount) + "\t" + str(tweet.id)[-3:]
    maxid = tweet.id
    tcount +=1
    if tweet.id in tweetlist:
        print "DUPLICATE"
    else:
        tweetlist.append(tweet.id)
        tweetfp.write(str(tweet._json)+'\n')
"""

try:
    for i in range(200):
        for tweet in tweepy.Cursor(api.search,q=q,max_id=maxid-1).items(100):
           # FYI: JSON is in tweet._json
            print "Round " + str(i) + "\t" + "Tweet #" + str(tcount) + "\t" + str(tweet.id)[-3:]
            maxid = min(tweet.id,maxid)
            tcount +=1
            if tweet.id in tweetlist:
                print "DUPLICATE"
            else:
                tweetlist.append(tweet.id)
                tweetfp.write(json.dumps(tweet._json)+'\n')
        print"\n"

    tweetfp.close()
    print "tweets: " + str(len(tweetlist))
    print "unique tweets: " + str(len(set(tweetlist)))

except:
    tweetfp.close()
    print "tweets: " + str(len(tweetlist))
    print "unique tweets: " + str(len(set(tweetlist)))
    
