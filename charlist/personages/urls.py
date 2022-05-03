from django.contrib import admin
from django.urls import path, include
from charlist.settings import DEBUG

import personages.views as personages

app_name = 'personages'

urlpatterns = [

    path('details/<int:pk>/', personages.PersonageDetailView.as_view(), name='details'),
    path('create/', personages.PersonageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', personages.PersonageUpdateView.as_view(), name='update'),

]