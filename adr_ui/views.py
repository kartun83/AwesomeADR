#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from .models import ADR
from .forms import ADRForm

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

def get_adr(request, adr_id):
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
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ADRForm()

    return render(request, 'adr_ui/new_adr.html', {'form': form})