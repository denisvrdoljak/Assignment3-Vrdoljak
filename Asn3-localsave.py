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

conn = S3Connection(aws_access_key_id, aws_secret_access_key)
s3bucket = conn.get_bucket(S3_Bucket)

for eachkey in s3bucket.list():
    #print each
    #print each.generate_url(0, query_auth=False, force_http=True)
    if "083859" in str(eachkey):
        tweetskey = eachkey
print "Found it:\n/t",tweetskey

#denisvrdoljak-w205-asn2,both/NBA_JSON.20150616-083859.json>
print "\n"


#tweetskey = s3bucket.get_key("3NBA_JSON.20150616-094946.json")
hello_url = tweetskey.generate_url(0, query_auth=False, force_http=True)
print hello_url


tweetskey.get_contents_to_filename('tweets.json')


