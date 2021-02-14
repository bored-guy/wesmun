"""WesMun URL Configuration

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
from django.urls import path, re_path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('download/', download),
    path('hi_index/', hi_index),
    path('contact/', contact),
    path('tutorial/', tutorial),
    path('get_one/', get_one),
    path('yanzhengma/', yanzhegnma, name='yanzhengma'),
    path('wrong_yanzheng/', wrong_yanzheng),
    path('get_data_index/', get_data_index),
    path('team/', team),
    path('person/', person),
    path('get_data/', get_data),
    path('get_img/', get_img),
    path('get_test/', get_test),
    path('people/', people),
    path('information/', information),
    path('money/', money),
    path('only_one/',only_one),
    path('no_inform/',no_inform),
path('already_pic/',already_pic),
path('already_inform/',already_inform),
path('no_num/',no_num),
path('no_fenpei/',no_fenpei),
]
urlpatterns += staticfiles_urlpatterns()
