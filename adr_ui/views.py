#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from .models import ADR, Status, InfluenceADR
from .forms import ADRForm

from .directions import *

from django.views.generic import ListView

# def index(request):
#     latest_adr_list = ADR.objects.order_by('-adrCreatedAt')[:5]
#     template = loader.get_template('adr_ui/index.html')
#     context = {
#         'latest_adr_list' : latest_adr_list,
#     }
#     #output = ', '.join([q.decision for q in latest_adr_list])
#     #return HttpResponse(output)
#     return HttpResponse(template.render(context, request))
class ADRListView(ListView):
    latest_adr_list = ADR.objects.order_by('-adrCreatedAt')[:5]
    template_name = 'adr_ui/index.html'
    model = ADR
    context = {
        'latest_adr_list' : latest_adr_list,
    }
    #output = ', '.join([q.decision for q in latest_adr_list])
    #return HttpResponse(output)
    #return HttpResponse(template_name.render(context, request))

def adr_detail(request, adr_id):
    response = "You're looking at the ADR %s."
    return HttpResponse(response % adr_id)

def get_adr(request, adr_id = None, template_name='adr_ui/new_adr.html'):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ADRForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
            form.save(commit=True)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        if adr_id:
            adr = get_object_or_404(ADR, pk=adr_id)
        else:
            adr = ADR()
        
        form = ADRForm(instance=adr)

    return render(request, template_name, {'form': form})

def gen_overview(request):
    pumlContent = render_to_string('adr_ui/puml_template.puml', { 'obj': ADR.objects.all(), 'legend': Status.objects.all(), 
                                                                  'influence': InfluenceADR.objects.all(), 
                                                                  'direction': directions['backward']})
    return HttpResponse(render_to_string('adr_ui/overview.html', { 'pumlContent': pumlContent }))
    #return render(request, 'adr_ui/overview.html')