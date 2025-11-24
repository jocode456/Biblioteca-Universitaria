def menu_livro():
    print("\n--- Gerenciar Livro ---")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Atualizar livro")
    print("4. Excluir livro")
    print("5. Voltar ao menu principal")
    return input("Escolha uma opção: ")

def listar_livros_view(livros):
    print("\n=== Lista de Livros ===")
    if not livros:
        print("Nenhum livro encontrado.")
    else:
        
        for livro in livros:
            print(f"ID: {livro[0]} | Título: {livro[1]} | Ano: {livro[2]} | Autor: {livro[3]}")

def solicitar_dados_livro():
    titulo = input("Título do Livro: ")
    try:
        ano = int(input("Ano de Publicação: "))
        id_autor = int(input("ID do Autor: "))
        return titulo, ano, id_autor
    except ValueError:
        print("Ano e ID do autor devem ser números.")
        return None, None, None

def solicitar_id_livro():
    try:
        return int(input("Informe o ID do livro: "))
    except ValueError:
        print("ID deve ser um número.")
        return None

def mensagem(texto):
    print(texto)