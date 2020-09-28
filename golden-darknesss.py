from __future__ import print_function
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
from huepy import *
import requests
import os
import argparse
import math
import urllib3
import re
import mechanize


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#logomakr.com/9J7b8j

parser = argparse.ArgumentParser()
parser.add_argument('-l', help = "length of word", dest = 'length', type = int, default = -1)
parser.add_argument('-s', help = "starting with this string", dest = 'start', default = '')
parser.add_argument('-e', help = "ending with this string", dest = 'end', default = '')
parser.add_argument('-i', help = "index of string", dest = 'index', type = int, default = -1 )
parser.add_argument('-b', help = "value of string", dest = 'inbetween', default = '')
parser.add_argument('-c', help = "custom query input for web scrapping", dest = "custom", default = '739292hd')
parser.add_argument('-u', help = "if length is unknown", dest = 'unknown_length', action = 'store_true')

args = parser.parse_args() 

length = args.length
start = args.start
end = args.end
index = args.index
inbetween = args.inbetween
custom = args.custom
unknownLength = args.unknown_length
url = ''
custom_regex = re.compile('[(*)(-)a-zA-Z]+')
entered_regex = re.compile('\\w*[^A-Za-z(-)(*)]+\\w*')
exit_ = False

print(red('''
                         WELCOME TO......
                       
	                    __       __              
	   ____ _  ____    / /  ____/ /  ___    ____ 
	  / __ `/ / __ \\  / /  / __  /  / _ \\  / __ \\
	 / /_/ / / /_/ / / /  / /_/ /  /  __/ / / / /  
	 \\__, /  \\____/ /_/   \\__,_/   \\___/ /_/ /_/ 
	/____/                                       
	                                                                            
	                                             
	    ____                     __                                        
	   / __ \\  ____ _   _____   / /__   ____   ___    _____   _____   _____
	  / / / / / __ `/  / ___/  / //_/  / __ \\ / _ \\  / ___/  / ___/  / ___/
	 / /_/ / / /_/ /  / /     / ,<    / / / //  __/ (__  )  (__  )  (__  ) 
	/_____/  \\__,_/  /_/     /_/|_|  /_/ /_/ \\___/ /____/  /____/  /____/                                                                     
	 
 '''))


if not unknownLength:
	if length == -1 and custom == '739292hd' and unknownLength == False:
		print(bad("at least one of -l [LENGTH] , -c [CUSTOM] and -u [UNKNOWN LENGTH] required"))
		exit()
	elif entered_regex.match(start) or entered_regex.match(end) or entered_regex.match(inbetween):
		print(bad("Words aren't allowed to contain characters other than alphabets."))
		exit()
	elif length > 0 :
		if length < len(start + inbetween +  end):
			print(bad("Please check the length of string entered. its sub strings seems to exceed it."))
			exit()

	if(exit_):
		exit()


	if custom == '739292hd' :
		if(index == -1):
			index = len (start)


		if length == -1 or length > 0 :
			if start == '' and end == '' :
				if length == -1 :
					print(bad('length of word is required for this case.'))
					exit()
				elif inbetween != '':
					if (index + len(inbetween))<= length :
						for i in range(length - index):
							url += '-'
						url += inbetween
						for i in range(length - len(url)):
							url += '-'

					else:
						print(bad('Invalid Case. Please check the length of word.'))
						exit()

				else:
					for i in range(length):
						url += '-'


			elif start == '' :
				for i in range(index):
					url += '-'
				url += inbetween
				for i in range( length - len(end) - index - len(inbetween)):
					url += '-'
				url += end
				

			elif index - len(start) >= 0  :
				if end == '':
					url += start
					for i in range(index - len(start)):
						url += '-'
					url += inbetween
					for i in range( length - index - len(inbetween)):
						url += '-'
				else:
					if index - len(start) >= 0:
						url += start
					for i in range(index - len(start)):
						url += '-'
					url += inbetween
					for i in range( length - index - len(inbetween) - len(end)):
						url += '-'
					url += end
			
			else:
				print(bad('In between string index overlaps the starting string.'))
				exit()

			

		else:
			print(bad('Length of word can\'t be negative'))
			exit();
	elif custom_regex.match(custom) :
		url = custom
	else:
		print(bad('Custom search url isn\'t valid.'))
		exit()

else :
	url = start + '*' + inbetween
	if(inbetween != ''):
		url += '*'
		if(end != ''):
			url += end
	else:
		url += end
if url == '*' :
	print(que("WARNING : Very few information parsed to find words."))

scrap_url = 'https://morewords.com/search?w=' + url



words = []

br = mechanize.Browser()
br.open(scrap_url)


for form in br.forms():
    if form.attrs.get('id') == 'max-results-form':
        br.form = form
        break
    


br.form["max_results"] = ["all"]


all_submit = br.submit()
source = br.response().read()
soup = BeautifulSoup(source, 'lxml')

div = soup.find('div',class_ = 'search-results')

m=''
j=1
while os.path.isfile(url + m):
	m='(' + str(j) + ')'
	j+=1

f = open (url + m + ".txt", 'w')

for a in div.findChildren('a',recursive=False):
	result = ''.join([i for i in a.text if not i.isdigit()])
	words.append(result.strip())
	f.write(result.strip() + '\n')	


f.close()


print(good(str(len(words)) + " words saved to " + url + m + ".txt "))









