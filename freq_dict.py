import re

def make_dict():
	keyfile = open('keywords.txt', 'r')
	resp_file = open('out.txt', 'w')
	data = keyfile.read().lower()
	data = re.sub('[^A-Za-z0-9]+', ' ', data)
	words = data.split()
	word_freq = {}

	for word in words:
		if word in word_freq:
			word_freq[word] += 1
		else:
			word_freq[word] = 1
	#word_freq = sorted(word_freq)
	#word_freq = sorted(word_freq.keys(), key=lambda x:x.lower())
	corpus = len(words)*1.0
	for key in word_freq:
		resp_file.write("{} --> {}      ---> {}%\n".format(key, word_freq[key], (word_freq[key]*100.0/corpus)))


	keyfile.close()
	resp_file.close()

make_dict()