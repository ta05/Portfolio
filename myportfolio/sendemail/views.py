# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email'], 
                'message': form.cleaned_data['message'], 
			}
            message = body['message'] + "\n\n" + body['first_name'] + ' ' + body['last_name'] + "\n\n" + body['email'] 
            try:
                send_mail(subject, message, 'talimi2000@gmail.com', ['talimi2000@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "sendemail/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
