'''def menuPrincipal():
print('-----------MENU---------')
print('1 - Menu de Paciente')
print('2 - Menu de Marcação de Consulta')
print('3 - Menu de Médico')
print('4 - Menu de Funcionário')
print('5- Menu de Clínica')
print('6 – SAIR')
'''

from util.cache import *
from Controladores.controladorClinica import *
from Controladores.controladorFuncionario import *
from Controladores.controladorMedico import *
from Controladores.controladorPaciente import *
from Controladores.controladorConsultas import *


def menuPrincipal():
    print('-' * 50)
    print('MENU PRINCIPAL'.center(50))
    print('-' * 50)
    print('1 - Menu de Paciente')
    print('2 - Menu de Marcação de Consulta')
    print('3 - Menu de Médico')
    print('4 - Menu de Funcionário')
    print('5 - Menu de Clínica')
    print('6 – Finilizar Aplicação')
    print('-' * 50)
    opcao = int(input("Digite Opção: "))
    return opcao


adicionarBase()


def main():
    while True:
        opcao=menuPrincipal()
        match opcao:
            case 1:
                while True:
                    opcao = menuPaciente()
                    match opcao:
                        case 1:
                            cadastrarPaciente()
                        case 2:
                            buscaPaciente()
                        case 3:
                            editarPaciente()
                        case 4:
                            removerPaciente()
                        case 5:
                            listarPaciente()
                        case 6:
                            print("\nMenu Paciente Fechado.\n")
                            break
                        case _:
                            print("Opção Inválida")
            case 2:
                while True:
                    opcao = menuConsulta()
                    match opcao:
                        case 1:
                            marcarConsulta()
                        case 2:
                            buscarConsultaPac()
                        case 3:
                            editarConsulta()
                            pass
                        case 4:
                            removerConsulta()
                        case 5:
                            listarConsulta()
                        case 6:
                            listarConsultaPorRetorno()
                        case 7:
                            listarPorDataHora()
                        case 8:
                            print("\nMenu Consulta Fechado.\n")
                            break
                        case _:
                            print("Opção Inválida")
            case 3:
                while True:

                    opcao = menuMedico()
                    match opcao:
                        case 1:
                            cadastrarMedico()
                        case 2:
                            buscaMedico()
                        case 3:
                            editarMedico()
                        case 4:
                            removerMedico()
                        case 5:
                            listarMedico()
                        case 6:
                            pesquisarPorEspecialidade()
                        case 7:
                            print("Menu Médico Fechado.")
                            break
                        case _:
                            print("Opção Inválida.")
            case 4:
                while True:
                    opcao = menuFuncionario()
                    match opcao:
                        case 1:
                            cadastrarFuncionario()
                        case 2:
                            buscaFuncionario()
                        case 3:
                            editarFuncionario()
                        case 4:
                            removerFuncionario()
                        case 5:
                            listarFuncionario()
                        case 6:
                            print("Menu Funcionário Fechado.")
                            break
                        case _:
                            print("Opção Inválida.")
            case 5:
                while True:
                    opcao = menuClinica()
                    match opcao:
                        case 1:
                            cadastrarClinica()
                        case 2:
                            buscaClinica()
                        case 3:
                            editarClinica()
                        case 4:
                            removerClinica()
                        case 5:
                            listarClinica()
                        case 6:
                            print("Menu Clínica Fechado.")
                            break
                        case _:
                            print("Opção Inválida.")
            case 6:
                print("Programa Encerrado.")
                break
            case _:
                print("Opção Inválida.")

main()