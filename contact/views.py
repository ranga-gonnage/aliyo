from django.shortcuts import render
from django.views import View

from contact.forms import ContactForm

class Contact(View):
    def get(self, request):
        context = {}
        return render(request, "contact.html", context)

    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
        	print("Coucou")
            # sender = Sender(contact_form)
            # sender.send_message_to_customer()
            # sender.send_message_to_manager()

        context = {}
        return render(request, "contact.html", context)