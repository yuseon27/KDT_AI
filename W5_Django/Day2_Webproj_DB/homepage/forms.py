from django import forms
from .models import Coffee  ## Model 호출

## ModelForm을 상속받는 CoffeeForm 생성, 입력 칸을 만들어줌
class CoffeeForm(forms.ModelForm) :   
    ## ModelForm과 Model을 연결
    class Meta :  
        model  = Coffee
        fields = ('name', 'price', 'is_ice')