from django.shortcuts import render
from .models import destination

# Create your views here.

def index(request):
    dest1=destination()
    dest2=destination()
    dest3=destination()
    dest1.name='Mumbai'
    dest1.para='The City That Never Sleeps'
    dest1.img='destination_1.jpg'
    dest1.price=700
    dest2.name="Laddak"
    dest2.para='The City of Snow'
    dest2.img='destination_2.jpg'
    dest2.price=1000
    dest3.name='Kedarnath'
    dest3.para='The City of Shivaji'
    dest3.img='destination_3.jpg'
    dest3.price=900
    dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})
