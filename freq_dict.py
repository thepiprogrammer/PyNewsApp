import re

def make_dict():
	keyfile = open('keywords.txt', 'r')
	resp_file = open('out_res.txt', 'r')
	freq1 = word_freq(keyfile)
	freq2 = word_freq(resp_file)
	#word_freq = sorted(word_freq)
	#word_freq = sorted(word_freq.keys(), key=lambda x:x.lower())
	#corpus = len(words)*1.0
	#for key in word_freq:
	#	resp_file.write("{} --> {}      ---> {}%\n".format(key, word_freq[key], (word_freq[key]*100.0/corpus)))
	myList = []

	for key in freq2:
		try:
			if freq1[key] < 10:
				myList.append(key)
		except KeyError:
			myList.append(key)

	#print myList
	strr = "Some keywords are: {}".format([item for item in myList])
	print(re.sub('[^A-Za-z0-9:]+', ' ', strr))

	keyfile.close()
	resp_file.close()


def word_freq(file):
	data = file.read().lower()
	data = re.sub('[^A-Za-z0-9]+', ' ', data)
	words = data.split()
	word_freq = {}

	for word in words:
		if word in word_freq:
			word_freq[word] += 1
		else:
			word_freq[word] = 1

	return word_freq

make_dict()