import nltk
nltk.help.upenn_tagset('MD')

text1="Children shoudn't drink a sugery drink before bed."
text2=nltk.word_tokenize(text1)
print(text2)

print(nltk.pos_tag(text2))

# Parsing sentence structure
text2 = nltk.word_tokenize("Alice loves Bob")
grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'
""")

parser = nltk.ChartParser(grammar)
trees = parser.parse_all(text2)
for tree in trees:
    print(tree)

#ambiguity in parsing
text3=nltk.word_tokenize("I saw a man with a telescope")
#grammar=nltk.data.load("grammar.cfg")
grammar=nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | VP PP
PP -> P NP
NP -> DT N | DT N PP | 'I'
DT -> 'a' | 'the' 
N -> 'man' | 'telescope'
V -> 'saw'
P -> 'with'
""")
print(grammar)

parser=nltk.ChartParser(grammar)
trees=parser.parse_all(text3)
for tree in trees:
    print (tree)


#treebank
from nltk.corpus import treebank
text=treebank.parsed_sents('wsj_0001.mrg')[0]
print(text)





