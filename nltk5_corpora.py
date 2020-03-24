import nltk
print(nltk.__file__)



from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

sample=gutenberg.raw("bible-kjv.txt")
tok=sent_tokenize(sample)
print(tok[5:15])
