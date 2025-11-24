from controller.autor_controller import AutorController
from controller.livro_controller import LivroController
from view.menu_view import menu_principal

def main():
    autor_controller = AutorController()
    livro_controller = LivroController()

    while True:
        opcao = menu_principal()
        
        if opcao == "1":
            autor_controller.iniciar()
        elif opcao == "2":
            livro_controller.iniciar()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()