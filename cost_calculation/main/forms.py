from django import forms


class CalculationForm(forms.Form):
    cost_work = forms.FloatField(label='Стоимость услуги',
                                 widget=forms.NumberInput(
                                     attrs={'placeholder': '100'}),
                                 required=True, min_value=1)
    count_human = forms.IntegerField(label='Количество людей',
                                     widget=forms.NumberInput(
                                         attrs={'placeholder': '2'}),
                                     required=True, min_value=1)
    count_task = forms.IntegerField(label='Количество услуг',
                                    widget=forms.NumberInput(
                                        attrs={'placeholder': '8'}),
                                    required=True, min_value=1)
