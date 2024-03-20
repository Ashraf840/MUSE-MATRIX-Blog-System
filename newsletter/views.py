from django.views import View
from django.http import HttpResponseRedirect
from .models import Newsletter
from django.contrib import messages
from django.shortcuts import render

class NewsletterPage(View):

    def get(self, request):
        subscribed_emails = Newsletter.objects.all()
        context = {
            'subscribed_emails': subscribed_emails
        }
        return render(request, 'newsletter/newsletterPage.html', context=context)

class newsletterSubscription(View):

    def post(self, request):
        Newsletter.objects.create(email=request.POST.get('email'))
        referer_url = request.META.get('HTTP_REFERER')
        if referer_url:
            messages.success(request, "Thank you for subscribing to our newsletter")
            return HttpResponseRedirect(referer_url)
        else:
            return HttpResponseRedirect('/')

