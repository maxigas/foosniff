#!/usr/bin/python

# 1. Import libraries and functions

from pattern.web import Twitter, plaintext

# 2. Set variables

keyword = "cybernetics"
# keyword = "algorithm"

# 3. Initialise

twitter = Twitter(language='en')

# 4. Get data

for tweet in twitter.search(keyword, cached=False):
	t = plaintext(tweet.text).replace('\n','') + '|||\n'
	print plaintext(t)
	with open('corpus.txt', 'a') as f:
		f.write(t.encode('utf-8'))
		
