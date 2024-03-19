from django.urls import path
from . import views

app_name = 'newsletterApp'

urlpatterns = [
    path('subscription/', views.newsletterSubscription.as_view(), name='subscription'),
]