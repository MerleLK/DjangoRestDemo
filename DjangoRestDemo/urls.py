"""DjangoRestDemo URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from quickstart.urls import router
from simpleDemo.urls import simple_router
from apidemo.urls import api_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'/', include('snippets.urls')),
]
urlpatterns += [
    url(r'^my_auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
urlpatterns += router.urls
urlpatterns += simple_router.urls
urlpatterns += api_urls
print(urlpatterns)
