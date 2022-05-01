from django.forms import ModelForm

from personages.models import Personage


class PersonageCreateForm(ModelForm):
    class Meta:
        model = Personage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name)
            # print(field)
            field.widget.attrs['class'] = 'model-form'