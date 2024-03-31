from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Toukou

# Create your views here.

def index(request):
    template = loader.get_template("top.html")
    return HttpResponse(template.render({}, request))

def index2(request):
    toukou = Toukou.objects.all()
    context = {'toukou': toukou}
    template = loader.get_template("itiran.html")
    return HttpResponse(template.render(context, request))

def index3(request):
    template = loader.get_template("touroku.html")
    return HttpResponse(template.render({}, request))

def index4(request):
    template = loader.get_template("toukou.html")
    return HttpResponse(template.render({}, request))

def index5(request):
    toukou_list = Toukou.objects.all()
    return render(
        request, 
        'blog/index5.html',
        {'toukou_list': toukou_list})

def post(request):
    title = request.POST['title']
    bun = request.POST['bun']
    toukou = Toukou(title = title, bun = bun)
    toukou.save()
    return HttpResponseRedirect(reverse('blog:index5'))
    
    