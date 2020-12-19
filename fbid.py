#!/usr/bin/env python

print("""

In the name of Allah, the most Gracious, the most Merciful.

 ▓▓▓▓▓▓▓▓▓▓
░▓ Author ▓ Abdullah <https://abdullah.today>
░▓▓▓▓▓▓▓▓▓▓ YouTube <https://YouTube.com/AbdullahToday>
░░░░░░░░░░

░█▀▀░█▀▄░▀█▀░█▀▄
░█▀▀░█▀▄░░█░░█░█
░▀░░░▀▀░░▀▀▀░▀▀

""")

#  A simple script which prints the Facebook ID of given username.

import urllib.request, re

# username = input("please enter the Facebook username: ")

def ask_for_username(username):
    print("Please enter the Facebook username: ")
    print("Enter q to exit.")
    user = input('Enter username: ')

    if not user:
        print("You entered nothing...")
        return ask_for_username(username)
    elif user in ['q', 'Q']:
        print("quiting. Bye...")
        exit()
    else:
        regex = re.split(r'((http|https):\/\/)?(www\.)?(facebook|fb)\.com\/([.a-z0-9]+)', user.lower())
        uname = regex[0] if len(regex) == 1 else regex[5]
        send_request = urllib.request.urlopen(f'https://m.me/{uname}').geturl().split('%2F')
        ID = 'not found.' if len(send_request) < 2 else send_request[-2]
        print('ID:', ['not found.', ID][ID.isdecimal()])

ask_for_username('str')
