#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import ADR

def index(request):
    latest_adr_list = ADR.objects.order_by('-createdAt')[:5]
    template = loader.get_template('adr_ui/index.html')
    context = {
        'latest_adr_list' : latest_adr_list,
    }
    #output = ', '.join([q.decision for q in latest_adr_list])
    #return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def adr_detail(request, adr_id):
    response = "You're looking at the ADR %s."
    return HttpResponse(response % adr_id)

def new_adr(request):
    response = "You're posting new ADR."
    return HttpResponse(response)