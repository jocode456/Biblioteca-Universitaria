import psycopg2

class LivroModel:
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

            sql = """
            SELECT l.id, l.titulo, l.ano_publicacao, a.nome 
            FROM livro l 
            JOIN autor a ON l.id_autor = a.id 
            ORDER BY l.id;
            """
            cursor.execute(sql)
            livros = cursor.fetchall()
            cursor.close()
            return livros
        except Exception as e:
            print(f"Erro SQL: {e}")
            return []

    def inserir(self, titulo, ano, id_autor):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES (%s, %s, %s);", (titulo, ano, id_autor))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            self.conexao.rollback()
            raise e

    def atualizar(self, id_livro, titulo, ano, id_autor):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE livro SET titulo = %s, ano_publicacao = %s, id_autor = %s WHERE id = %s;", (titulo, ano, id_autor, id_livro))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            self.conexao.rollback()
            raise e

    def excluir(self, id_livro):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM livro WHERE id = %s;", (id_livro,))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            self.conexao.rollback()
            raise e