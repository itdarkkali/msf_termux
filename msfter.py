import os
from sys import exit as exit
def install():
	os.system ("pkg update -y")
	os.system ("cd $HOME && git clone https://github.com/Hax4us/Metasploit_termux > nul")
	os.system ("cd $HOME/Metasploit_termux && chmod +x metasploit.sh")
	os.system ("cd $HOME/Metasploit_termux && bash metasploit.sh")
	os.system ("cd $HOME && bundle init > hdh.txt && rm -rf hdh.txt")
	os.system ("cd $HOME && gem install bundler -v 1.16.1")
	os.system ("cd $HOME && bundle install -j5")
	os.system ("cd $HOME/Metasploit_termux && bash metasploit.sh")
def main():
	print("""
             _____         
  __ _  ___ / _/ /____ ____
 /  ' \(_-</ _/ __/ -_) __/
/_/_/_/___/_/ \__/\__/_/
                             
---
Created By otx2s
Helped By YamkaFox
Ver: 2.0
---

""")
def yt():
	input("Press Enter")

main()
def doyouinstall():
	global fff
	fff = input("[???] Do you want to install metasploit? (y/n): ")
	if fff == "y":
		print("======================================")
		print("[+] Jesus, it will take a lot of time!")
		print("======================================")
		install()
		print("=====================================")
		print("[+] Metasploit installed successfully")
		print("[+] Type 'msfconsole' to start.")
		print("=====================================")
		exit()
	elif fff == "n":
		print("\nGoodbye...")
		print("=====================================")
		exit()
	else:
		doyouinstall()
while True:
	doyouinstall()


