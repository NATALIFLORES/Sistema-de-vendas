from flask import Flask, jsonify, request,Blueprint
from produto_repository import ProdutoRepository
from produto import Produto

produto_bp = Blueprint("produtos",__name__)
repo = ProdutoRepository()
@produto_bp.route("/produtos",methods =['GET'])
def listar_produtos():
    repo = ProdutoRepository()
    dados = repo.find_all()

    cabecalhos = ["id","nome","descricao","preco","quanridadeEstoque","CategoriaID"]
    dados_retorno = [dict(zip(cabecalhos,d)) for d in dados]
    
    return jsonify(dados_retorno)

@produto_bp.route("/produtos/<int:produtoID>")
def buscar_id(produtoID):
    repo = ProdutoRepository()
    produto = repo.find_by_id(produtoID)
    produto_retorno = {"id":produto[0],"nome":produto[1],"desscricao":produto[2],"preco":produto[3],"quantidadeEstoque":produto[4],"CategoriaID":produto[5]}
    return jsonify(produto_retorno)

@produto_bp.route("/produtos",methods = ['POST'])
def cadastro_produto():
    repo = ProdutoRepository()

    dados_json = request.get_json()

    id = dados_json.get("id")
    nome = dados_json.get("nome")
    descricao = dados_json.get("descricao")
    preco = dados_json.get("preco")
    quantidadeEstoque = dados_json.get("quantidadeEstoque")
    CategoriaID = dados_json.get("CategoriaID")

    repo.create(nome,descricao,preco,quantidadeEstoque,CategoriaID)
    return jsonify({
        "mensagem":"Produto cadastrado com sucesso.",
        "nome":nome,
        "descricao":descricao,
        "preco":preco,
        "quantidadeEstoque":quantidadeEstoque,
        "CategoriaID":CategoriaID
    })

@produto_bp.route("/produtos/<int:id_produto>",methods = ['DELETE'])
def remover_produto(id_produto):
    repo = ProdutoRepository()
    repo.delete(id_produto)

    return jsonify({
        "mensagem":"Produto removido com sucesso."
})