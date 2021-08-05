from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404

from .models import contractContent
from .forms import contractContentForm

app_name = 'portfolio_app'

'''
from .models import 
from .forms import 
'''
def home(request):
    if request.method == 'POST':
        form = contractContentForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'successfully!!')
        else:
            messages.success(request, 'eror !!')

    redirect(home)
            

    contrac_form = contractContentForm()

    contex = {
        'key': 'value',
        'contrac_form': contrac_form,
    }
    return render(request, 'home.html', contex)



def about(request):
    contex = {
        'key': 'value',
    }
    return render(request, 'about.html', contex)


def all_commentsFV(request):
    header = 'All-Comments'

    try:
        all_comments = contractContent.objects.all()
    except contractContent.DoesNotExist:
        raise Http404("No MyModel matches the given query.")    
            
    contex = {
        'header' : header,
        'app_name': app_name,
        'all_comments': all_comments,
    }
    return render(request, 'comments.html', contex)