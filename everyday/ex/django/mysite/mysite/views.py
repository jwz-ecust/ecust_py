from django.shortcuts import render
from datetime import datetime

def hello(request):
    return render(request,'hello_world.html',{'current_time':datetime.now(),})