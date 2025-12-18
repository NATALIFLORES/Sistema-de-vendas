from conexao import Conexao

class ProdutoRepository:
    def __init__(self):
        self.conexao = Conexao()
        
    def find_all(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("SELECT ProdutoID as id, Nome as nome, Descricao as descricao, Preco as preco, QuantidadeEstoque as quantidadeEstoque, CategoriaID as CategoriaID FROM Produto ORDER BY produtoID")
        return cursor.fetchall()
    
    def find_by_id(self,produto_id):
        cursor = self.conexao.get_cursor()
        cursor.execute(
            "SELECT ProdutoID as id, Nome as nome, Descricao as descricao, Preco as preco, QuantidadeEstoque as quantidadeEstoque, CategoriaID as CategoriaID FROM Produto WHERE produtoID = %s",
            (produto_id,)
        )
        return cursor.fetchone()
    
    def create(self,nome, descricao="",preco = 0.0,quantidadeEstoque = 0,CategoriaID= None):

         cursor = None
         try:
             cursor = self.conexao.get_cursor()
             cursor.execute(
                "INSERT INTO Produto(Nome,descricao,Preco,QuantidadeEstoque,CategoriaID)" \
                "VALUES (%s,%s,%s,%s,%s)",(nome,descricao,preco,quantidadeEstoque,CategoriaID)
            )
             self.conexao.get_conexao().commit()
             return cursor.lastrowid
         except Exception as e :
             print(f"Erro ao criar produto: {e}")
             self.conexao.get_conexao().rollback()
             return None
         finally:
             if cursor:
                 cursor.close()

    def update(self,produto_id,nome,descricao="",preco=0.0,quantidadeEstoque=0,CategoriaID=None):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "UPDATE Produto SET Nome = %s,descricao = %s,preco =%s,quantidadeEstoque = %s,CategoriaID =%s WHERE ProdutoID = %s",
                (nome,descricao,preco,quantidadeEstoque,CategoriaID)
            )
            self.conexao.get_conexao().commit()
            return cursor.rowcount >0
        except Exception as e:
            print(f"Erro ao atualizar Produto {produto_id}: {e}")
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def delete(self,poduto_id):

        cursor = None
        try:
            cursor=self.conexao.get_cursor()
            cursor.execute(
                "DELETE FROM Produto WHERE ProdutoID = %s",(poduto_id,)
            )
            self.conexao.get_conexao().commit()
            return cursor.rowcount >0
        except Exception as e:
            print(f"Erro ao deletar o Produto {poduto_id}: {e}")
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()