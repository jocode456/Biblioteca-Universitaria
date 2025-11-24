import psycopg2

class AutorModel:
    def __init__(self):
        try:
            
            self.conexao = psycopg2.connect(
                host="localhost",
                database="biblioteca_universitaria",
                user="postgres",
                password="admin"
            )
        except Exception as e:
            print("Erro ao conectar ao banco:", e)

    def listar(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome, nacionalidade FROM autor ORDER BY id;")
            autores = cursor.fetchall()
            cursor.close()
            return autores
        except Exception as e:
            return []

    def inserir(self, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s);", (nome, nacionalidade))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            self.conexao.rollback()
            raise e

    def atualizar(self, id_autor, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE autor SET nome = %s, nacionalidade = %s WHERE id = %s;", (nome, nacionalidade, id_autor))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            self.conexao.rollback()
            raise e

    def excluir(self, id_autor):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM autor WHERE id = %s;", (id_autor,))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            self.conexao.rollback()
            raise e