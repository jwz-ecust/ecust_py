from django.shortcuts import render
from zjw.models import zjw
# Create your views here.

def lastest_zjw(request):
    zjw_list = zjw.objects.order_by('-id')
    return render(request,'zjw.html',{'zjw_list':zjw_list})