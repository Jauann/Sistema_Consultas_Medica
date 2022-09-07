'''# REGRAS MARCAÇÃO DE CONSULTAS
1-baseConsultas só deverá ser acessada do arquivo controlador
2-Consulta será um dicionário com as seguintes chaves: codigo,
 paciente, medico, data, hora, retorno e observacao
3-Não poderá existir uma marcação de consulta para o mesmo médico na mesma
data e hora
4-Não excluir uma marcação de consulta sem a confirmação do usuário
5–A chave “Retorno” deverá armazenar o valor TRUE caso a consulta seja um
 retorno do paciente, e FALSE caso seja uma nova consulta.'''

'''def menuConsulta ():
print('-----------MENU MARCAÇÃO DE CONSULTAS---------')
print('1 - Marcar Consulta')
print('2 - Buscar Consulta por Paciente')
print('3 - Editar Consulta')
print('4 - Remover Consulta')
print('5 - Listar Consultas')
print('6 - Listar Consultas por Retorno')
print('7 - Listar Consultas por intervalo de datas') 
print('8 – SAIR')'''

from Controladores.controladorMedico import verificarCRM
from datetime import *
import calendar
from _datetime import datetime
import json
import os


def menuConsulta():
    print('-' * 50)
    print('MENU MARCAÇÃO DE CONSULTAS'.center(50))
    print('-' * 50)
    print('1 - Marcar Consulta')
    print('2 - Buscar Consulta por Paciente')
    print('3 - Editar Consulta')
    print('4 - Remover Consulta')
    print('5 - Listar Consultas')
    print('6 - Listar Consultas por Retorno')
    print('7 - Listar Consultas por intervalo de datas')
    print('8 – Voltar ao Menu Principal')
    opcao = int(input("\nDigite opção: "))
    return opcao


from Controladores.controladorPaciente import *
from Controladores.controladorMedico import *


baseConsultas = {}
arqbaseC = "BancoConsultas.json"


def carregar_consultas():
    if os.path.exists(arqbaseC):
        with open(arqbaseC, 'r+') as arqJsonC:
            global baseConsultas
            baseConsultas = json.load(arqJsonC)


def gravarDadosJSONCON():
    with open('../Sistema de Marcação de Consulta Médica/BancoConsultas.json', 'w+') as arqJsonC:
        json.dump(baseConsultas, arqJsonC, indent=True)


def lerDadosJSONCON():
    with open("BancoConsultas.json", 'r') as arqJsonC:
        global baseConsultas
        baseConsultas = json.load(arqJsonC)


def verificarDataHora(datahora, medico):
    carregar_consultas()
    for consulta in baseConsultas.values():
        if datahora == consulta.get("datahora") and medico == consulta.get("medico"):
             return True
    return False


def VerificarConsultas(codigo):
    carregar_consultas()
    for consulta in baseConsultas.values():
        if codigo == consulta.get("codigo"):
            return True
    return False


def marcarConsulta():
    carregar_consultas()
    print("Marcação de Consulta")
    while True:
        carregar_medicos()
        codigo = str(input("Digite o código de sua consulta: "))
        if VerificarConsultas(codigo):
            print("Consulta com o código já cadastrado")
            input(">>> ")
            return
        paciente = str(input("Digite o CPF do paciente: "))
        if not verificarCPFpac(paciente):
            carregar_pacientes()
            print("Paciente não cadastrado")
            return
        medico = str(input("Digite a CRM do médico que atenderá o paciente: "))
        if not verificarCRM(medico):
            print("Médico não cadastrado.")
            return
        else:
            verificarCRM(medico)
        try:
            datahora = str(input("Digite a data do atendimento (Formato DD/MM/YYYY HH:MM): "))
        except ValueError:
            print("Formato errado, tente novamente")
            return
        if verificarDataHora(datahora, medico):
            print("\nData e Hora já agendadas ou muito próximas uma da outra,"
                  "\no intervalo entre uma consulta e outra é de 30 minutos.")
            return
        retorno = 0
        retornopesq = int(input("O paciente está sendo atendido pela primeira vez ou está retornando?"
                                "\n[1- Primeira vez | 2- Retornando]\n>>> "))
        if retornopesq == 2:
            retorno = True
        elif retornopesq == 1:
            retorno = False
        else:
            print("Opção inválida.")
        observacao = str(input("Alguma observação específica para esse atendimento?\n>>> "))
        if observacao == "":
            observacao = "Sem observações."
        consulta = {"codigo": codigo, "paciente": paciente, "medico": medico, "datahora": datahora,
                    "retorno": retorno, "observacao": observacao}
        codigo = consulta.get("codigo")
        baseConsultas[codigo] = consulta
        gravarDadosJSONCON()
        opcao = int(input("Deseja marcar outra consulta? - [1-Sim | 2-Não]: "))
        if opcao != 1:
            break


