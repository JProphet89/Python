from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from biker.models import Biker
from biker.forms.newregister import NewItemForm
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
    context={'bikers': Biker.objects.all()}
    template='index.html'
    return render(request,template,context)


def newbiker(request):
    if request.method == 'POST':
        form=NewItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=NewItemForm()
    context={'form':form}
    template='newbiker.html'
    return render(request,template,context)

def bikerview(request,id):
	intention=Biker.objects.get(pk=id)
	if intention:
		context={
        	'biker':intention
        }
        template='bikerviews.html'
        return render(request,template,context)
