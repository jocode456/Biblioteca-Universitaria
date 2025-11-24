from model.livro_model import LivroModel
from view.livro_view import *

class LivroController:
    def __init__(self):
        self.model = LivroModel()

    def iniciar(self):
        while True:
            opcao = menu_livro()
            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "5":
                break
            else:
                mensagem("Opção inválida.")

    def cadastrar(self):
        try:
            titulo, ano, id_autor = solicitar_dados_livro()
            if titulo and id_autor:
                self.model.inserir(titulo, ano, id_autor)
                mensagem("Livro cadastrado com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao cadastrar (Verifique se o ID do autor existe): {e}")

    def listar(self):
        livros = self.model.listar()
        listar_livros_view(livros)

    def atualizar(self):
        self.listar()
        id_livro = solicitar_id_livro()
        if id_livro:
            titulo, ano, id_autor = solicitar_dados_livro()
            try:
                self.model.atualizar(id_livro, titulo, ano, id_autor)
                mensagem("Livro atualizado!")
            except Exception as e:
                mensagem(f"Erro ao atualizar: {e}")

    def excluir(self):
        self.listar()
        id_livro = solicitar_id_livro()
        if id_livro:
            try:
                self.model.excluir(id_livro)
                mensagem("Livro excluído!")
            except Exception as e:
                mensagem(f"Erro ao excluir: {e}")