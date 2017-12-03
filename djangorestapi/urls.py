"""djangorestapi URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from rest_framework_swagger.views import get_swagger_view

from api.urls import router as api_router

schema_view = get_swagger_view(title='DjangoRest Quickstart')


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api-explorer/', login_required(schema_view)),

    url(r'api/', include(api_router.urls, namespace='api')),
]
