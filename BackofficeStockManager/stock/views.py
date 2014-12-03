from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from accounts.models import User
from stock.models import Stock
from stock.forms.newitem import NewItemForm

# Create your views here.
@login_required
def stock_index(request):
    if request.user.tyuser!='admin':
        return redirect('/')
    context={'stocks':Stock.objects.all()}
    template='stock.html'
    return render(request,template,context)

@login_required
def newproduct(request):
    if request.user.tyuser!='admin':
        return redirect('/')
    if request.method == 'POST':
        form=NewItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/stock/')
    form=NewItemForm()
    context={'form':form}
    template='newitem.html'
    return render(request,template,context)


@login_required
def upgrade(request,id):
    if request.user.tyuser!='admin':
        return redirect('/')
    if request.method == 'POST':
        instance = get_object_or_404(Stock, id=id)
        form = NewItemForm(request.POST or None,instance=instance)
        if form.is_valid():
            form.save() 
            return redirect('/stock/')
    intention=Stock.objects.get(pk=id)
    if intention:
        form=NewItemForm(instance=intention)
        context={'form':form}
        template='upgradeitem.html'
        return render(request,template,context)
    return redirect('/stock/')
    
