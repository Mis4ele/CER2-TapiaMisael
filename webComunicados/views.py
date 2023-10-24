from django.shortcuts import render
from .models import Entidad, Comunicado

# Create your views here.

def index(request):
    title = "Comunicados"
    Comunicados = Comunicado.objects.all().order_by('-fecha_publicacion')

    if request.method == 'POST':
        departamento = request.POST.get('formDepto')
    else:
        departamento = 'Todos los departamentos'

    data = {
        "title": title,
        "Comunicados": Comunicados,
        "Entidades": Entidad.objects.all(),
        "departamento": departamento,
    }

    return render(request,'webComunicados/index.html', data)
