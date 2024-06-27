from django.shortcuts import redirect, render
from .models import Producto
from .forms import ProductoForm

def inicio(request):
    productos = Producto.objects.all()

    q = request.GET.get('q')
    filtro = request.GET.get('filtro')

    if q:
        productos = productos.filter(nombre__icontains=q)

    if filtro == 'precio':
        productos = productos.order_by('precio')
    elif filtro == 'cantidad':
        productos = productos.order_by('cantidad')

    context = {
        'productos': productos
    }

    return render(request, 'core/inicio.html', context)

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/lista_productos.html', {'productos': productos})

def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm()
    return render(request, 'core/registrar_producto.html', {'form': form})
