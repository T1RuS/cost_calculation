from django.shortcuts import render
from django.http import JsonResponse

from .forms import CalculationForm


def index(request):
    template = 'main/index.html'
    form = CalculationForm(request.POST or None)
    cost = None
    context = {
        'form': form,
        'cost': cost,
    }

    if request.method == 'POST' and form.is_valid():
        cost = 1
        for num in form.cleaned_data.values():
            cost *= num

        text = f'Общая стоимость: {cost}'
        context['cost'] = cost
        # return JsonResponse(data={'text': text})

    return render(request, template, context)
