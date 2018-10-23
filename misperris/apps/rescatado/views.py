from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.rescatado.forms import RescatadoForm
from apps.rescatado.models import Rescatado

# Create your views here.


def index(request):
    return render (request, 'rescatado/index.html')


"""class RescatadoCreate(CreateView):
    model = Rescatado
    form_class = RescatadoForm
    template_name = 'rescatado/rescatado_form.html'
    success_url = reverse_lazy('rescatado:index')"""


#se visualiza el form para crear un nuevo rescatado
def rescatado_view(request):
    if request.method == 'POST':
        form = RescatadoForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('rescatado_listar')
    else:
        form = RescatadoForm()
    return render(request, 'rescatado/rescatado_form.html', {'form':form})


def rescatado_list(request):
    rescatado = Rescatado.objects.all()
    contexto = {'rescatados':rescatado}
    return render(request, 'rescatado/rescatado_list.html', contexto)


def rescatado_edit(request, id_rescatado):
    rescatado = Rescatado.objects.get(id=id_rescatado)
    if request.method == 'GET':
        form = RescatadoForm(instance=rescatado)
    else:
        form = RescatadoForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('rescatado_listar')
    return render(request,'rescatado/rescatado_form.html',{'form':form})

def rescatado_delete(request, id_rescatado):
    rescatado = Rescatado.objects.get(id=id_rescatado)
    if request.method == 'POST':
        rescatado.delete()
        return redirect('rescatado_listar')
    return render(request,'rescatado/rescatado_delete.html', {'rescatado':rescatado})