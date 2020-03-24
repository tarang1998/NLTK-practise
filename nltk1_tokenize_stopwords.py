#import nltk
#nltk.download()

from nltk import sent_tokenize,word_tokenize
from nltk.corpus import stopwords


example_text="Hello Mr. Tarang, how are you? The weather is awesome today. I am awesome"

print(sent_tokenize(example_text))

words=word_tokenize(example_text)
print(words)



stop_words=set(stopwords.words("English"))
#print(stop_words)

filtered_words=[w for w in words if not w in stop_words]
print(filtered_words)


