"""BlogApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
#for doc need

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#documentation yasg
schema_view =  get_schema_view(
    openapi.Info(
        title= 'Blogs Api',
        default_version= 'v1',
        description= 'A project to learn DRF',
        terms_of_service= 'www.google.com/policies/terms',
        contact= openapi.Contact(email="tsunil359@gmail.com"),
        license= openapi.License(name =  "RCX license"),
    ), 
    public = True,
    permission_classes = (permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blogs.urls') ),

    path('api-auth/', include('rest_framework.urls')),#login/ logout
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),#login logout pw reset pw reset confirm

    #all auth
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    #schema


  #now we dont need this:  path('openapi', get_schema_view(
      #  title = "Blogs Api",
      #  description =  "A simple API for learning DRF",
      #  version= "1.5.6",
    #), name = 'open-schema'),


    #docs
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout = 0), name = 'schema-swagger-ui'),

    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout = 0
    ), name = 'schema-redoc'),
]
