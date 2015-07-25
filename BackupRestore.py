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

def restorefroms3():
    for eachkey in s3bucket.list():
    if "db_restT" in eachkey.key:
        try:
            eachkey.set_contents_from_filename("/data/db/restT_restored.ns")
        except:
            print "Restore failed."
    if "db_tweets" in eachkey.key:
        try:
            eachkey.set_contents_from_filename("/data/db/db_tweets_restored.ns")
        except:
            print "Restore failed."

def backuptos3():
    if True:
        try:
            s3bucket.get_contents_to_filename("/data/db/restT_restored.ns")
        except:
            print "Backup failed."
    if "db_tweets" in eachkey.key:
        try:
            s3bucket.get_contents_to_filename("/data/db/db_tweets_restored.ns")
        except:
            print "Backup failed."

while(True):
    backupoption = raw_input("Enter 'B' to backup,\nEnter 'R' to restore\n'Q' to quit:")
    if 'B' in backupoption.split()[0]:
        print "Backing up..."
        print "Backup disabled, remove comment from script to enable"
        #backuptos3()
        
        
    elif 'R' in backupoption.split()[0]:
        print "Restoring..."
        print "Restore disabled, remove comment from script to enable"
        #restorefroms3()
        
    elif 'Q' in backupoption.split()[0]:
        print "Quitting..."
        break
    else:
        print "Response not understood..."
        continue

