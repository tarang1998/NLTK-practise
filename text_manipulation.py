text1="Ethics are built right into the ideals and objectives of the UnitedNations "

#length of text
print(len(text1))

#splitting the text into words using split() function
#split(separator,no of times)--->by default separator--whitespace
t2=text1.split()
print(len(t2))
print(t2)



#to find specific words
#eg.words more than 3  characters long
t3=[w for w in t2 if len(w)>3]
print(t3)

#to find capitalized words(first letter is capitalized)
t3=[w for w in t2 if w.istitle()]
print(t3)

#words that end with 's'
print([w for w in t2 if w.endswith('s')])


#finding unique words with the set() func
t3="To be or not to be"
t4=t3.split()
print(len(t4))
print(len(set(t4)))
print(set(t4))
#set does not distinguish between "To" and "to"

#solution-->lower case all the words
print(set([w.lower() for w in t4]))


t5="ouagadougou"
t6=t5.split("ou")
print(t6)
#['','agad','g','']


t7='ou'.join(t6)
print(t7) #ouagadougou

print(list(t5))#[c for c in t5]

t8="    A quick brown fox jumped over the lazy dog "
print(t8.split(" "))


t8=t8.strip()
print(t8.split())

t9=" ".join(t8.split())
print(t9)

print(t9.find('o'))
print(t9.rfind('o'))

print(t9.replace("o","O"))


