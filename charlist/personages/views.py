from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from personages.models import Personage

from personages.forms import PersonageCreateForm


@login_required
def all_personages(request):
    all_personages = Personage.objects.all()

    context = {
        'all_personages': all_personages,
    }

    return render(request, 'personages/all_personages.html', context=context)

# вариант FBV - Function Detailed View
# def personage_details(request, pk):
#     get_personage_details = get_object_or_404(Personage, pk=pk)
#
#     context = {
#         'page_title': 'Detail title',
#         'personage': get_personage_details, # контекст следует называть четко по имени класса
#     }
#
#     return render(request, 'personages/personage_detail.html', context=context)


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


# вариант CBV - Class Detail View
class PersonageDetailView(PageTitleMixin, DetailView):
    # template_name = 'personages/personage_detail.html'  # автоматически вычисляется из имя класса + _detail
    model = Personage
    page_title = 'Personage detail'
    # pk_url_kwarg = 'pk' # нужно, если как primary key используется не 'pk' или 'slug'
    # context_object_name = 'personage_details' # можно переопределять, если нужен кастом,
                                                # но если не определено, за контекст берется имя класса


# @login_required # ERROR
# @permission_required('personages.add_personage')
# @user_passes_test(lambda u: u.is_superuser)
# class PersonageCreateView(LoginRequiredMixin, CreateView):
# class PersonageCreateView(PermissionRequiredMixin, CreateView):
class PersonageCreateView(UserPassesTestMixin, CreateView):
    # permission_required = 'personages.add_personage'  # для PermissionRequiredMixin
    model = Personage
    success_url = reverse_lazy('all_personages') #  обязательный параметр
    form_class = PersonageCreateForm
    # fields = '__all__'  #  обязательный параметр либо он, либо form_class

    def test_func(self):
        print(self.request.user)
        return self.request.user.is_superuser
        # if self.request.user.is_anonimous:  # ERROR не срабатывает
        #     print('Login to create')

    # все проверки на права делать на уровне вьюх


class PersonageUpdateView(UpdateView):
    model = Personage
    success_url = reverse_lazy('all_personages')
    fields = '__all__'
