# title = buttercup / url based web brute force tool
# author = jolankaa / https://github.com/jolankaa
# website = https://iconsoftware.systems 
import os
try:
	import requests
except ModuleNotFoundError:
	os.system("pip install requests")
import time
import sys
from platform import system
import datetime 
import os

proxy = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

error="""
  ___  ______________  _____
 / _ \/ ___/ ___/ __ \/ ___/
/  __/ /  / /  / /_/ / /    
\___/_/  /_/   \____/_/     
"""

help_menu = """
For Use :
python3 buttercup.py <url(no http/https)> <wordlist> <subdomain on\of>

"""

banner ="""
888~~\  888   | ~~~888~~~ ~~~888~~~ 888~~  888~-_    e88~-_  888   | 888~-_   
888   | 888   |    888       888    888___ 888   \  d888   \ 888   | 888   \  
888 _/  888   |    888       888    888    888    | 8888     888   | 888    | 
888  \  888   |    888       888    888    888   /  8888     888   | 888   /  
888   | Y88   |    888       888    888    888_-~   Y888   / Y88   | 888_-~   
888__/   "8__/     888       888    888___ 888 ~-_   "88_-~   "8__/  888      

Url Based Brute Force Tool .
															               
									AUTHOR = JOLANKA
"""
try:
	url = sys.argv[1]
	wordlist = sys.argv[2]
except IndexError:
	print(error)
	print(help_menu)
	exit()

def ProsesStart():
	print("[{}] Buttercup started ".format(datetime.datetime.today()))
	time.sleep(1)
	directory = "." # . kullanarak mevcut dizin
	directory2 = "./logs"
	folder = []
	in_logs_file = []

	for filename in os.listdir(directory):
	    if os.path.isdir(os.path.join(directory, filename)):
									folder.append(filename)

	if ("logs" not in folder):
		description ="this is only done the first time you open it".upper()
		time.sleep(1)
		print("[{}] Setting up ({}) ".format(datetime.datetime.today(),description))
		time.sleep(2)
		print("[{}] Creating logs Folder".format(datetime.datetime.today()))
		folder_name = "logs"
		os.mkdir(folder_name)

	for filename2 in os.listdir(directory2):
		in_logs_file.append(filename2)

	if("buttercup.log" not in in_logs_file):
		with open("logs/buttercup.log","a",encoding="utf-8") as log_file:
			log_file.write("[{}] Created Log File".format(datetime.datetime.today()))
			log_file.close()
			time.sleep(1)
			print("\n[{}] Created Log File ".format(datetime.datetime.today()))

def buttercup():
		with open('{}'.format(wordlist) ,'r') as file:
			for line in file:
				try:
					sub_response = requests.get("https://{}.{}".format(line,url))
				except requests.exceptions.SSLError:
					sub_response = requests.get("http://{}.{}".format(line,url))
				if (sub_response.status_code == 200):
					print("[{}][+] Found :) {}.{}".format(datetime.datetime.today().today,line,url))
					with open("logs/buttercup.log","a",encoding="utf-8") as log_file:
						log_file.write("\n[{}] Requests {}.{} Found ✔ ".format(datetime.datetime.today(),line,url))
						log_file.close()
				else:
					print("[{}][-] Not Found :( {}.{}".format(datetime.datetime.today(),line,url))
					with open("logs/buttercup.log","a",encoding="utf-8") as log_file1:
						log_file1.write("\n[{}] Requests {}.{} Not Found  ".format(datetime.datetime.today(),line,url))
						log_file1.close()
					pass


if __name__ == "__main__":
	print(banner)
	ProsesStart()
	buttercup()

