from django.contrib import admin
from django.urls import path, include
from charlist.settings import DEBUG

import pers_stats.views as pers_stats
import personages.views as personages

app_name = 'personages'

urlpatterns = [

    path('details/<int:pk>/', personages.PersonageDetailView.as_view(), name='details'),
    path('create/', personages.PersonageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', personages.PersonageUpdateView.as_view(), name='update'),

    path('', pers_stats.index, name='pers_stats_main'),  # как только добавляется новый эндпоинт, он должен быть прописан тут
]