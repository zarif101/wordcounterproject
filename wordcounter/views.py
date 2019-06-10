from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def badword(request):
    return HttpResponse('You should not be saying that little boy')

def count(request):
    usertext = request.GET['usertext']
    thewords = usertext.split()
    thelength = str(len(thewords))
    worddictionary = {}
    for word in thewords:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=len, reverse=False)
    print(sortedwords)

    return render(request, 'count.html', {'usertext':usertext,'thelength':thelength, 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
