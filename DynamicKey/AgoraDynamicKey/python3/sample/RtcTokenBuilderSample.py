#! /usr/bin/python
# ! -*- coding: utf-8 -*-

import sys
import os
import time
from random import randint
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee

appID = "f68f8f99e18d4c76b7e03b2505f08ee3"
appCertificate = "6fa04d10a03442f09b859f6d91bbea58"
channelName = "xyz"
uid = "abc-55441-u1"
userAccount = "2882341273"
expireTimeInSeconds = 3600
currentTimestamp = int(time.time())
# privilegeExpiredTs = currentTimestamp + expireTimeInSeconds
privilegeExpiredTs = 1611010057 + 60
role = 1

def main():
    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, role, privilegeExpiredTs)
    print("Token with int uid: {}".format(token))
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, role, privilegeExpiredTs)
    print("Token with user account: {}".format(token))


    appId1 = "f68f8f99e18d4c76b7e03b2505f08ee3"
    appCertificate1 = "6fa04d10a03442f09b859f6d91bbea58"
    channelName1 = "xyz"
    uid1 = "abc-55441-u1"
    role1 = str(1)

    print("its us now")
    token = RtcTokenBuilder.buildTokenWithUid(appId1, appCertificate1, channelName1, uid1, role1, privilegeExpiredTs)
    print(token)



if __name__ == "__main__":
    main()
