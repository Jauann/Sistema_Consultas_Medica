'''# REGRAS MÉDICO
1 - baseMedicos só deverá ser acessada do arquivo controlador
2 - Medico será um dicionário com as seguintes chaves: CRM, nome, e-mail, especialidade, clinica.
3 - Não poderá existir mais de um médico com o mesmo CRM
4 – O tipo de especialidade do médico deverá ser: Cardiologia ou Neurologia
5- Não excluir um médico sem a confirmação do usuário'''

'''def menuMedico():
print('-----------MENU MÉDICO---------')
print('1 - Cadastrar Médico')
print('2 - Buscar Médico por CRM)
print('3 - Editar Médico') #antes Buscar por CRM
print('4 - Remover Médico')
print('5 - Listar Todos os Médicos')
print('6 - Pesquisar Médico por Especialidade')
print('7 – SAIR')'''

from Controladores.controladorPaciente import verificarClinica
import json
import os

baseMedico = {}
arqbaseM = "BancoMedico.json"


def carregar_medicos():
    if os.path.exists(arqbaseM):
        with open(arqbaseM, 'r+') as arqJson:
            global baseMedico
            baseMedico = json.load(arqJson)


def gravarDadosJSONm():
    with open('../Sistema de Marcação de Consulta Médica/BancoMedico.json', 'w+') as arqJson:
        json.dump(baseMedico, arqJson, indent=True)


def lerDadosJSONm():
    with open("BancoMedico.json", 'r') as arqJson:
        global baseMedico
        baseMedico = json.load(arqJson)


def menuMedico():
    print('-' * 50)
    print('MENU MÉDICO'.center(50))
    print('-' * 50)
    print('1 - Cadastrar Médico')
    print('2 - Buscar Médico por CRM')
    print('3 - Editar Médico')
    print('4 - Remover Médico')
    print('5 - Listar Todos os Médicos')
    print('6 - Pesquisar Médico por Especialidade')
    print('7 – Retornar ao menu principal')
    opcao = int(input("\nDigite opção: "))
    return opcao


def verificarCRM(CRM):
    carregar_medicos()
    for medico in baseMedico.values():
        if CRM == medico.get("CRM"):
            return True
    return False


def cadastrarMedico():
    carregar_medicos()
    print("Cadastro de Médico")
    while True:
        especialidade = ""
        CRM = str(input("Digite a CRM do médico: "))
        if verificarCRM(CRM):
            print("Médico já cadastrado com essa CRM.\nPressione qualquer tecla para voltar:")
            input(">>> ")
            return
        nome = str(input("Digite o nome do médico: "))
        email = str(input("Digite o email do médico: "))
        espescolha = int(input("Digite a especialidade do médico:"
                               "\n[1- Cardiologia | 2- Neurologia]\n>>> "))
        if espescolha == 1:
            especialidade = "Cardiologia"
        elif espescolha == 2:
            especialidade = "Neurologia"
        clinica = str(input("Digite o nome da clínica que o médico trabalha: "))
        medico = {"CRM": CRM, "nome": nome, "email": email, "especialidade": especialidade, "clinica": clinica}
        CRM = medico.get("CRM")
        baseMedico[CRM] = medico
        gravarDadosJSONm()
        opcao = int(input("Deseja cadastrar outro médico? - [1-Sim | 2-Não]: "))
        if opcao != 1:
            break


def buscaMedico():
    lerDadosJSONm()
    print("Busca de Médico")
    crmpesq = str(input("Informe a CRM do médico que você quer encontrar: "))
    for medico in baseMedico.values():
        if medico.get("CRM") == crmpesq:
            print("CRM: %s - Médico: %s - E-mail: %s - Especialidade: %s" % (
                medico["CRM"], medico["nome"], medico["email"], medico["especialidade"]))
            print("\nPressione qualquer tecla para voltar ao menu médico.")
            input(">>> ")
            return
    print("Médico não encontrado.\nPressione qualquer tecla para voltar ao menu médico.")
    input(">>> ")
    return


