'''# REGRAS CLÍNICA
1 - baseClinica só deverá ser acessada do arquivo controlador
2 - Clinica será um dicionário com as seguintes chaves: CNPJ, nome, endereco
3 - Não poderá existir mais de uma clínica com o mesmo CNPJ
4- Não excluir uma clínica sem a confirmação do usuário'''

'''def menuClinica ():
print('-----------MENU CLÍNICA---------')
print('1 - Cadastrar Clínica')
print('2 - Buscar Clínica por CNPJ')
print('3 - Editar Clínica')
print('4 - Remover Clínica')
print('5 - Listar todas as Clínicas')
print('6 – SAIR')'''


import json
import os

baseClinica = {}
arqbase = "BancoClinica.json"

def carregar_clinica():
    if os.path.exists(arqbase):
        with open(arqbase, 'r+') as arqJson:
            global baseClinica
            baseClinica = json.load(arqJson)


def gravarDadosJSON():
    with open('BancoClinica.json', 'w+') as arqJson:
        json.dump(baseClinica, arqJson, indent=True)


def lerDadosJSON():
    with open("BancoClinica.json", 'r') as arqJson:
        global baseClinica
        baseClinica = json.load(arqJson)


def menuClinica():
    print('-' * 50)
    print('MENU CLÍNICA'.center(50))
    print('-' * 50)
    print('1 - Cadastrar Clínica')
    print('2 - Buscar Clínica por CNPJ')
    print('3 - Editar Clínica')
    print('4 - Remover Clínica')
    print('5 - Listar todas as Clínicas')
    print('6 – Retornar ao Menu Principal')
    print("---------------------------------")
    opcao = int(input("\nDigite opção: "))
    return opcao


def verificarCNPJ(CNPJ):
    carregar_clinica()
    for clinica in baseClinica.values():
        if CNPJ == clinica.get("CNPJ"):
            return True
    return False


def cadastrarClinica():
    carregar_clinica()
    print("Cadastro de Clínica")
    while True:
        CNPJ = str(input("Digite CNPJ: "))
        if verificarCNPJ(CNPJ):
            print("Clínica já cadastrada com esse CNPJ\nPressione qualquer tecla para voltar:")
            input(">>> ")
            return
        nome = str(input("Digite o nome da clínica: "))
        endereco = str(input("Digite o endereço da clínica: "))
        clinica = {"CNPJ": CNPJ, "nome": nome, "endereco": endereco}
        CNPJ = clinica.get("CNPJ")
        baseClinica[CNPJ] = clinica
        gravarDadosJSON()
        opcao = int(input("Deseja cadastrar outra clínica? - [1-Sim | 2-Não]: "))
        if opcao != 1:
            break


def editarClinica():
    lerDadosJSON()
    print("Editando Clínica")
    cnpjpesq = str(input("Digite o CNPJ da clínica que você deseja editar: "))
    for clinica in baseClinica.values():
        if clinica.get("CNPJ") == cnpjpesq:
            print("CNPJ: %s - Clínica: %s - Endereço: %s" % (
                clinica["CNPJ"], clinica["nome"], clinica["endereco"]))
            while True:
                novoNome = clinica.get("nome")
                novoEndereco = clinica.get("endereco")
                opcao = int(input("Selecione o que você deseja editar:\n[1- Nome | 2- Endereço]: "))
                if opcao == 1:
                    novoNome = str(input("Digite o novo nome: "))
                    print("Nome da clínica alterado.")
                elif opcao == 2:
                    novoEndereco = str(input("Digite o novo endereço: "))
                    print("Endereço da clínica alterado.")
                else:
                    print("Opção inválida.")
                CNPJ = clinica.get("CNPJ")
                clinica = {'CNPJ': CNPJ, "nome": novoNome, "endereco": novoEndereco}
                baseClinica[CNPJ] = clinica
                gravarDadosJSON()
                op2 = int(input("Deseja continuar a editar? [1- Sim | 2- Não]: "))
                if op2 != 1:
                    break
            print("Clinica atualizada.\nPressione qualquer tecla para voltar ao menu clínica.")
            input(">>> ")
            return
    print("Clínica não encontrada.\nPressione qualquer tecla para voltar ao menu clínica.")
    input(">>> ")
    return


def removerClinica():
    lerDadosJSON()
    print("Remover Clínica")
    CNPJ = str(input("Digite CNPJ: "))
    for clinica in baseClinica.values():
        if clinica.get("CNPJ") == CNPJ:
            print(baseClinica[CNPJ])
            opcao = int(input("Deseja remover esta clínica? [1- Sim | 2- Não]: "))
            if opcao == 1:
                del baseClinica[CNPJ]
                gravarDadosJSON()
                print("Clinica removida com sucesso.\nPressione qualquer tecla para voltar ao menu clínica.")
                input(">>> ")
                return
            else:
                print("Pressione qualquer tecla para voltar ao menu de clínica")
                input(">>> ")
                break
    return


def buscaClinica():
    lerDadosJSON()
    print("Busca de Clínica")
    cnpjpesq = str(input("Informe o CNPJ da clínica que você quer encontrar: "))
    for clinica in baseClinica.values():
        if clinica.get("CNPJ") == cnpjpesq:
            print("CNPJ: %s - Clínica: %s - Endereço: %s" % (
                clinica["CNPJ"], clinica["nome"], clinica["endereco"]))
            print("\nPressione qualquer tecla para voltar ao menu clínica.")
            input(">>> ")
            return
    print("Clínica não encontrada.\nPressione qualquer tecla para voltar ao menu clínica.")
    input(">>> ")
    return


def listarClinica():
    lerDadosJSON()
    print("Listagem de Clínicas")
    for i in range(0, len(baseClinica)):
        for clinica in baseClinica.values():
            print("--------------------------------")
            print("CNPJ: %s \nClínica: %s \nEndereço: %s" % (
                clinica["CNPJ"], clinica["nome"], clinica["endereco"]))
        print("\nPressione qualquer tecla para voltar ao menu clínica.")
        input(">>> ")
        return
    print("Não há clínicas para serem listadas.")
    print("\nPressione qualquer tecla para voltar ao menu clínica.")
    input(">>> ")
    return
