
from conexao import conector 

#Criando a tabela

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            categoria  TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER
            )

            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()

# criar_tabela()

#Adicionar produtos

def adicionar_produto(nome, categoria, preco, quantidade ):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastrar o produto {erro}")
        finally:
            cursor.close()
            conexao.commit()

# adicionar_produto("cuscuz", "flocao", 15.00, 30)

#Função Listar produtos

def listar_produtos():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar o produto {erro}")
            return[]
        finally:
            cursor.close
            conexao.close

# listar_produtos()

#Função atualizar produto

def atualizar_produtos(quantidade, id):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos  SET quantidade = %s WHERE id = %s",
                (quantidade, id)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar o produto {erro}")
        finally:
            cursor.close()
            conexao.close()

atualizar_produtos(25,1)