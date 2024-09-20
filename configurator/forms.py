from .models import AssemblerPC, CPU, GPU, Motherboard, RAM, StorageDrive, PowerSupply, CoolingSystem, Case
from django.forms import ModelForm, ModelChoiceField, ChoiceField


class ConfiguratorForm(ModelForm):

    # cpu = ModelChoiceField(queryset=CPU.objects.all(), label='Процессор', empty_label='Выберите процессор', required=False)
    # gpu = ModelChoiceField(queryset=GPU.objects.all(), label='Видеокарта', empty_label='Выберите видеокарту', required=False)
    # motherboard = ModelChoiceField(queryset=Motherboard.objects.all(), label='Материнская плата', empty_label='Выберите материнскую плату', required=False)
    # ram = ModelChoiceField(queryset=RAM.objects.all(), label='Оперативная память', empty_label='Выберите оперативную память', required=False)
    # storage_drive = ModelChoiceField(queryset=StorageDrive.objects.all(), label='Накопитель', empty_label='Выберите накопитель', required=False)
    # power_supply = ModelChoiceField(queryset=PowerSupply.objects.all(), label='Блок питания', empty_label='Выберите блок питания', required=False)
    # cooling_system = ModelChoiceField(queryset=CoolingSystem.objects.all(), label='Система охлаждения', empty_label='Выберите систему охлаждения', required=False)
    # case = ModelChoiceField(queryset=Case.objects.all(), label='Корпус', empty_label='Выберите корпус', required=False)

    class Meta:
        model = AssemblerPC
        fields = ['name', 'cpu', 'gpu', 'motherboard', 'ram', 'storage_drive', 'power_supply',
                  'cooling_system', 'case', 'price_all', 'user_score']
        labels = {
            'cpu': 'Процессор',
            'gpu': 'Видеокарта',
            'motherboard': 'Материнская плата',
            'ram': 'Оперативная память',
            'storage_drive': 'Накопитель',
            'power_supply': 'Блок питания',
            'cooling_system': 'Система охлаждения',
            'case': 'Корпус'
        }

    # def clean_model(self):
    #     model_list = self.cleaned_data['cpu', 'gpu', 'motherboard', 'ram', 'storage_drive', 'power_supply',
    #               'cooling_system', 'case']
    #     if len(model_list) < 3:
    #         raise ValueError('Для сохранения сборки выберите, как минимум, 3 комплектующие')
    #     return model_list