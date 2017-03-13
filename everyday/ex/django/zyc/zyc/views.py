from django.http import HttpResponse
from django.template import Context,Template
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime
def hello(request):
    return HttpResponse("Hello Wold, YicHen Zhang")


def my_home_page(request):
    return HttpResponse("Welcome to my homepage!")

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now%s.</body></html>" %now
    return HttpResponse(html)

def time(request,offset):
    offset = int(offset)
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(offset,dt)
    return HttpResponse(html)


def zhangjiawei(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date}}.</body></html>")
    c = Context({'current_date':now})
    html = t.render(c)
    return HttpResponse(html)


def cbb(request):
    now = datetime.datetime.now()
    t = get_template('Template')
    html = t.render(Context({'person_name':'zhangjiawei','company':'ECUST','ship_date':now,'itemlist':['a','v','b'],'ordered_warranty':True,}))
    return HttpResponse(html)


def zyc(request):
    now = datetime.datetime.now()
    dir = {'person_name':'zhangjiawei','company':'ECUST','ship_date':now,'itemlist':['a','v','b'],'ordered_warranty':True}
    return render_to_response('Template',dir)
