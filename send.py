#!/usr/bin/env python
import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random

try:
    import requests
except ImportError:
    print('Error !! : Some dependencies are not installed')
    print('Error Occured!!!\nUse Non-Supported Version')
    input('Press Any Key To Use Non-supported Version')
    os.system('bash send.sh --sendsms')

# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']

# The Credit For This Code Goes to the Coding Family. https://github.com/dan998/
# And The Contributors Mentioned At https://github.com/dan998/Cybersms/
# As beginners we would like you to share and leave your comments of how we can improve and be better to serve you.

def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def banner():
    clr()
    logo = """                                                  
     \033[0m████████████████████████████████████████████████████████████████████
     \033[0m████\033[92m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\033[0m████
     \033[0m██\033[92m▒▒\033[0m██         \033[93m___   _  ______  _  __ \033[94m   ______  _______      \033[0m██\033[92m▒▒\033[0m██
     \033[0m██  \033[92m▒▒\033[0m██      \033[93m/ _ | / |/ / __ \/ |/ /_\033[94m__/ __/  |/  / __/    \033[0m██\033[92m▒▒  \033[0m██
     \033[0m██    \033[92m▒▒\033[0m██   \033[93m/ __ |/    / /_/ /    /__\033[94m_/\ \/ /|_/ /\ \    \033[0m██\033[92m▒▒    \033[0m██
     \033[0m██      \033[92m▒▒\033[0m██\033[93m/_/ |_/_/|_/\____/_/|_/   \033[94m/___/_/  /_/___/  \033[0m██\033[92m▒▒      \033[0m██
     \033[0m██        \033[92m▒▒\033[0m██                                   \033[91mV1.4 \033[0m██\033[92m▒▒        \033[0m██
     \033[0m██          \033[92m▒▒\033[0m████████████████████████████████████████\033[92m▒▒          \033[0m██
     \033[0m██            \033[92m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            \033[0m██
     \033[0m██     \033[94mCoded by: https://github.com/dan998/                    \033[0m██
     \033[0m██     \033[94mYoutube : https://www.youtube.com/c/           \033[0m██
     \033[0m██   \033[94mInstagram : h     \033[0m██
     \033[0m██                                                                ██
     \033[0m████████████████████████████████████████████████████████████████████
     \033[92m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                                         """
    print(logo)
    print("\n")
    

def Track() :
  TXTID = input("Enter Text ID of Cybersms \n\t -->>")
  os.system(f"curl https://textbelt.com/status/{TXTID}")
  input("\nPress Enter To Exit..")
  print("\nThanks For Using Cybersms..")
  print("\tWe Hope To See You Again\n Type bash Run.sh\n\tTo Run Again..")
  input('\n\n\nThank You For Using Cybersms\nAfter v1.45 There are no Ads Enabled in this Tool.\nPress Enter To Continue.\n')
  os.system('figlet -f slant The Coding Family')
  print("We love you continue to support our team.\nThank you for your support...")
  exit()

while True:
	print("\033[0mThis Tool Is Used To Send Cyber Anonymous Messages")
	break
type = 0
try:
	if sys.argv[1] == "track":
		type = 1
except Exception:
	type = 0
if type == 1:
	print("Track The cyber Anonymous Message You Sent Using This Tool.")
	print()
	Track()
elif type == 0:
	while True:
		print("Enter The Details Of The Person You Want To Send Cyber Anonymous Message")
		cc = input("\tEnter Country Code (Without +) : ")
		if '+' in cc:
		        tc = list(cc)
		        tc.remove('+')
		        cc = ''.join(tc)
		        cc = cc.strip()
		if len(cc) >= 4 or len(cc) < 1:
		        print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
		        continue
		pn = input("Enter Phone Number : +" + cc + " ")
		if len(pn) <= 6:
		        print('\n\nInvalid Phone Number..\n')
		        continue
		numbe = cc + pn
		if not numbe.isdigit():
		            print('\n\nPhone Number Must Consist Of Numbers Only\n')
		            continue
		receiver = '+' + numbe
		text = input("Enter Message to send : ")
		
		resp = requests.post('https://textbelt.com/text',{
			'phone' : receiver,
			'message' : text ,
			'key' : 'textbelt'
		})
		
		print(resp.json())
		input('\n\n\nThank You For Using Cybersms\nAfter v1.49 There are no Ads Enabled in this Tool.\nPress Enter To Continue.\n')
		os.system('figlet -f slant Just Kidding')
		print("There's No Ads.\nWe love you continue to support our team.\nThank you for your support...")
		break
		if '"success" : true ' in resp.text:
		    print("\033[92m Message Sent Succesfully \033[0m")
		    input('\n\t\tPress Enter To Exit...')
		    banner()
		    exit()
		if '"success" : false ' in resp.text:
		    print("\033[91m Error Occured")
		    print("\033[91m Failed to send CyberSMS! ")
		    input('\n\t\tPress Enter To Exit...')
		    banner()
		    exit()
		exit() 
