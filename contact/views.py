from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.contrib import messages

from contact.forms import ContactForm
from contact.sender import Sender

class Contact(View):
    def get(self, request):
        context = {}
        context["site_key"] = settings.RECAPTCHA_SITE_KEY
        return render(request, "contact.html", context)

    def post(self, request):
        data = request.POST
        contact_form = ContactForm(data)
        if contact_form.is_valid():
            sender = Sender(contact_form)
            if sender.is_recaptach_sucess(data):
                sender.send_message_to_customer()
                sender.send_message_to_manager()
                messages.success(request, 'Merci pour votre message, nous allons y répondre au plus vite !')

        context = {}
        context["site_key"] = settings.RECAPTCHA_SITE_KEY
        return render(request, "contact.html", context)

class About(View):
    def get(self, request):
        context = {}
        return render(request, "about.html", context)