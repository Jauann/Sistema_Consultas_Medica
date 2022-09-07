from Controladores.controladorClinica import baseClinica
from Controladores.controladorPaciente import basePaciente
from Controladores.controladorMedico import baseMedico
from Controladores.controladorConsultas import baseConsultas
from Controladores.controladorFuncionario import baseFuncionario
from datetime import *
import json

data = date(year=2022, month=5, day=17)
hora = time(hour=20, minute=10)
data2 = date(year=2022, month=5, day=17)
hora2 = time(hour=21, minute=10)


def adicionarBase():

    '''clinica = {"CNPJ": "11.111.111/1111-11", "nome": "Windows", "endereco": "Rua microsoft"}
    cnpj = clinica.get("CNPJ")
    baseClinica[cnpj] = clinica
    funcionario = {"matricula": "1", "CPF": "222.222.222.-22", "nome": "Elon Musk", "email": "Elonmusk@tesla.wrld", "clinica": "Windows"}
    cpf = funcionario.get("CPF")
    baseFuncionario[cpf] = funcionario
    paciente = {"CPF": "111.111.111-11", "nome": "Bill Gates", "email": "Gatesbill@win.wrld", "telefone": "99-99999-9999", "endereco": "Lá longe"}
    CPF = paciente.get("CPF")
    basePaciente[CPF] = paciente
    paciente = {"CPF": "112.111.111-11", "nome": "Gafield", "email": "Garfield@gmail.com",
                "telefone": "81-99999-9999", "endereco": "Rua dos Gatos"}
    CPF = paciente.get("CPF")
    basePaciente[CPF] = paciente
    medico = {"CRM": "111", "nome": "Endo", "email": "endo@gmail.com",
              "especialidade": "Cardiologia", "clinica": "Windows"}
    CRM = medico.get("CRM")
    baseMedico[CRM] = medico
    medico = {"CRM": "222", "nome": "Sakura", "email": "Sakura@gmail.com",
              "especialidade": "Neurologia", "clinica": "Windows"}
    CRM = medico.get("CRM")
    baseMedico[CRM] = medico
    medico = {"CRM": "333", "nome": "Neji", "email": "Neji@gmail.com",
              "especialidade": "Cardiologia", "clinica": "Windows"}
    CRM = medico.get("CRM")
    baseMedico[CRM] = medico
    medico = {"CRM": "444", "nome": "Madara", "email": "Madara@gmail.com",
              "especialidade": "Neurologia", "clinica": "Grannvale"}
    CRM = medico.get("CRM")
    baseMedico[CRM] = medico
    consulta = {"codigo": "01", "paciente": "111.111.111-11", "medico": "André Belmont", "data": data,
         "hora": hora, "retorno": True, "observacao": "Sem Observações"}
    codigo = consulta.get("codigo")
    baseConsultas[codigo] = consulta
    consulta = {"codigo": "02", "paciente": "112.111.111-11", "medico": "Arvis", "data": data2,
         "hora": hora2, "retorno": False, "observacao": "Queimadura grave de Terceiro Grau"}
    codigo = consulta.get("codigo")
    baseConsultas[codigo] = consulta
'''