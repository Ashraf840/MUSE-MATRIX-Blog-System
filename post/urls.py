from django.urls import path
from . import views

app_name = 'postApp'

urlpatterns = [
    path('<int:id>/<str:slug>/', views.postDetail.as_view(), name='postDetail')
]