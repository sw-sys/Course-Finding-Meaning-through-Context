# NOTES from https://github.com/jdportercode/TAP23

sample = "The pig and the dog went out to play. They had a ball and a stick. It was snack time and they shared a chocolate bar. This is a good way to play"

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

# Takes a word and returns a cleaned up version of the word
def wordcleaner(someword):
    cleanword = someword.casefold()
    while cleanword and not cleanword[-1].isalnum():
        cleanword = cleanword[:-1]
    while not cleanword[0].isalnum():
        return cleanword

# print(wordcleaner(sample))

# count the words
counts = {}

cleanwords = [wordcleaner(w) for w in words]

for w in words:
    cleanwords.append(wordcleaner(w))