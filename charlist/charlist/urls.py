"""charlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from charlist.settings import DEBUG

import pers_stats.views as pers_stats
import personages.views as personages
import myauth.views as myauth

urlpatterns = [
    path('personage/', include('personages.urls', namespace='personages')),
    path('myauth/', include('myauth.urls', namespace='myauth')),
    path('all_personages/', personages.all_personages, name='all_personages'),

    path('', pers_stats.index, name='pers_stats_main'),  # как только добавляется новый эндпоинт, он должен быть прописан тут
    path('admin/', admin.site.urls),
]

# if DEBUG:
#     urlpatterns += path('__debug__/', include('debug_toolbar.urls'))