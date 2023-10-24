from django.shortcuts import render
from .models import Entidad, Comunicado

# Create your views here.

def index(request):
    title = "SIN - Inicio"
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

def comunicado(request):
    title = "SIN - Comunicado"
    Comunicados = Comunicado.objects.all()
    idComunicado = request.GET.get('idComunicado')
    comunicado = "No se ha encontrado ese comunicado."

    for comu in Comunicados:
        if str(comu.id) == str(idComunicado):
            comunicado = comu
            break

    data = {
        "title": title,
        "comunicado": comunicado,
        "logo": '/'.join(str(comunicado.entidad.logo).split('/')[2:]),
    }

    return render(request,'webComunicados/comunicado.html', data)