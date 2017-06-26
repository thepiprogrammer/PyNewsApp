#classifier copied from http://agiliq.com/blog/2009/03/finding-keywords-using-python/ 
#not linked to actual project

def find_keyword(test_string = 'This is a random sentence to check frequency'):
	key_file = open('keywords.txt', encoding="utf8")
	data = key_file.read()
	words = data.split()
	word_freq = {}
	for word in words:
		if word in word_freq:
			word_freq[word]+=1
		else:
			word_freq[word] = 1
	word_prob_dict = {}
	corpus = len(words)
	for word in word_freq:
		word_prob_dict[word] = float(word_freq[word])/corpus

	prob_list = []
	for word, prob in word_prob_dict.items():
		prob_list.append(prob)
		non_exist_prob = min(prob_list)/2

	words = test_string.split()
	test_word_freq = {}
	for word in words:
		if word in test_word_freq:
			test_word_freq[word]+=1
		else:
			test_word_freq[word] = 1

	test_words_ba = {}
	for word, freq in test_word_freq.items():
		if word in word_prob_dict:
			test_words_ba[word] = freq/word_prob_dict[word]
		else:
			test_words_ba[word] = freq/non_exist_prob

	test_word_ba_list = []
	for word, ba in test_words_ba.items():
		test_word_ba_list.append((word, ba))

	def sort_func(a, b):
		if a[1] > b[1]:
			return -1
		elif a[1] < b[1]:
		return 1
		return 0

	test_word_ba_list.sort(sort_func, keyword=lambda)
	return test_word_ba_list[:2]