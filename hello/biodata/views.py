from django.shortcuts import render
from .forms import Biodataform

def biodata_form(request):
    if request.method == 'POST':
        form = Biodataform(request.POST)
        if form.is_valid():
            return render(request, 'display.html', {'data': form.cleaned_data})
    else:
        form = Biodataform()
    return render(request, 'form.html', {'form': form})