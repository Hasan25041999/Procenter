from django.shortcuts import render,redirect
from home.models import *
from home.forms import *
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method=='POST':
        obj=CreateForm(request.POST)
        pro=EduForm(request.POST)
        if obj.is_valid():
            obj.save()
        if pro.is_valid():
            pro.save()
            return redirect('signup')
        else:
            return redirect('signup')
    else:
        obj=CreateForm()
        pro=EduForm()
        for x,y in zip(obj.fields.values(),pro.fields.values()):
            x.widget.attrs['class']='form-control'
            obj.fields['DOB'].widget=forms.DateInput(attrs={'class':'form-control','type' : 'date'})
            y.widget.attrs['class']='form-control'
            
            pro.fields['Year'].widget=forms.DateInput(attrs={'class':'form-control','type' : 'date'})

        return render(request,'signup.html',{'data':obj, 'pro':pro})
    