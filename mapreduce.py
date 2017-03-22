d = "realdonaldtrump"
import tweet_download

import csv
import os 

twitter = []

f = open("C:/users/joshua keith/documents/twitter100.csv")
lines = csv.reader(f, delimiter = ",")
count = 0
for line in lines:
    rank = line[0]
    word = line[1].title()
    count += 1
    if count < 101:
        twitter.append(word)
    
from multiprocessing import Pool

def sanitize(w):
 
#Strip punctuation from the front
  while len(w) > 0 and not w[0].isalnum():
    w = w[1:]
 
#Strip punctuation from the back
  while len(w) > 0 and not w[-1].isalnum():
    w = w[:-1]
 
  return w

sanitize("!Josh!")

"""
Given a list of tokens, return a list of tuples of
titlecased (or proper noun) tokens and a count of '1'.
Also remove any leading or trailing punctuation from
each token.
"""
def Map(L):
 
  results = []
  for w in L:
    # True if w contains non-alphanumeric characters
    if not w.isalnum():
      w = sanitize(w)
 
    # True if w is a title-cased token
    if w.istitle():
      results.append ((w, 1))
 
  return results

Map("A beagle named Rawley joined a foxhound named Pip.")

"""
Group the sublists of (token, 1) pairs into a term-frequency-list
map, so that the Reduce operation later can work on sorted
term counts. The returned result is a dictionary with the structure
{token : [(token, 1), ...] .. }
"""

def Partition(L):
  tf = {}
  for sublist in L:
    for p in sublist:
      # Append the tuple to the list in the map
      try:
        tf[p[0]].append (p)
      except KeyError:
        tf[p[0]] = [p]
  return tf

Partition("A beagle named Rawley joined a foxhound named Pip. Then he made him mad.")
 
"""
Given a (token, [(token, 1) ...]) tuple, collapse all the
count tuples from the Map operation into a single term frequency
number for this token, and return a final tuple (token, frequency).
"""
def Reduce(Mapping):
  return (Mapping[0], sum(pair[1] for pair in Mapping[1]))
"""
If a token has been identified to contain
non-alphanumeric characters, such as punctuation,
assume it is leading or trailing punctuation
and trim them off. Other internal punctuation
is left intact.
"""

"""
Load the contents the file at the given
path into a big string and return it.
"""
def load(path):
 
  word_list = []
  #f = open("C:/Users/joshua keith/desktop/realdonaldtrump_tweets.txt", "r")
  f = open("C:/Users/joshua keith/desktop/" + d + "_tweets.txt", "r")
  for line in f:
    word_list.append (line)
 
  # Efficiently concatenate Python string objects
  return (''.join(word_list)).split ()

#load("C:/Users/Joshua Keith/Desktop/sample.txt")

"""
A generator function for chopping up a given list into chunks of
length n.
"""

def chunks(l, n):
  for i in xrange(0, len(l), n):
    yield l[i:i+n]
 
"""
Sort tuples by term frequency, and then alphabetically.
"""
def tuple_sort (a, b):
  if a[1] < b[1]:
    return 1
  elif a[1] > b[1]:
    return -1
  else:
    return cmp(a[0], b[0])
 
if __name__ == '__main__':
    shakespeare = "C:/Users/joshua keith/desktop/realdonaldtrump_tweets.txt"
    #shakespeare = "C:/Users/joshua keith/desktop/" + d + "tweets.txt"
# Load file, stuff it into a string
    text = load(shakespeare)

# Build a pool of 8 processes
    pool = Pool(processes =8,)
# Fragment the string data into 8 chunks
    partitioned_text = list(chunks(text, int(len(text)/8)))
# Generate count tuples for title-cased tokens
    single_count_tuples = pool.map(Map, partitioned_text)
# Organize the count tuples; lists of tuples by token key
    token_to_tuples = Partition(single_count_tuples)
# Collapse the lists of tuples into total term frequencies
    term_frequencies = pool.map(Reduce, token_to_tuples.items())
# Sort the term frequencies in nonincreasing order 
    shakesort = sorted(term_frequencies,key=lambda a: a[1],reverse=True)
    shake = list(shakesort)
    #print top 50
    for pair in shake[:50]:
        if pair[0] not in twitter:
    		print pair[0], "-", pair[1]
    		export = open(d + '_export.txt','a')
    export.close()
#    
#     

 
