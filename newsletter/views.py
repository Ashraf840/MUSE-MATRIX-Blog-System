from django.views import View
from django.http import HttpResponseRedirect
from .models import Newsletter
from django.contrib import messages

class NewsletterPage(View):

    def get(self, request):
        pass

class newsletterSubscription(View):

    def post(self, request):
        Newsletter.objects.create(email=request.POST.get('email'))
        referer_url = request.META.get('HTTP_REFERER')
        if referer_url:
            messages.success(request, "Thank you for subscribing to our newsletter")
            return HttpResponseRedirect(referer_url)
        else:
            return HttpResponseRedirect('/')

