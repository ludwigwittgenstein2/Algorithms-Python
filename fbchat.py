"""
Test FB chat/Module
"""

import fbchat
from getpass import getpass
username = str(raw_input("Username:"))
client = fbchat.client(username, getpass())
no_of_friends = int(raw_input("Number of friends:"))

for i in range(no_of_friends):
    name = str(raw_input("Name:"))
    friends = client.getUsers(name)
    friend = friends[0]
    msg=str(raw_input("Message:Test, Python"))
    sent = client.send(friend.uid, msg)
    if sent:
        print("Sent")
