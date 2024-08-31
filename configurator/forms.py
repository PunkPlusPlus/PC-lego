from .models import AssemblerPC
from django.forms import ModelForm, TextInput

class ConfiguratorForm(ModelForm):
    class Meta:
        model = AssemblerPC
        fields = ['name', 'cpu', 'gpu', 'motherboard', 'ram', 'storage_drive', 'power_supply',
                  'cooling_system', 'case', 'price_all', 'user_score']

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название сборки",
            }),
            'cpu': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Процессор",
            }),
            'gpu': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Видеокарта",
            }),
            'motherboard': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Материнская плата",
            }),
            'ram': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Оперативная память",
            }),
            'storage_drive': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Накопитель",
            }),
            'power_supply': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Блок питания",
            }),
            'cooling_system': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Система охлаждения",
            }),
            'case': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Корпус",
            }),
            'price_all': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Общая стоимость",
            }),
            'user_score': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Рейтинг",
            }),
        }