def converterEmDataHora(datahorastr):
    return datetime.strptime(datahorastr, "%d/%m/%Y,%H:%M").datetime()


# def converterEmHora(horastr):
#     return datetime.strptime(horastr, "%H:%M").time()


def buscarConsultaPac():
    lerDadosJSONCON()
    print("Busca de Consulta por Paciente")
    ppesq = str(input("Digite o CPF do paciente que deseja buscar: "))
    for consulta in baseConsultas.values():
        if consulta.get("paciente") == ppesq:
            print("Código: %s | Paciente %s | CRM do médico: %s | DataHora: %s | %s |\nObservação: %s" % (
                  consulta["codigo"], consulta["paciente"], consulta["medico"], consulta["datahora"],
                   consulta["retorno"], consulta["observacao"]))
            print("\nPressione qualquer tecla para voltar ao menu consultas.")
            input(">>> ")
            return
    print("Consulta não encontrada.\nPressione qualquer tecla para voltar ao menu consultas.")
    input(">>> ")
    return


def editarConsulta():
    lerDadosJSONCON()
    print("Editando Consultas")
    codpesq = (input("Digite o codigo da consulta que você deseja editar: "))
    for consulta in baseConsultas.values():
        if consulta.get("codigo") == codpesq:
            pacienteC = basePaciente.get(consulta.get("codigo"), ["paciente"])
            if consulta.get("retorno") == True:
                retornoC = "Retornando"
            else:
                retornoC = "Primeiro Atendimento"
            print("Código: %s | Paciente %s | Médico %s | DataHora: %s | %s |\nObservação: %s" %
                  (consulta["codigo"], pacienteC, consulta["medico"], consulta["datahora"],
                   retornoC, consulta["observacao"]))
            while True:
                novoPaciente = consulta.get("paciente")
                novoMedico = consulta.get("medico")
                novaDataHora = consulta.get("datahora")
                novoRetorno = consulta.get("retorno")
                novaObservacao = consulta.get("observacao")
                opcao = int(input(
                    "Selecione o que você deseja editar:\n[1- Paciente | 2- Médico | 3- DataHora |\n[4- Alterar Retorno | 5- Alterar Observação]\n>>>  "))
                if opcao == 1:
                    novoPaciente = str(input("Digite o CPF do novo Paciente: "))
                    carregar_pacientes()
                    if not verificarCPFpac(novoPaciente):
                        print("Paciente não cadastrado")
                        return
                    print("Paciente alterado.")
                elif opcao == 2:
                    novoMedico = str(input("Digite a CRM do novo Médico: "))
                    carregar_medicos()
                    if not verificarCRM(novoMedico):
                        print("Médico não cadastrado.")
                        return
                    print("Médico alterado.")
                elif opcao == 3:
                    novaDataHora = str(input("Digite a nova data: "))
                    print("Data Alterada.")
                    if verificarDataHora(novaDataHora,novoMedico):
                        print("Data e Hora já agendadas ou muito próximas uma da outra,\n"
                              "o intervalo entre uma consulta e outra é de 30 minutos.")
                        return
                elif opcao == 4:
                    novoRetorno = 0
                    retornopesq = int(input("O paciente está sendo atendido pela primeira vez ou está retornando?"
                                            "\n[1- Primeira vez | 2- Retornando]\n>>> "))
                    if retornopesq == 2:
                        novoRetorno = True
                    elif retornopesq == 1:
                        novoRetorno = False
                    else:
                        print("Opção inválida.")
                elif opcao == 5:
                    novaObservacao = str(input("Alguma observação específica para esse atendimento?\n>>> "))
                    print("Observação atualizada.")
                else:
                    print("Opção inválida.")
                codigo = consulta.get("codigo")
                consulta = {"codigo": codigo, "paciente": novoPaciente, "medico": novoMedico, "datahora": novaDataHora,
                            "retorno": novoRetorno, "observacao": novaObservacao}
                baseConsultas[codigo] = consulta
                gravarDadosJSONCON()
                op2 = int(input("Deseja continuar a editar? [1- Sim | 2- Não]: "))
                if op2 != 1:
                    break
            print("Consulta atualizada.\nPressione qualquer tecla para voltar ao Menu Consultas.")
            input(">>> ")
            return
    print("Consulta não encontrada.\nPressione qualquer tecla para voltar ao Menu Consultas.")
    input(">>> ")


