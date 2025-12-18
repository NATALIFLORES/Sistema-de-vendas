from flask import Flask, jsonify, request

from categoria_repository import CategoriaRepository

app = Flask(__name__)

@app.route("/ola",methods =['GET'])
def ola():
    return "minha primeira API"

@app.route("/clientes",methods = ['GET'])
def listar_cliente():
     dados = [{"nome":"Leandro"},{"nome":"Maria"},{"nome":"Silva"},{"nome":"Marta"}]
     return jsonify(dados)

@app.route("/categorias",methods =['GET'])
def listar_categorias():
    repo = CategoriaRepository()
    dados = repo.find_all()
    #categoria_dic = []
    #for d in dados:
     #   categoria_dic.append({"id":d[0],"nome":d[1],"descricao":d[2]})
    cabecalhos = ["id","nome","descricao"]
    dados_retorno = [dict(zip(cabecalhos,d)) for d in dados]
    """
    dados = [{"id":"1","nome":"Eletrônicos","descricao":"Produtos eletrônicos como celulares, computadores, etc."},
             {"id":"2","nome":"Roupas","descricao":"Vestuário masculino, feminino e infantil"},
             {"id":"3","nome":"Móveis","descricao":"Móveis para casa e escritório"},
             {"id":"4","nome":"Alimentos","descricao":"Produtos alimentícios e bebidas"}]
    """
    return jsonify(dados_retorno)

@app.route("/categorias/<int:categoriaID>")
def buscar_por_id(categoriaID):
    repo = CategoriaRepository()
    categoria = repo.find_by_id(categoriaID)
    categoria_retorno = {"id":categoria[0],"nome":categoria[1],"descricao":categoria[2]}
    return jsonify(categoria_retorno)

@app.route("/categorias",methods = ['POST'])
def cadastro_categoria():
    repo = CategoriaRepository()
    #recebendo os dados via protocolo POST http
    dados_json = request.get_json()

    #pegando os dados recebidos do json
    id = dados_json.get("id")
    nome = dados_json.get("nome")
    descricao = dados_json.get("descricao")

    #enviando para banco de dados
    repo.create(nome,descricao)
    return jsonify({
        "mensagem":"Categoria cadastrado com sucesso.",
        "nome":nome,
        "descricao":descricao
        })
@app.route("/categorias/<int:id_categoria>",methods=['DELETE'])
def remover_categoria(id_categoria):
    #objeto de conumicacao
    repo = CategoriaRepository()

    #removendo acategpria do banco de dados
    repo.delete(id_categoria)

    return jsonify({
        "mensagem":"Categoria removida com sucesso."
    })


if __name__=="__main__":
    app.run(debug=True, port = 5000)