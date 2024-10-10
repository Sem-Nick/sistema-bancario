from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from .models import Cartao
from .forms import CartaoForm
from .forms import EmprestimoForm
from .models import Emprestimo
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string

Usuario = get_user_model()

# @login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

@login_required
def criar_clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')

    else:
        form = ClienteForm()
    return render(request, 'clientes/criar_clientes.html', {'form': form})

@login_required
def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/atualizar_cliente.html', {'form': form})

@login_required
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/deletar_cliente.html', {'cliente': cliente})

# @login_required
def exportar_clientes_pdf(request):
    # Buscando todos os usuários
    clientes = Cliente.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('clientes/clientes_pdf.html', {'clientes': clientes})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="clientes.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response

# @login_required
def exportar_cartao_pdf(request):
    # Buscando todos os usuários
    cartao = Cartao.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('cartoes/cartoes_pdf.html', {'cartao': cartao})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="clientes.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response

# @login_required
def listar_cartoes(request):
    cartoes = Cartao.objects.all()
    return render(request, 'cartoes/listar_cartoes.html', {'cartoes': cartoes})

@login_required
def solicitar_cartao(request):
    if request.method == "POST":
        form = CartaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cartoes')
    else:
        form = CartaoForm()
    return render(request, 'cartoes/solicitar_cartao.html', {'form': form})

@login_required
def solicitar_limite(request, id):
    cartao = get_object_or_404(Cartao, id=id)
    if request.method == "POST":
        form = CartaoForm(request.POST, instance=cartao)
        if form.is_valid():
            form.save()
            return redirect('listar_cartoes')
    else:
        form = CartaoForm(instance=cartao)
    return render(request, 'cartoes/solicitar_limite.html', {'form': form})

@login_required
def cancelar_cartao(request, id):
    cartao = get_object_or_404(Cartao, id=id)
    if request.method == "POST":
        cartao.delete()
        # Redireciona para a lista de pedidos
        return redirect('listar_cartoes')
    return render(request, 'cartoes/cancelar_cartao.html', {'cartoes': cartao})

def listar_emprestimo(request):
    emprestimo = Emprestimo.objects.all()
    return render(request, 'emprestimo/listar_emprestimo.html', {'emprestimo': emprestimo})

@login_required
def cancelar_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == "POST":
        emprestimo.delete()
        # Redireciona para a lista de pedidos
        return redirect('listar_emprestimo')
    return render(request, 'emprestimo/cancelar_emprestimo.html', {'emprestimo': emprestimo})

@login_required
def solicitar_emprestimo(request):
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_emprestimo')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimo/solicitar_emprestimo.html', {'form': form})