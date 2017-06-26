import json
from pprint import pprint
from urllib.request import urlopen
from functions import *
print("Exit code = 0")
x = 1
while x != 0:
	x = sources_list()
	if x == 1:
		newsApi_API()
	elif x == 2:
		notready()
	elif x == 0:
		thankyou()
	else:
		invalid()
#webscraping not implemented yet