def removerConsulta():
    lerDadosJSONCON()
    print("Remover Consulta")
    codigo = str(input("Digite o codigo da consulta: "))
    for consulta in baseConsultas.values():
        if consulta.get("codigo") == codigo:
            print(baseConsultas[codigo])
            opcao = int(input("Deseja remover esta consulta? [1- Sim | 2- Não]: "))
            if opcao == 1:
                del baseConsultas[codigo]
                gravarDadosJSONCON()
                print("Consulta removida com sucesso.\nPressione qualquer tecla para voltar ao menu consultas.")
                input(">>> ")
                return
    print("Consulta não encontrada.\nPressione qualquer tecla para voltar ao menu consultas")
    input(">>> ")
    return


def listarConsulta():
    lerDadosJSONCON()
    print("Listagem de Consultas")
    for consulta in baseConsultas.values():
        print("--------------------------------")
        if consulta.get("retorno") == True:
            retornoC = "Retornando"
        else:
            retornoC = "Primeiro Atendimento"
        print("Código: %s \nPaciente %s \nCRM do médico: %s \n%s  \nDataHora: %s \nObservação: %s" %
              (consulta["codigo"], consulta["paciente"], consulta["medico"], consulta["datahora"],
               retornoC, consulta["observacao"]))
    print("\nPressione qualquer tecla para voltar ao menu consulta.")
    input(">>> ")
    return


def listarConsultaPorRetorno():
    lerDadosJSONCON()
    print("Listagem de Consultas por Retorno")
    op = int(input("O paciente está retornando?\n[1- Sim | 2- Não]\n>>> "))
    if op == 1:
        for consulta in baseConsultas.values():
            if consulta.get("retorno") == True:
                print('--------------------------------\nPacientes Retornando:\n--------------------------------')
                pacienteC = basePaciente.get(consulta.get)
                print("Código: %s | Paciente %s | CRM do médico: %s | DataHora: %s |\nObservação: %s" %
                      (consulta["codigo"], pacienteC, consulta["medico"], consulta["datahora"],
                       consulta["observacao"]))
        print("\nPressione qualquer tecla para voltar ao menu consulta.")
        input(">>> ")
        return
    elif op == 2:
        for consulta in baseConsultas.values():
            if consulta.get("retorno") == False:
                print("--------------------------------\nPacientes atendidos pela primeira vez:\n--------------------------------")
                pacienteC = basePaciente.get(consulta.get)
                print("Código: %s | Paciente: %s | CRM do médico: %s | DataHora: %s |\nObservação: %s" %
                      (consulta["codigo"], pacienteC, consulta["medico"], consulta["datahora"],
                       consulta["observacao"]))
        print("\nPressione qualquer tecla para voltar ao menu consulta.")
        input(">>> ")
        return
    else:
        print("Opção Inválida")
    print("Não há consultas para serem listadas.")
    print("\nPressione qualquer tecla para voltar ao menu consulta.")
    input(">>> ")
    return


def listarPorDataHora():
    carregar_consultas()
    x = int(input('Digite a data e hora inicial DD/MM/AAAA HH/MM: ').replace("/", "").replace(":", "").replace(" ", ""))
    z = int(input('Digite a data e hora final DD/MM/AAAA HH/MM: ').replace("/", "").replace(":", "").replace(" ", ""))
    print("-" * 34)
    print("LISTAGEM DE CONSULTAS".center(34))
    print("-" * 34)
    for codigo in baseConsultas:
        if int(baseConsultas[codigo]["datahora"].replace("/", "").replace(":", "").replace(" ", "")) >= x and \
           int(baseConsultas[codigo]["datahora"].replace("/", "").replace(":", "").replace(" ", "")) <= z:
            print("Código: %s \nPaciente: %s \nCRM do médico: %s \nData e Hora: %s \nObservação: %s" %
            (baseConsultas[codigo]["codigo"], baseConsultas[codigo]["paciente"], baseConsultas[codigo]
            ["medico"], baseConsultas[codigo]["datahora"], baseConsultas[codigo]["observacao"]))
            print("-" * 34)