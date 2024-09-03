import os


jogos = [{'nome':'The Legend of Zelda','categoria':'Aventura','ativo':'False'},
         {'nome':'Super Mario Bros','categoria':'Plataforma','ativo':'True'},
         {'nome':'Minecraft','categoria':'Sandbox','ativo':'False'}]

def exibir_nome_do_programa():
    
    print("""
░█████╗░██████╗░░█████╗░░█████╗░██████╗░███████╗████████╗███████╗░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║░░██║
███████║██████╔╝██║░░╚═╝███████║██║░░██║█████╗░░░░░██║░░░█████╗░░██║░░╚═╝███████║
██╔══██║██╔══██╗██║░░██╗██╔══██║██║░░██║██╔══╝░░░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
██║░░██║██║░░██║╚█████╔╝██║░░██║██████╔╝███████╗░░░██║░░░███████╗╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝
""")

def exibir_opcoes():
    
    print("1. Cadastrar jogo")
    print("2. Listar jogos")
    print("3. Alternar estado do jogo")
    print("4. Sair\n")

def finalizar_app():
    
    exibir_subtitulo("Finalizar app")

def voltar_ao_menu_principal():
    
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_jogo():
    
    exibir_subtitulo("Cadastro de novos jogos")
    nome_do_jogo = input("Digite o nome do jogo que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do jogo {nome_do_jogo}: ")
    dados_do_jogo = {'nome':nome_do_jogo, 'categoria':categoria, 'ativo':False}
    jogos.append(dados_do_jogo)
    print(f"O jogo {nome_do_jogo} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_jogos():
    
    exibir_subtitulo("Listando jogos")
    
    print(f"{'Nome do jogo'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}")
    for jogo in jogos:
        nome_jogo = jogo['nome']
        categoria = jogo['categoria']
        ativo = "ativado" if jogo['ativo'] else "desativado"
        print(f" - {nome_jogo.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def alternar_estado_jogo():
    
    exibir_subtitulo('Alterando estado do jogo')
    nome_jogo = input("Digite o nome do jogo que deseja alterar o estado: ")
    jogo_encontrado = False

    for jogo in jogos:
        if nome_jogo == jogo['nome']:
            jogo_encontrado = True
            jogo['ativo'] = not jogo['ativo']
            mensagem = f"O jogo {nome_jogo} foi ativado com sucesso" if jogo['ativo'] else f"O jogo {nome_jogo} foi desativado com sucesso"
            print(mensagem)

    if not jogo_encontrado:
        print("O jogo não foi encontrado")

    voltar_ao_menu_principal()

def escolher_opcao():
    
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_novo_jogo()
        elif opcao_escolhida == 2:
            listar_jogos()
        elif opcao_escolhida == 3:
            alternar_estado_jogo()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
