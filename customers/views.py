from django.shortcuts import render
from .models import Customer
from services.models import Service
from django.http import HttpResponseRedirect
from forms import *


# Create your views here.

def customers(request):
	customers = Customer.objects.all()
	services = Service.objects.all()
	template = 'customers.html'
	return render(request,template,{"customers":customers,"services":services,"request":request})




def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = ContactForm(request.POST) # A form bound to the POST data
	if form.is_valid():
	    subject = form.cleaned_data['subject']
	    message = form.cleaned_data['message']
	    sender = form.cleaned_data['sender']
	    cc_myself = form.cleaned_data['cc_myself']

	    recipients = ['zack@hotmail.com']
	    if cc_myself:
	        recipients.append(sender)

	    from django.core.mail import send_mail
	    send_mail(subject, message, sender, recipients)
	    return HttpResponseRedirect('/thanks/') # Redirect after POST

        
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })

def thanks(request):
 	template ='thanks.html'
 	return render(request,template)

