from django.views import View
from django.http import HttpResponseRedirect
from .models import Newsletter
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import threading


# Multi-threading
class EmailThread(threading.Thread):
    def __init__(self, msg):
        self.email = msg
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class NewsletterPage(View):

    template_name = 'newsletter/newsletterPage.html'

    def send_email(self, subject, from_email, to_email):
        # TODO: make use of dynamic content
        text_content = render_to_string(
            'email-templates/account_creation_info.txt', 
        )
        html_content = render_to_string(
            'email-templates/account_creation_info.html', 
        )
        msg = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=to_email)
        msg.attach_alternative(html_content, "text/html")
        EmailThread(msg).start()

    def get_subscribed_emails(self):
        return Newsletter.objects.all()

    def get(self, request):
        subscribed_emails = self.get_subscribed_emails()
        context = {
            'subscribed_emails': subscribed_emails
        }
        return render(request, self.template_name , context=context)
    
    def post(self, request):
        # Handle post-data
        email_addresses=request.POST.get('recipient')
        if email_addresses:
            email_list = [email.strip() for email in email_addresses.split(',')] # split on comma & then strip the leading & trailing whitespaces
        print("email_list:", email_list)
        subject=request.POST.get('subject')
        text_message=request.POST.get('email-body')
        # Send email
        from_mail = "python4dia@gmail.com"
        self.send_email(subject=subject, from_email=from_mail, to_email=email_list)
        # Render the newsletter page
        subscribed_emails = self.get_subscribed_emails()
        context = {
            'subscribed_emails': subscribed_emails
        }
        return render(request, self.template_name , context=context)

class newsletterSubscription(View):

    def post(self, request):
        # TODO: Check for existing subscribed-email before adding same email
        Newsletter.objects.create(email=request.POST.get('email'))
        referer_url = request.META.get('HTTP_REFERER')
        if referer_url:
            messages.success(request, "Thank you for subscribing to our newsletter")
            return HttpResponseRedirect(referer_url)
        else:
            return HttpResponseRedirect('/')

