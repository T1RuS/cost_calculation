from django.shortcuts import render

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

        context['cost'] = cost

    return render(request, template, context)
