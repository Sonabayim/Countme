"""countme URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from .views import HomeView, get_data, ChartData
from profiles.views import UserLoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chart/$', HomeView.as_view(), name='home'),
    url(r'^$', UserLoginForm.as_view(), name='login'),    
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/$', ChartData.as_view()),
    # url(r'^$', MainView.as_view(), name='main'),


]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
