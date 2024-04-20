import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True}, 
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nome_do_programa():
    """ Exibe o título estlizado do programa"""
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    """ Exibe quais são as opções para o usuário"""
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    """ Finaliza a execução do programa"""
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    """ Permite voltar para o menu

    Outputs:
    - Executa o programa novamente para voltar ao menu principal
    """
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    """ Caso a opção seja inválida
    
    Ouputs:
    - Retornar ao menu principal(função)
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """ Essa função exibe os subtítulos da opção escolhida

    Inputs: 
    - Texto do subtítulo
    """

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do restaurante 
    - Categoria do restaurante

    Outputs: 
    - Adiciona um novo restaurante na lista de restaurantes
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restuarante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restuarante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    """ Exibe ao usuário uma lista dos restaurantes e suas informações
    
    Outputs:
    - Lista os restaurantes na tela
    """
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Staus')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        catergoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {catergoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()
    
def alternar_estado_restaurante():
    """ Alterna de ativado para desativado ou de desativado para ativado
    
    Output:
    - Alterna o restaurante e exibe mensagem do sucesso da operação
    """
    exibir_subtitulo('Alternando Estado do restaurante')
    nome_restaurante =  input('Dgite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrando = False

    for restaurante in restaurantes:
        if nome_restaurante ==  restaurante['nome']:
            restaurante_encontrando = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrando:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    """ Permite o usuário escolher a opção
    
    Inputs:
    - Qual será a opção

    Outputs:
    - Executa a opção escolhida
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
       opcao_invalida() 

def main():
    """ Todo o funcionamento do programa"""
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
