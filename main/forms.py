# файл forms.py

from django import forms
from .models import Report_view


class FilterForm(forms.Form):
    # Получаем список уникальных значений поля 'naimenovanie_strukturnogo_podrazdeleniya'
    choices_list = Report_view.objects.values_list('naimenovanie_strukturnogo_podrazdeleniya',
                                                   flat=True).distinct().order_by(
        'naimenovanie_strukturnogo_podrazdeleniya')
    # Преобразуем в список кортежей для ChoiceField
    choices = [(choice, choice) for choice in choices_list]

    naimenovanie_strukturnogo_podrazdeleniya = forms.ChoiceField(
        choices=[('', 'Выберите подразделение')] + choices,
        label='Подразделение',
        required=False
    )
