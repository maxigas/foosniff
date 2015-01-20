#!/usr/bin/python

# 1. Import libraries and functions

from sys import stdout
from pattern.web import Twitter, plaintext
from pattern.db import Datasheet

# 2. Set variables

keyword = "cybernetics"
count   = 1000
# keyword = "algorithm"

# 3. Initialise

twitter = Twitter(language='en')
#ds = Datasheet()

# 4. Get data

# Twitter.search() returns up to 3000 results for a given query (30 queries with
# 100 results each, or 300 queries with 10 results each). It has a limit of 150
# queries per 15 minutes. Each call to search() counts as one query.

i = None
for x in range(count / 10):
	for tweet in twitter.search(keyword, start=x, count=10):
		i = tweet.id
		t = i + ' | ' + tweet.text.replace('\n','') + ' | \n'
		stdout.write('.')
		if (x % 5) == 0:
			with open('corpus.txt', 'a') as f:
				f.write(t.encode('utf-8'))
				stdout.write('*')
