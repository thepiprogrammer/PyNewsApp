__all__ = ['sources_list', 'newsApi_API', 'further_read_theNextWeb', 'invalid', 'thankyou', 'notready']

#functions

import json
from pprint import pprint
from urllib.request import urlopen
import binascii
from image_retriever import return_image
import re 
from apikey import key

apiKey = key()

keys = {'1': "https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey={}".format(apiKey)
, '2': "https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey={}".format(apiKey)}

def sources_list():
	print("Possible news sources:\n\
	\t1: The Next Web\n\
	\t2: Google News\n\
	\t0: Exit\n")
	x = int(input("Enter your choice: "))
	return x

def newsApi_API(x):
	url = keys[str(x)]
	print()
	json_string = urlopen(url).read()

	#with open('jsondata.txt') as data_file:    
	data = json.loads(json_string)
	names = [d['title'] for d in data['articles']]
	#pprint(names)
	i = 1
	for name in names:
		print("{}: {}".format(i, name))
		i += 1
	print("\n")
	resp1 = "y"
	while (resp1 == "y" or resp1 == "Y"):
		resp1 = input("Would you like to read more of any of these articles? (y/n) ")
		if resp1 == "y" or resp1 == "Y":
			further_read_theNextWeb(data)
		else:
			print("Exiting The Next Web... \n")

def further_read_theNextWeb(data):
	resp2 = int(input("Which one? "))-1
	s = data['articles'][resp2]
	url = s['url']
	html = urlopen(url).read()
	
	#correction begins here

	#string_lst = ['\\n', '\\r', '\\xc0', '\\xc1', 'sc2']
	description = str(html).split("meta property=\"bt:body\" content=", 1)[1].split("\">", 1)[0]
	description = description.replace("\\r\\n\\r\\n", ' ').replace("\\r\\n", ' ').replace("\\\'", "\'").replace("\\xc2", ' ').replace("\\xc0", ' ').replace("\\t", ' ').replace("\\xa0", ' ')

	#description = re.sub(r"(?=("+'|'.join(string_lst)+r"))", ' ', description)

	#escapes = ''.join([chr(char) for char in range(1, 32)])
	#description = description.translate(None, escapes)

	#correction ends here
	print(image(s['urlToImage']))
	print("\nTitle: {}\n\n\
		Author: {}\n\n\
		Description: {}\n\n\
		To read more, go to {} \n".format(s['title'], s['author'], description, s['url']))

def image(url):
	return return_image(url, 0.05, 5)

def invalid():
	print()
	print("Invalid option, try again!")
	print("\n")

def thankyou():
	print()
	print("Thank you for using our news app!")
	print("\n")

def notready():
	print()
	print("Not ready yet, check back later!")
	print("\n")