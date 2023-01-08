from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import members, person
from .forms import ContactForm
from django.core.mail import send_mail
from datetime import datetime
from django.template.loader import render_to_string

def about(request):
  mymembers = person.objects.all().values()
  template = loader.get_template('files/all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

   
# Create your views here.
def index(request):
    
    
    mymembers = person.objects.all().values()
    template = loader.get_template('files/index.html')
    context = {
    'person': mymembers,
  }
    return HttpResponse(template.render(context, request))
def about(request):
    
    
    mymembers = person.objects.all().values()
    template = loader.get_template('files/all_members.html')
    context = {
    'person': mymembers,
  }
    return HttpResponse(template.render(context, request))


def contact(request):
    if request.method == 'POST':    
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['contact']
            
            html = render_to_string('files/emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })
            
            
            
            send_mail('The Contact for subject', 'This is the message', 'lilbdawg10@gmail.com', ['blaize.ramsay@gmail.com'], html_message=html)
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index.html'))
    else:
        form = ContactForm()
    return render(request, 'files/contact.html', {
        'form': form
    })

