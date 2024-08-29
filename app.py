import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':'False'},
                {'nome':'Pizza Suprema','categoria':'Pizza','ativo':'True'},
                {'nome':'Cantina','categoria':'Italian','ativo':'False'}]

def exibir_nome_do_programa():
    """Essa função é responsávle por exibir o nome da aplicação"""
    print("""
░█████╗░██████╗░████████╗░██████╗████████╗███████╗░█████╗░██╗░░██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║░░██║
███████║██████╔╝░░░██║░░░╚█████╗░░░░██║░░░█████╗░░██║░░╚═╝███████║
██╔══██║██╔══██╗░░░██║░░░░╚═══██╗░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
██║░░██║██║░░██║░░░██║░░░██████╔╝░░░██║░░░███████╗╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝
""")

def exibir_opcoes():
    """Essa função é responsável por exibir os menus"""
    print("1. Cadastrar Jogo")
    print("2. Listar Jogos")
    print("3. Alternar estado do jogo")
    print("4. Sair\n")

def finalizar_app():
    """Essa função é responsável por encerra o aplicativo"""
    exibir_subtitulo("Finalizar app")

def voltar_ao_menu_principal():
    """Essa função é responsável por voltar a tela principal após teclar qualquer caractere + Enter
    
    Inputs:
    - Qualquer tecla para sair
    
    Outputs:
    - Executa a função main() para voltar a tela principal

    """
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    """Essa função é responsável por sinalizar ao usuário que a opção escohida é inválida e retorna a tela principal"""
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """Essa função cria um padrão de exibição para os títulos do menu escolhido"""
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adicona um novo restaurante na lista de restaurantes
    """
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Essa função é responsável por listar os restaurantes cadastrados"""
    exibir_subtitulo("Listando restaurantes")
    
    print(f"{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = "ativado" if restaurante['ativo'] else "desativado"
        print(f" - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def altenar_estado_restaurante():
    """Essa função é responsável por alterar o estado/status do restaurante (ativado/desativado)
    
    Inputs:
    - Necessário digitar o nome do restaurante cadastrar para alternar o status

    Outputs:
    - O usuário é sinalizado que o restaurante foi ativado ou desativado
    
    """
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante['ativo'] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()


def escolher_opcao():
    """Essa função é responsável por permitir a seleção do menu"""
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            altenar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """Essa função reseta o programa para tela principal, exibindo o nome e os menus"""
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()