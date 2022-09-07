'''# REGRAS FUNCIONÁRIO
1 - baseFuncionario só deverá ser acessada do arquivo controlador
2 - Funcionario será um dicionário com as seguintes chaves: matricula, cpf, nome, e-mail, clinica
3 - Não poderá existir mais de um Funcionário com a mesma Matrícula
4 - Não poderá existir mais de um Funcionário com o mesmo CPF
5- Não excluir o funcionário sem a confirmação do usuário'''

'''def menuFuncionario ():
print('-----------MENU FUNCIONÁRIO---------')
print('1 - Cadastrar Funcionário')
print('2 - Buscar Funcionário por Matrícula')
print('3 - Editar Funcionário') #antes Buscar por matrícula
print('4 - Remover Funcionário')
print('5 - Listar Todos os Funcionários')
print('6 – SAIR')
'''

from Controladores.controladorClinica import *
import json
import os

baseFuncionario = {}
arqbaseF = "BancoFuncionario.json"


def carregar_funcionarios():
    if os.path.exists(arqbaseF):
        with open(arqbaseF, 'r+') as arqJson:
            global baseFuncionario
            baseFuncionario = json.load(arqJson)


def gravarDadosJSONf():
    with open('../Sistema de Marcação de Consulta Médica/BancoFuncionario.json', 'w+') as arqJson:
        json.dump(baseFuncionario, arqJson, indent=True)


def lerDadosJSONf():
    with open('BancoFuncionario.json', 'r') as arqJson:
        global baseFuncionario
        baseFuncionario = json.load(arqJson)


def menuFuncionario():
    print('-' * 50)
    print('MENU FUNCIONÁRIO'.center(50))
    print('-' * 50)
    print('1 - Cadastrar Funcionário')
    print('2 - Buscar Funcionário por Matrícula')
    print('3 - Editar Funcionário')
    print('4 - Remover Funcionário')
    print('5 - Listar Todos os Funcionários')
    print('6 – Retornar ao Menu Principal')
    opcao = int(input("\nDigite opção: "))
    return opcao


def verificarCPFfunc(CPF):
    carregar_funcionarios()
    for funcionario in baseFuncionario.values():
        if CPF == funcionario.get("CPF"):
            return True
    return False


def verificarMatricula(matricula):
    carregar_funcionarios()
    for funcionario in baseFuncionario.values():
        if matricula == funcionario.get("matricula"):
            return True
    return False


def verificarClinica(clinica):
    carregar_clinica()
    for i in baseClinica.values():
        if i.get("CNPJ") == clinica:
            return True
    return False


def cadastrarFuncionario():
    carregar_funcionarios()
    print("Cadastro de Funcionario")
    while True:
        matricula = str(input("Digite a matrícula do funcionário: "))
        if verificarMatricula(matricula):
            print("Funcionário já cadastrado com essa matrícula.\nPressione qualquer tecla para voltar:")
            input(">>> ")
            return
        CPF = str(input("Digite CPF: "))
        if verificarCPFfunc(CPF):
            print("Funcionário já cadastrado com esse CPF.\nPressione qualquer tecla para voltar:")
            input(">>> ")
            return
        nome = str(input("Digite o nome do funcionário: "))
        email = str(input("Digite o email do funcionário: "))
        clinica = str(input("Digite o CNPJ da clínica que o funcionário trabalha: "))
        if verificarClinica(clinica):
            CNPJ = clinica
            clinica = baseClinica[CNPJ]["nome"]
        else:
            print("Clínica não cadastrada com esse CNPJ")
            clinica = "Sem Vinculo"
        funcionario = {"matricula": matricula, "CPF": CPF, "nome": nome, "email": email, "clinica": clinica}
        cpf = funcionario.get("CPF")
        baseFuncionario[cpf] = funcionario
        gravarDadosJSONf()
        opcao = int(input("Deseja cadastrar outro funcionário? - [1-Sim | 2-Não]: "))
        if opcao != 1:
            break


