from django.shortcuts import render
from .models import Produto, Categoria

def lista_produtos(request, categoria_id=None):
    categorias = Categoria.objects.all()

    if categoria_id:
        produtos = Produto.objects.filter(categoria_id=categoria_id, ativo=True)
    else:
        produtos = Produto.objects.filter(ativo=True)

    return render(request, 'index.html', {
    'categorias': categorias,
    'produtos': produtos,
    'categoria_ativa': categoria_id
})
    
from django.shortcuts import get_object_or_404

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    return render(request, 'produto.html', {
        'produto': produto
    })