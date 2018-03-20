from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html'  )

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.replace('"','').replace(',','').lower().split()
    #print(wordlist)
    #countlist = []
    #wordset = set(wordlist)
    #print(wordset)
    # newlist = []
    worddictionary = {}
    for word in wordlist:
        # occurs = wordlist.count(word)
        # newlist.append((word,occurs))
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    #print(newlist)
    # -- worddictionary = dict(newlist)
    #print(worddictionary)

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    print(type(sortedwords))
    print(sortedwords)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':dict(sortedwords).items()})
