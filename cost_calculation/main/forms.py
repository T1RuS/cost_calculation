from django import forms


class CalculationForm(forms.Form):
    cost_work = forms.FloatField(help_text='100',
                                 label='Стоимость услуги',
                                 required=True, min_value=0.01)
    count_human = forms.IntegerField(help_text='2',
                                     label='Количество людей',
                                     required=True, min_value=1)
    count_task = forms.IntegerField(help_text='8',
                                    label='Количество услуг',
                                    required=True, min_value=1)
