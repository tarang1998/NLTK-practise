import nltk
input1="List listed lists listing listings"

#normalize
words1=input1.lower().split(' ')
print(words1)

porter=nltk.PorterStemmer()
stemmed=[porter.stem(w) for w in words1]
print(stemmed)

#lemmatization
udhr=nltk.corpus.udhr.words('English-Latin1')
text1=udhr[:20]
print(text1)


stemmed=[porter.stem(w) for w in text1]
#word obtained after stemming are not valid words
print(stemmed)#Universal->univer  Declaration->declar

#lemmatization
WNlemma=nltk.WordNetLemmatizer()
words=[WNlemma.lemmatize(w) for w in text1]
print(words)# difference Rights->Rights rights->right


#tokenization
text1="People shoudn't eat anuthing before going to bed."
print(nltk.word_tokenize(text1))


#Sentence tokenization
text2="This is the first sentence. Second sentence. Third sentence? fourth"
print(nltk.sent_tokenize(text2))
