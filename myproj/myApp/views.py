from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from datetime import datetime
from myApp.models import Software
from django.contrib import messages

# Create your views here.
def hola_mundo(resquest):
    return HttpResponse(encabezado+"Quibo Felipe"+pie)

encabezado = """
<div style='background-color: rgb(130, 163, 163)'>
<h1>Django Web Framework</h1>
<hr>
<ul>
    <li><a href="/">Principal</a></li>
    <li><a href="/holaMundo">Hola Mundo</a></li>
</ul>
</div>
"""
pie = """
<div style='background-color: rgb(130, 163, 163); text-align: center;'>
<br>Derechos reservados
<br>By Felipe Duarte
</div>
"""

def principal(request):
    return render(request, 'principal.html')

def bienvenido(request, nombre = 'Julian', lugar= 'Halacho'):
    if nombre == "ninguno":
        return redirect('/')
    return HttpResponse(encabezado + f"Bienvenido {nombre} de {lugar}" + pie)

def web(request):
    fecha = datetime(2001,1,15)  
    return render(request,"web.html", 
                {'protocolo':'Protocolo de Transferencia de Hipertextos',
                'frontend':
                ['HTML','CSS','Js','Vue','React','Angular'],
                'backend':
                ['Js','Python','Java','.NET','PHP'],
                'autor':'Felipe',
                'fecha':fecha},
                )

def python(request):
    try:        
        #result = Software.objects.get(id=10)
        #result = Software.objects.get(nombre='Numpy')
        #result = Software.objects.get(define='Paquete usado en astronomía')nombre=’Pandas’
        #result = Software.objects.filter(nivel=2)
        #result = Software.objects.order_by('-nombre')[:5]
        result = Software.objects.all()
        paginar = Paginator(result,4)
        pagian = request.GET.get('pagina')
        mostrar = paginar.get_page(pagian)
        
        return render(request, 'python.html', {'sw':{mostrar}})
    except:
        return render(request, 'python.html',{'sw':{}})
    
def borrar_software(request, id):
    sw = Software.objects.get(pk=id)
    sw.delete()
    messages.success(request,f'Se elimino: {sw.nombre}')
    return redirect('/python')

def guardar_sw_get(request):
    if request.method == 'GET':
        sw = Software(
            nivel = request.GET['nivel'],
            nombre = request.GET['nombre'],
            define = request.GET['define'],
        )
        sw.save()
        messages.success(request,f'Se guardo: {sw.nombre}')
    else:
        messages.success(request,f'Error al enviar datos')
    return redirect('/python')


def guardar_sw_post(request):
    if request.method == 'POST':
        sw = Software(
            nivel = request.POST['nivel'],
            nombre = request.POST['nombre'],
            define = request.POST['define'],
        )
        sw.save()
        messages.success(request,f'Se guardo: {sw.nombre}')
    else:
        messages.success(request,f'Error al enviar datos')
    return redirect('/python')
