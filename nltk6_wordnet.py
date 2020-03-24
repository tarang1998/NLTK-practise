from nltk.corpus import wordnet

syns=wordnet.synsets("program")

#synset
print(syns)
print(syns[0].name())
#??
print(syns[0].lemmas())
print(syns[1].lemmas())
print(syns[2].lemmas())
print(syns[0].lemmas()[0].name())

#definition
print(syns[0].definition())

#examples
print(syns[0].examples())

synonyms=[]
antonyms=[]
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        print("lemmas:",l)
        synonyms.append(l.name())
        if l.antonyms():
            print("antonyms:",l.antonyms())
            antonyms.append(l.antonyms()[0].name())


print("synonyms:",set(synonyms))
print("anonyms:",set(antonyms))



w1=wordnet.synset("ship.n.01")
w2=wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))
