from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Hello')


def eggs(request):
    return HttpResponse('<h1>Eggs are great!<h1>')


def homepage(request):
    return render(request, 'home.html', {'hithere': 'This is Jade!'})


def wordcount(request):
    return render(request, 'word.html')


def count(request):
    my_text = request.GET['fulltext']
    # print(my_text)
    wordlist = my_text.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    return render(request, 'count.html', {'my_text': my_text, 'word_count': len(wordlist), 'worddictionary': worddictionary})