def editarMedico():
    lerDadosJSONm()
    print("Editando Médico")
    crmpesq = (input("Digite a CRM do médico que você deseja editar: "))
    for medico in baseMedico.values():
        if medico.get("CRM") == crmpesq:
            print("CRM: %s - Médico: %s - E-mail: %s - Especialidade: %s - Clínica: %s " % (
                medico["CRM"], medico["nome"], medico["email"], medico["especialidade"], medico["clinica"]))
            while True:
                novoNome = medico.get("nome")
                novoEmail = medico.get("email")
                novaEspecialidade = medico.get("especialidade")
                novaClinica = medico.get("clinica")
                opcao = int(input(
                    "Selecione o que você deseja editar:\n[1- Nome | 2- E-mail | 3- Especialidade | 4- Clínica]: "))
                if opcao == 1:
                    novoNome = str(input("Digite o novo nome: "))
                    print("Nome do médico alterado.")
                elif opcao == 2:
                    novoEmail = str(input("Digite o novo e-mail: "))
                    print("E-mail do médico alterado.")
                elif opcao == 3:
                    op = int(input("Digite a especialidade do médico:"
                                   "\n[1- Cardiologia | 2- Neurologia]\n>>> "))
                    if op == 1:
                        novaEspecialidade = "Cardiologia"
                    elif op == 2:
                        novaEspecialidade = "Neurologia"
                elif opcao == 4:
                    novaClinica = str(input("Digite o nome da nova clínica: "))
                    print("Clínica do médico alterada.")
                else:
                    print("Opção inválida.")
                CRM = medico.get("CRM")
                medico = {"CRM": CRM, "nome": novoNome, "email": novoEmail, "especialidade": novaEspecialidade, "clinica": novaClinica}
                baseMedico[CRM] = medico
                gravarDadosJSONm()
                op2 = int(input("Deseja continuar a editar? [1- Sim | 2- Não]: "))
                if op2 != 1:
                    break
            print("Médico atualizado.\nPressione qualquer tecla para voltar ao menu médico.")
            input()
            return
    print("Médico não encontrado.\nPressione qualquer tecla para voltar ao menu médico.")
    input()


def removerMedico():
    lerDadosJSONm()
    print("Remover Médico")
    CRM = str(input("Digite a CRM: "))
    for medico in baseMedico.values():
        if medico.get("CRM") == CRM:
            print(baseMedico[CRM])
            opcao = int(input("Deseja remover este médico? [1- Sim | 2- Não]: "))
            if opcao == 1:
                del baseMedico[CRM]
                gravarDadosJSONm()
                print("Médico removido com sucesso.\nPressione qualquer tecla para voltar ao menu médico.")
                input(">>> ")
                return
            else:
                print("Pressione qualquer tecla para voltar ao menu médico")
                input(">>> ")
                break
    print("Médico não encontrado.\nPressione qualquer tecla para voltar ao menu médico")
    input(">>> ")
    return


def listarMedico():
    lerDadosJSONm()
    print("Listagem de Médicos")
    for i in range(0, len(baseMedico)):
        for medico in baseMedico.values():
            print("--------------------------------")
            print("CRM: %s \nMédico: %s \nE-mail: %s \nEspecialidade: %s \nClínica: %s" % (
                medico["CRM"], medico["nome"], medico["email"], medico["especialidade"], medico["clinica"]))
        print("\nPressione qualquer tecla para voltar ao menu médico.")
        input(">>> ")
        return
    print("Não há médicos para serem listados.")
    print("\nPressione qualquer tecla para voltar ao menu médico.")
    input(">>> ")
    return


def pesquisarPorEspecialidade():
    lerDadosJSONm()
    print("Busca de Médicos por Especialidade")
    esppesq = ""
    opcao = int(input("Informe a especialidade do médico que você quer encontrar:"
                      "\n[1- Cardiologia | 2- Neurologia]\n>>> "))
    if opcao == 1:
        esppesq = "Cardiologia"
    elif opcao == 2:
        esppesq = "Neurologia"
    else:
        print("Opção Inválida.")
    for medico in baseMedico.values():
        if medico.get("especialidade") == esppesq:
            print("Médico(a): %s - CRM: %s - Clínica: %s" % (medico["nome"], medico["CRM"], medico["clinica"]))
    print("\nPressione qualquer tecla para voltar ao menu médico.")
    input(">>> ")
    return