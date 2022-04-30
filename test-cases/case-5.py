
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
    print(s1) # comment in nested
    sys.exit(0)

s2 = sys.argv[1] # comment after statement

# comment line

s3 = 1

'''
block comment
'''

s4 = 2

"""
block comment
"""

s5 = urllib2.urlopen("http://search.twitter.com/search.json?q="+screen)

'''
block comment
# with a comment line
'''

s6 = json.load(s5)

"""
block comment
# with a comment line
"""

print(len(s6), "tweets")

'''
block comment 
statement = 1 # with a comment after statement
'''

for s7 in s6["results"]:
    print(s7["text"])

"""
block comment 
statement = 1 # with a comment after statement
"""

for s8 in s6['results']:
    print("(%s) %s" % (s8["created_at"], s8["text"]) )

'''
block comment 
mulitple_line_string = """abcd
efghi
jkl"""
'''

s9 = a + b

"""
block comment 
mulitple_line_string = '''abcd
efghi
jkl'''
"""

s10 = c + d + e