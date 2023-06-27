from django.shortcuts import *

from .forms import ClovekForm
from .models import clovek

def index(request):
    lidi = clovek.objects.all()
    return render(request, 'index.html', {'lidi': lidi})

def detail(request,pk):
    osoba = get_object_or_404(clovek, pk=pk)
    return render(request,'detail.html', {'osoba': osoba})

def create(request):
    if request.method == 'POST':
        form = ClovekForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('index')
    else:
        form = ClovekForm()
    return render(request, 'create.html', {'form': form})
