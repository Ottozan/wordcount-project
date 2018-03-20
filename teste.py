fulltext = 'se eu digo pare voce nao repare no meu jeito mas se digo venha '+\
        'voce traz a lenha pro meu fogo acender'
wordlist = fulltext.split()
print(wordlist)
countlist = []
wordset = set(wordlist)
print(wordset)
newlist = []
for word in wordset:
    occurs = wordlist.count(word)
    newlist.append((word,occurs))
print(newlist)
worddictionary = dict(newlist)
sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
print(worddictionary)
# worddictionary.items = {newlist}
