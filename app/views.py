from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.

# def insert_topic(request):
#     tn=input('enter topic name :')
#     to=topic.objects.get_or_create(topic_name=tn)[0]
#     to.save()
#     return HttpResponse('data is inserted')
# def insert_webpage(request):
#     tn=input('enter topic name :')
#     to=topic.objects.get_or_create(topic_name=tn)[0]
#     to.save()
#     n=input('enter name :')
#     u=input('enter url :')
#     wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
#     wo.save()
#     return HttpResponse('data is inserted')
# def insert_ar(request):
#     tn=input('enter topic name :')
#     to=topic.objects.get_or_create(topic_name=tn)[0]
#     to.save()
#     n=input('enter name :')
#     u=input('enter url :')
#     wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
#     wo.save()
#     d=input('enter date :')
#     a=input('enter author name :')
#     e=input('enter email :')
#     ao=accessrecords.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
#     ao.save()
#     return HttpResponse('data inserted')

def display_topic(request):
    qsto=topic.objects.all()
    # qsto=topic.objects.filter(topic_name__startswith='v')
    # qsto=topic.objects.filter(topic_name__endswith='l')
    d={'qsto':qsto}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    qswo=webpage.objects.filter(topic_name='cricket').order_by('-name')
    # qswo=webpage.objects.exclude(topic_name='cricket').order_by('-name')
    qswo=webpage.objects.all().order_by(Length('name').desc())
    d={'qswo':qswo}
    return render(request,'display_webpage.html',d)

def display_access(request):
    qsao=accessrecords.objects.all()
    d={'qsao':qsao}
    return render(request,'display_access.html',d)

def insert_topic(request):
    tn=input('enter topic name:')
    to=topic.objects.get(topic_name=tn)
    qsto=topic.objects.all()
    d={'qsto':qsto}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    tn=input('enter topic name:')
    n=input('enter name:')
    ur=input('enter url')
    to=topic.objects.get(topic_name=tn)

    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=ur)[0]
    wo.save()
    qswo=webpage.objects.all()
    d={'qswo':qswo}
    return render(request,'display_webpage.html',d)

def insert_ar(request):
    pk=input('enter primary key :')
    d=input('enter date :')
    a=input('enter author name :')
    e=input('enter email :')
    wo=webpage.objects.get(pk=pk)
    ao=accessrecords.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()

    qsao=accessrecords.objects.all()
    d={'qsao':qsao}
    return render(request,'display_access.html',d)

