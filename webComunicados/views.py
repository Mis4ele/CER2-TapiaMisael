from django.shortcuts import render

# Create your views here.

def index(request):
    title = "Comunicados"
    if request.method == 'POST':
        testing = request.POST.get('getlista')
    else:
        testing = 'nada'

    data = {
        "title": title,
        "testing": testing,
    }

    return render(request,'webComunicados/index.html', data)
