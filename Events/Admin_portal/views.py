from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def dashboard(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def test(request):
    context = {'message': 'Alan',
               'ask': 'how are you ? '}
    template=loader.get_template('test.html')
    return HttpResponse(template.render(context, request))


# Create your views here.
