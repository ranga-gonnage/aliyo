from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage

import requests

class Sender:
    def __init__(self, contact_form):
        self.contact_form = contact_form

    def send_message_to_customer(self):
        email_from = "contact@aliyo.fr"
        email_to = self.contact_form.cleaned_data.get('email')
        context = {
            'name': self.contact_form.cleaned_data.get('name')
        }
        message = get_template('mails/customer_mail.html').render(context)
        self._send_mail(email_from, email_to, message, "Aliyo : Avis de réception")

    def send_message_to_manager(self):
        email_from = "contact@aliyo.fr"
        email_to = "contact@aliyo.fr"
        context = {
            'name': self.contact_form.cleaned_data.get('name'),
            'email' : self.contact_form.cleaned_data.get('email'),
            'message' : self.contact_form.cleaned_data.get('message')
        }
        message = get_template('mails/manager_mail.html').render(context)
        self._send_mail(email_from, email_to, message, "Aliyo : Demande d'informations")

    def is_recaptach_sucess(self, data):
        secret_key = settings.RECAPTCHA_SECRET_KEY
        print(data.get('g-recaptcha-response'))
        data = {
            'response': data.get('g-recaptcha-response'),
            'secret': secret_key
        }
        resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result_json = resp.json()
        print(result_json.get('success'))
        return result_json.get('success')

    def _send_mail(self, email_from, email_to, message, subject):
        msg = EmailMessage(
            subject,
            message,
            email_from,
            [email_to,],
        )
        msg.content_subtype ="html"
        msg.send()