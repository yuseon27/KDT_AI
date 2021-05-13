from django.shortcuts import render, HttpResponse
from .models import Coffee
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

def coffee_view(request) : #{
    coffee_all = Coffee.objects.all()   ## SELECT * FROM Coffee   ## .get(), .fiter(), .....
    return render(request, 'coffee.html', {"coffee_list":coffee_all})    
#}