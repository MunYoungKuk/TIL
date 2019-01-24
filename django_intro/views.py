#python manage.py runserver $IP:$PORT 장고서버 실행
from django.http import HttpResponse
from django.shortcuts import render
import random

def index(request):
    return HttpResponse("hello!!")
    
def html_tag(request):
    s = "<h1>안녕하세요!!</h1>"
    return HttpResponse(s)
    
def dinner(request):
    return HttpResponse(random.choice(["중식",'일식','한식','양식']))
    
def lotto(request):
    return HttpResponse(random.sample(range(1,46),6))
    
def html_file(request):
    return render(request,"html_file.html")