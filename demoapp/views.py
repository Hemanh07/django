from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render (request,'content.html',{'name':'hemanth'.capitalize()})
def add(request):
    num_1=request.POST['number_1']
    num_2=request.POST['number_2']
    try:
        sum=int(num_1)+int(num_2)                           
    except:
        sum='sorry division by zero is not allowed'
    return render(request,'result.html',{'sum':sum})     