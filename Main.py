# -*- coding: utf-8 -*-

from functions import *
print("Exit code = 0")
x = 1
while x != 0:
	x = sources_list()
	if x > 0 and x < 3:
		newsApi_API(x)
	elif x == 0:
		thankyou()
	else:
		invalid()

		
#webscraping not implemented yet