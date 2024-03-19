from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include(('post.urls', 'app_name'), namespace='PostApplication')),
    path('newsletter/', include(('newsletter.urls', 'app_name'), namespace='NewsletterApplication')),
    path('', views.homePage.as_view(), name="HomepageApplication"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
