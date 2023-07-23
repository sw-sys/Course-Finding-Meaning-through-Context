### SESSION 2
###
# NOTES from https://github.com/jdportercode/TAP23
#
# Semantic analysis is the process of drawing meaning from text by analyzing its grammatical structure and identifying relationships between individual words in a particular context
#
#
#
### COMPARING FILES
# Beatles biographies

import os
from scipy.stats import fisher_exact
### Getting Filenames from a Directory

# Make a variable for your "source directory" (sdir)
sdir = "BeatleTexts"

# Get filenames
files = os.listdir(sdir)

# To make sure we only have files with correct extension

files = [i for i in files if i.endswith('.txt')]

# create full path versions of our filenames for later

files = [os.path.join(sdir, f) for f in files]

# test files print
# print(files)
# output = ['BeatleTexts\\George_Harrison.txt', 'BeatleTexts\\John_Lennon.txt', 'BeatleTexts\\Paul_McCartney.txt', 'BeatleTexts\\Ringo_Starr.txt']

# open a file and returns a list of words 

def file2words(somefilename, clean=True):
    with open(somefilename, encoding="utf-8") as source:
        text = source.read()
    words = text.split()
    if clean:
        words = [alphaclean(w) for w in words]
    return words

# clean the words
def alphaclean(someword):
    chars = [i for i in someword if i.isalpha()]
    cleanword = ' '.join(chars)
    cleanword = cleanword.lower()
    return cleanword

# # count the words
counts = {}

for w in words:
    w = alphaclean(w)
    if w not in counts:
        counts[w] = 0
    counts[w] += 1

# see what the word count of each file is
# wc = word count

wcs = {}

for f in files:
    words = file2words(f)
    wc = len(words)
    wcs[f] = wc

#print(wcs)

    #output 
    # {'BeatleTexts\\George_Harrison.txt': 11140, 
    # 'BeatleTexts\\John_Lennon.txt': 12598, 
    # 'BeatleTexts\\Paul_McCartney.txt': 14254, 
    # 'BeatleTexts\\Ringo_Starr.txt': 9696}

# count target word in our files
target_word = 'song'

for f in files:
    words = file2words(f)
    #print(words[:10])
    count = words.count(target_word)
    print(f,"\t",count)

# Looking for most distinctive words
# Collocations are words which are conventionally used together
# Stop words appear everywhere so frequent collocant
