def menu_autor():
    print("\n--- Gerenciar Autor ---")
    print("1. Cadastrar autor")
    print("2. Listar autores")
    print("3. Atualizar autor")
    print("4. Excluir autor")
    print("5. Voltar ao menu principal")
    return input("Escolha uma opção: ")

def listar_autores_view(autores):
    print("\n=== Lista de Autores ===")
    if not autores:
        print("Nenhum autor encontrado.")
    else:
        for autor in autores:
            print(f"ID: {autor[0]} | Nome: {autor[1]} | Nacionalidade: {autor[2]}")

def solicitar_dados_autor():
    nome = input("Nome do Autor: ")
    nacionalidade = input("Nacionalidade: ")
    return nome, nacionalidade

def solicitar_id():
    try:
        return int(input("Informe o ID do autor: "))
    except ValueError:
        print("ID deve ser um número.")
        return None

def mensagem(texto):
    print(texto)