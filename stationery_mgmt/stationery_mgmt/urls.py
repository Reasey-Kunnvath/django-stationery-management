from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin1/', admin.site.urls),
    path("admin/", include('login.login_urls')),
]
