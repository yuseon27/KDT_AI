from django.shortcuts import render, HttpResponse
'''
render : html 문서 관리 함수
render(request, '.html', {})

'''
# Create your views here.
def index(request) : #{
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'index.html', {})
#}