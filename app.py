import os

def mostra_titulo():
    print("""


    ▄▀█ █▀█ ▀█▀ ▀█▀ █▀▀ █▀▀ █░█
    █▀█ █▀▄ ░█░ ░█░ ██▄ █▄▄ █▀█
    """)

def mostra_escolhas():
    print("1. Cadastrar Artista")
    print("2. Listar Projetos")
    print("3. Ativar Publicação")
    print("4. Sair\n")

def escolhe_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))

    def finaliza_programa():
        os.system("cls")
        print("Finalizando o programa\n")

    def opcao_invalida():
        print("Esse caracter não e permitido\n")
        input("Aperte qualquer tecla para voltar")
        main()
    try:
            opcao_escolhida = int(input("Escolha uma opção: "))

            if opcao_escolhida == 1:
                print("Você escolheu Cadastrar Artista.")
            elif opcao_escolhida == 2:
                print("Você escolheu Listar seus projetos.")
            elif opcao_escolhida == 3:
                print("Você escolheu Ativar sua publicação.")
            elif opcao_escolhida == 4:
                finaliza_programa()
            else:
                opcao_invalida()
    except:
     opcao_invalida()

    def main():
        mostra_titulo()
        mostra_escolhas()
        escolhe_opcao()

    if__name__ == "__main__"
    main()

