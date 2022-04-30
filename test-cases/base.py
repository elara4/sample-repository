
import json
import sys
import urllib2
import os

s1 = """
Usage: ./tweet_search.py 'keyword'
e.g ./tweet_search.py pythonforbeginners

Use "+" to replace whitespace"
e.g ./tweet_search.py "python+for+beginners"
"""

if len(sys.argv)!=2:
    print(s1)
    sys.exit(0)

s2 = sys.argv[1]

s3 = 1

s4 = 2

s5 = urllib2.urlopen("http://search.twitter.com/search.json?q="+screen)

s6 = json.load(s5)

print(len(s6), "tweets")

for s7 in s6["results"]:
    print(s7["text"])

for s8 in s6['results']:
    print("(%s) %s" % (s8["created_at"], s8["text"]) )

s9 = a + b

s10 = c + d + e