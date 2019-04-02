"""myfirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from music import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/$', views.IndexView.as_view(), name='index'),
    url(r'^music/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^music/album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^music/album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'^music/album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^register/$', views.UserFormView.as_view(), name='register')


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
