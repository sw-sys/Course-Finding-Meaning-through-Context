# NOTES from https://github.com/jdportercode/TAP23
# 
# Getting word counts from texts
#

import os

# sample = "The pig and the dog went out to play. The dog had a ball and the pig had a stick. It was snack time and they shared a chocolate bar. This is a good way to play."
# sample.casefold()

## Some common case methods
# sample.upper()
# sample.lower()
# sample.title()
# sample.casefold()
# #Basically a more aggressive form of .lower()

## Some common character checks
# sample.isalpha()
# sample.isdigit()
# sample.isalnum() # alphanumeric

## Positioning/Index?
# sample[0] # first digit
# sample[-1] # last digit

### GETTING WORD COUNTS FROM TEXT

# filename
fn = "Chopin_Awakening.txt"

# open file
with open (fn) as source:
    text = source.read()

# turn text in to words
words = text.split()

# # check everythign working - first 100 words
# print(words[:100])

# clean the words

def alphaclean(someword):
    chars = [i for i in someword if i.isalpha()]
    cleanword = ''.join(chars)
    cleanword = cleanword.lower()
    return cleanword

# # test func w/ first 100 words
# print(alphaclean(words[:100]))

# count the words
counts = {}

for w in words:
    w = alphaclean(w)
    if w not in counts:
        counts[w] = 0
    counts[w] += 1

print(counts['edna'])