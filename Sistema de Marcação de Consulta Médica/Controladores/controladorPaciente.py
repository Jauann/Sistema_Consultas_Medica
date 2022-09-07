'''# REGRAS PACIENTE
1 - basePacientes só deverá ser acessada do arquivo controlador
2 - Paciente será um dicionário com as seguintes chaves: cpf, nome, e-mail, telefone e endereço.
3 - Não poderá existir mais de um paciente com o mesmo CPF
4- Não excluir o paciente sem a confirmação do usuário'''

'''def menuPaciente():
print('-----------MENU PACIENTE---------')
print('1 - Cadastrar Paciente')
print('2 - Buscar Paciente por cpf')
print('3 - Editar Paciente') #antes Buscar por cpf o Paciente
print('4 - Remover Paciente')
print('5 - Listar Todos os Paciente')
print('6 – SAIR')'''


from Controladores.controladorClinica import *
import json
import os


basePaciente = {}
arqbaseP = "BancoPaciente.json"


def carregar_pacientes():
    if os.path.exists(arqbaseP):
        with open(arqbaseP, 'r+') as arqJson:
            global basePaciente
            basePaciente = json.load(arqJson)


def gravarDadosJSONp():
    with open('../Sistema de Marcação de Consulta Médica/BancoPaciente.json', 'w+') as arqJson:
        json.dump(basePaciente, arqJson, indent=True)


def lerDadosJSONp():
    with open("BancoPaciente.json", 'r') as arqJson:
        global basePaciente
        basePaciente = json.load(arqJson)


def menuPaciente():
    print('-' * 50)
    print('MENU PACIENTE'.center(50))
    print('-' * 50)
    print('1 - Cadastrar Paciente')
    print('2 - Buscar Paciente por cpf')
    print('3 - Editar Paciente')
    print('4 - Remover Paciente')
    print('5 - Listar Todos os Pacientes')
    print('6 – Voltar ao Menu Principal')
    opcao = int(input("\nDigite opção: "))
    return opcao


def verificarCPFpac(CPF):
    carregar_pacientes()
    for paciente in basePaciente.values():
        if CPF == paciente.get("CPF"):
            return True
    return False


def verificarClinica(clinica):
    gravarDadosJSON()
    for i in baseClinica.values():
        if i.get("CNPJ") == clinica:
            return True
    return False


def cadastrarPaciente():
    carregar_pacientes()
    print("Cadastro de Paciente")
    while True:
        CPF = str(input("Digite CPF: "))
        if verificarCPFpac(CPF):
            print("Paciente já cadastrado com esse CPF.\nPressione qualquer tecla para voltar:")
            input(">>> ")
            return
        nome = str(input("Digite o nome do paciente: "))
        email = str(input("Digite o email do paciente: "))
        telefone = str(input("Digite o telefone do paciente: "))
        endereco = str(input("Digite o endereço do paciente: "))
        paciente = {"CPF": CPF, "nome": nome, "email": email, "telefone": telefone, "endereco": endereco}
        CPF = paciente.get("CPF")
        basePaciente[CPF] = paciente
        gravarDadosJSONp()
        opcao = int(input("Deseja cadastrar outro paciente? - [1-Sim | 2-Não]: "))
        if opcao !=1:
            break


def buscaPaciente():
    lerDadosJSONp()
    print("Busca de Paciente")
    cpfpesq = str(input("Informe o CPF do paciente que você quer encontrar: "))
    for paciente in basePaciente.values():
        if paciente.get("CPF")==cpfpesq:
            print("CPF: %s - Paciente %s - E-mail: %s - Fone: %s - Endereço: %s" % (
                paciente["CPF"], paciente["nome"], paciente["email"], paciente["telefone"], paciente["endereco"]))
            print("\nPressione qualquer tecla para voltar ao menu paciente.")
            input(">>> ")
            return
    print("Paciente não encontrado.\nPressione qualquer tecla para voltar ao menu paciente.")
    input(">>> ")
    return


def editarPaciente():
    lerDadosJSONp()
    print("Editando Paciente")
    cpfpesq = str(input("Digite o CPF do paciente que você deseja editar: "))
    for paciente in basePaciente.values():
        if paciente.get("CPF") == cpfpesq:
            print("CPF: %s - Paciente %s - E-mail: %s - Fone: %s - Endereço: %s" % (
                paciente["CPF"], paciente["nome"], paciente["email"], paciente["telefone"], paciente["endereco"]))
            while True:
                novoNome = paciente.get("nome")
                novoEmail = paciente.get("email")
                novoTelefone = paciente.get("telefone")
                novoEndereco = paciente.get("endereco")
                opcao = int(input("Selecione o que você deseja editar:\n[1- Nome | 2- E-mail | 3- Telefone | 4- Endereço]: "))
                if opcao == 1:
                    novoNome = str(input("Digite o novo nome: "))
                    print("Nome do paciente alterado.")
                elif opcao == 2:
                    novoEmail = str(input("Digite o novo e-mail: "))
                    print("E-mail do paciente alterado.")
                elif opcao == 3:
                    novoTelefone = str(input("Digite o novo telefone: "))
                    print("Telefone do paciente alterado.")
                elif opcao == 4:
                    novoEndereco = str(input("Digite o novo endereço: "))
                    print("Endereço do paciente alterado.")
                else:
                    print("Opção inválida.")
                CPF = paciente.get("CPF")
                paciente={"CPF":CPF, "nome":novoNome, "email":novoEmail, "telefone":novoTelefone, "endereco":novoEndereco}
                basePaciente[CPF] = paciente
                gravarDadosJSONp()
                op2=int(input("Deseja continuar a editar? [1- Sim | 2- Não]: "))
                if op2!=1:
                    break
            print("Paciente atualizado.\nPressione qualquer tecla para voltar ao menu paciente.")
            input(">>> ")
            return
    print("Paciente não encontrado.\nPressione qualquer tecla para voltar ao menu paciente.")
    input(">>> ")


def removerPaciente():
    lerDadosJSONp()
    print("Remover Paciente")
    CPF = str(input("Digite o CPF: "))
    for paciente in basePaciente.values():
        if paciente.get("CPF") == CPF:
            print(basePaciente[CPF])
            opcao = int(input("Deseja remover este paciente? [1- Sim | 2- Não]: "))
            if opcao == 1:
                del basePaciente[CPF]
                gravarDadosJSONp()
                print("Paciente removido com sucesso.\nPressione qualquer tecla para voltar ao menu paciente.")
                input(">>> ")
                return
            else:
                print("Pressione qualquer tecla para voltar ao menu paciente")
                input(">>> ")
                break
    return


def listarPaciente():
    lerDadosJSONp()
    print("Listagem de Pacientes")
    for i in range(0, len(basePaciente)):
        for paciente in basePaciente.values():
            print("--------------------------------")
            print("CPF: %s \nPaciente %s \nE-mail: %s \nFone: %s \nEndereço: %s" % (
                paciente["CPF"], paciente["nome"], paciente["email"], paciente["telefone"], paciente["endereco"]))
        print("\nPressione qualquer tecla para voltar ao menu paciente.")
        input(">>> ")
        return
    print("Não há pacientes para serem listados.")
    print("\nPressione qualquer tecla para voltar ao menu paciente.")
    input(">>> ")
    return