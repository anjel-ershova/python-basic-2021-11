from django.urls import reverse_lazy
from django.views.generic import CreateView

from myauth.forms import CharlistUserCreateForm
from myauth.models import CharlistUser


class NewUserRegister(CreateView):
    model = CharlistUser
    success_url = reverse_lazy('all_personages')
    # success_url = '/' # должен быть реверс лейзи по хорошему
    form_class = CharlistUserCreateForm

