from django.shortcuts import render, HttpResponse
from .models import Coffee
from .forms import CoffeeForm

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
    # 만약 request가 POST라면 :
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> DB에 저장!
    if request.method == "POST" :
        form = CoffeeForm(request.POST)  ## 새로운, 완성된 Form을 만들고
        if form.is_valid() :             ## 채워진 form 안에 있는 값이 유효한지 확인
            form.save()                  ## 이 Form을 Model에 저장


    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list":coffee_all, "coffee_form":form})    
#}