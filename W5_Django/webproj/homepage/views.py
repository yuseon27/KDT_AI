from django.shortcuts import render, HttpResponse
'''
render : html 문서 관리 함수
render(request, '.html', {})

'''
# Create your views here.
def index(request) : #{
    # return HttpResponse("<h1>Hello World!</h1>")
    number = 50
    name   = 'Michael'
    nums   = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_num":number, "my_name":name, "my_list":nums})
#}