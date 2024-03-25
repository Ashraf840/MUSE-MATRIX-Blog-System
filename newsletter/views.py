from django.views import View
from django.http import HttpResponseRedirect
from .models import Newsletter
from django.contrib import messages
from django.shortcuts import render

class NewsletterPage(View):

    template_name = 'newsletter/newsletterPage.html'

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
        message=request.POST.get('email-body')
        # Send email
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

