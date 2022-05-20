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
        cost_work = int(form.cleaned_data['cost_work'])
        count_task = int(form.cleaned_data['count_task'])
        count_human = int(form.cleaned_data['count_human'])
        context['cost'] = cost_work * count_human * count_task
        return render(request, template, context)
    return render(request, template, context)