def buscaFuncionario():
    lerDadosJSONf()
    print("Busca de Funcionário")
    matrpesq = str(input("Informe a matrícula do funcionário que você quer encontrar: "))
    for funcionario in baseFuncionario.values():
        if funcionario.get("matricula") == matrpesq:
            print("Matrícula: %s - CPF: %s - Funcionário %s - E-mail: %s - Clínica: %s" % (
                funcionario["matricula"], funcionario["CPF"], funcionario["nome"], funcionario["email"],
                funcionario["clinica"]))
            print("\nPressione qualquer tecla para voltar ao menu funcionário.")
            input()
            return
    print("Funcionário não encontrado.\nPressione qualquer tecla para voltar ao menu funcionário.")
    input()
    return


def editarFuncionario():
    lerDadosJSONf()
    print("Editando Funcionário")
    matrpesq = (input("Digite a matrícula do funcionário que você deseja editar: "))
    for funcionario in baseFuncionario.values():
        if funcionario.get("matricula") == matrpesq:
            print("Matrícula: %s - CPF: %s - Funcionário %s - E-mail: %s - Clínica: %s" % (
                funcionario["matricula"], funcionario["CPF"], funcionario["nome"], funcionario["email"],
                funcionario["clinica"]))
            while True:
                novoNome = funcionario.get("nome")
                novoEmail = funcionario.get("email")
                novaClinica = funcionario.get("clinica")
                opcao = int(input("Selecione o que você deseja editar:\n[1- Nome | 2- E-mail | 3- Clínica]: "))
                if opcao == 1:
                    novoNome = str(input("Digite o novo nome: "))
                    print("Nome do funcionario alterado.")
                elif opcao == 2:
                    novoEmail = str(input("Digite o novo e-mail: "))
                    print("E-mail do funcionario alterado.")
                elif opcao == 3:
                    novaClinica = str(input("Digite o CNPJ da clínica: "))
                    if verificarClinica(novaClinica):
                        CNPJ = novaClinica
                        novaClinica = baseClinica[CNPJ]["nome"]
                        print("Clínica alterada.")
                    else:
                        print("Clínica não cadastrada com esse CNPJ")
                        novaClinica = "Sem Vinculo"
                else:
                    print("Opção inválida.")
                matricula = funcionario.get("matricula")
                CPF = funcionario.get("CPF")
                funcionario = {"matricula": matricula, "CPF": CPF, "nome": novoNome, "email": novoEmail,
                               "clinica": novaClinica}
                baseFuncionario[matricula] = funcionario
                gravarDadosJSONf()
                op2 = int(input("Deseja continuar a editar? [1- Sim | 2- Não]: "))
                if op2 != 1:
                    break
            print("Funcionário atualizado.\nPressione qualquer tecla para voltar ao menu funcionário.")
            input()
            return
    print("Funcionário não encontrado.\nPressione qualquer tecla para voltar ao menu funcionário.")
    input()


def removerFuncionario():
    lerDadosJSONf()
    print("Remover Funcionário")
    CPF = str(input("Digite o CPF: "))
    for funcionario in baseFuncionario.values():
        if funcionario.get("CPF") == CPF:
            print(baseFuncionario[CPF])
            opcao = int(input("Deseja remover este funcionário? [1- Sim | 2- Não]: "))
            if opcao == 1:
                del baseFuncionario[CPF]
                gravarDadosJSONf()
                print("Funcionário removido com sucesso.\nPressione qualquer tecla para voltar ao menu Funcionário.")
                input(">>> ")
                return
            else:
                print("Pressione qualquer tecla para voltar ao menu Funcionário")
                input(">>> ")
                break
    print("Funcionário não encontrado.\nPressione qualquer tecla para voltar ao menu Funcionário")
    input(">>> ")
    return

def listarFuncionario():
    lerDadosJSONf()
    print("Listagem de Funcionários")
    for i in range(0, len(baseFuncionario)):
        for funcionario in baseFuncionario.values():
            print("--------------------------------")
            print("Matrícula: %s \nCPF: %s \nFuncionário %s \nE-mail: %s \nClínica: %s" % (
                funcionario["matricula"], funcionario["CPF"], funcionario["nome"], funcionario["email"],
                funcionario["clinica"]))
        print("\nPressione qualquer tecla para voltar ao menu funcionário.")
        input()
        return
    print("Não há funcionários para serem listados.")
    print("\nPressione qualquer tecla para voltar ao menu funcionário.")
    input()
    return
