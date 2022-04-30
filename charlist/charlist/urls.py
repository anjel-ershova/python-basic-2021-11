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

urlpatterns = [
    path('create_personage/', personages.create_user),

    path('', pers_stats.index),  # как только добавляется новый эндпоинт, он должен быть прописан тут
    path('admin/', admin.site.urls),
]

# if DEBUG:
#     urlpatterns += path('__debug__/', include('debug_toolbar.urls'))