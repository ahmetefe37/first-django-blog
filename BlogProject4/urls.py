"""BlogProject4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home_app.views import home_view
from aboutme_app.views import aboutme_view
from contactme_app.views import contactme_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name="home_url"),
    path("aboutme/", aboutme_view, name="aboutme_url"),
    path("contactme/", contactme_view, name="contactme_url"),
    path("post/", include("post_app.urls")),
    path("accounts/",include("accounts.urls"),name="accoutns_url"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
