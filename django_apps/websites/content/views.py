from websites.content.models import *
from websites.content.forms import ContactForm, SubscribeForm, UserContactForm, UserForm
from websites.shopping.models import Item

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

#import oauth2 as oauth 
import cgi


@csrf_protect
def index(request):
    items = Item.objects.all().order_by('-id')[:6]
    return render_to_response("index.html", {
        'items': items
    }, RequestContext(request), )


@csrf_protect
def contact(request):
    if request.POST:
        c = ContactForm(request.POST, request.FILES)
        if c.is_valid():
            mail = EmailMessage(
                "Custom Order",
                "Email From: {0}\n".format(c.cleaned_data["email"]) + c.cleaned_data["description"],
                "noreply@illustrious-designs.com",
                [settings.EMAIL_ADDRESS]
            )

            image = request.FILES['image']

            mail.attach(image.name, image.read(), image.content_type)
            # send it
            mail.send()

            return HttpResponseRedirect("/")
        else:
            form = c
        print c.errors
    else:
        form = ContactForm()
    return render_to_response("contact.html", {'form': form, }, RequestContext(request), )


@csrf_protect
def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.POST:
        contact_form = UserContactForm(request.POST, request.FILES)
        register_form = UserForm(request.POST)
        if register_form.is_valid() and contact_form.is_valid():
            user = register_form.save(commit=False)
            user.save()
            contact = contact_form.save(commit=False)
            contact.user = user
            contact.save()
            return HttpResponseRedirect("/")
    else:
        contact_form = UserContactForm()
        register_form = UserForm()
    return render_to_response("register.html", {'contact_form': contact_form, 'user_form': register_form},
                              RequestContext(request), )
