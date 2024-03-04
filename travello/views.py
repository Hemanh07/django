from django.shortcuts import render
from .models import Destinatiion
# Create your views here.
def travel(request):

    dest1= Destinatiion()
    dest2= Destinatiion()
    dest3= Destinatiion()
    
    destination_list= Destinatiion.objects.all()
    #dest1.name='Bali'
    return render (request,'index.html',{'destinations':destination_list})