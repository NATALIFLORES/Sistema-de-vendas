class Produto:
    def __init__(self, ProdutoID=None, nome="", descricao ="", preco ="", quantidadeEstoque ="",CategoriaID=None):
        self.__ProdutoID = ProdutoID
        self.__nome = nome 
        self.__descricao = descricao
        self.__preco = preco 
        self.__quantidadeEstoque = quantidadeEstoque 
        self.__CategoriaID = CategoriaID

    @property
    def ProdutoID(self):
        return self.__ProdutoID
    
    @ProdutoID.setter
    def ProdutoID(self,valor):
        if valor is None or isinstance(valor, id):
            self.__ProdutoID = valor
        else:
            raise ValueError("ID deve ser inteiro ou None")
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__nome = valor.strip()
        else: 
            raise ValueError("Nome deve ser na forma de3 texto nao vazia(máx. 100 caracteres)")
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, valor):
        if isinstance(valor, str) and len(valor) <= 500:
            self.__descricao = valor.strip()
        else:
            raise ValueError("Descrição deve ser string (máx. 500 caracteres)")
    @property
    def preco(self):
        return self.__preco 
    @preco.setter
    def preco(self,valor):
        if isinstance(valor, (int, float)) and valor >= 0:
           self.__preco = valor
        else:
            raise ValueError("O preço este produto tem que ser maior ou igual a zero")
    @property
    def quantidadeEstoque(self):
        return self.__quantidadeEstoque
    @quantidadeEstoque.setter
    def quantidadeEstoque(self,quantidade):
        if isinstance(quantidade, int) and quantidade >= 0:
           self.__quantidadeEstoque = quantidade
        else:
            raise ValueError("Quantidade em estoque deve ser um inteiro ou igual á 0")
        
    @property
    def CategoriaID(self):
        return self.__CategoriaID
    
    @CategoriaID.setter
    def CategoriaID(self,valor):
        if valor is None or isinstance(valor, id):
            self.__CategoriaID = valor
        else:
            raise ValueError("ID deve ser inteiro ou None")