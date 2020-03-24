import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()

eg_text='He listed down the words in a listly manner into the list so it could be used for the listing. Is this right?'
words=word_tokenize(eg_text)
print(words)

for w in words:
    print(ps.stem(w))

WNlemma=nltk.WordNetLemmatizer()
Lem=[WNlemma.lemmatize(t) for t in words]
print(Lem)
