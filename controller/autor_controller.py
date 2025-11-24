from model.autor_model import AutorModel
from view.autor_view import *

class AutorController:
    def __init__(self):
        self.model = AutorModel()

    def iniciar(self):
        while True:
            opcao = menu_autor()
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
            nome, nacionalidade = solicitar_dados_autor()
            if nome:
                self.model.inserir(nome, nacionalidade)
                mensagem("Autor cadastrado com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao cadastrar: {e}")

    def listar(self):
        autores = self.model.listar()
        listar_autores_view(autores)

    def atualizar(self):
        self.listar() 
        id_autor = solicitar_id()
        if id_autor:
            nome, nacionalidade = solicitar_dados_autor()
            try:
                self.model.atualizar(id_autor, nome, nacionalidade)
                mensagem("Autor atualizado!")
            except Exception as e:
                mensagem(f"Erro ao atualizar: {e}")

    def excluir(self):
        self.listar()
        id_autor = solicitar_id()
        if id_autor:
            try:
                self.model.excluir(id_autor)
                mensagem("Autor excluído!")
            except Exception as e:
                mensagem(f"Erro ao excluir (O autor pode ter livros vinculados): {e}")