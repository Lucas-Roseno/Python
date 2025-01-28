
from sys import exit
from Medico import Medico
from Consulta import Consulta
from Consultorio import Consultorio
from Paciente import Paciente
from Pessoa  import Pessoa

consultorio = Consultorio([], [], [], [], [], [], [], [], [], [], [])

opc = int
cont = 0

while(opc != 7):
    opc = int(input(('\nMenu:\n\n'
                     +'1 - Dados do médico\n'
                     +'2 - Cadastrar um paciente/consulta\n'
                     +'3 - Cancelar consulta\n'
                     +'4 - Imprimir a consulta\n'
                     +'5 - Ver agendas'
                     +'\n6 - Imprimir dados último paciente'
                     +'\n7 - Sair\nOpção: ')))

    match opc:
        case 1: 
            medico = Medico('Carla', 'feminina', 'Rua 1223', '300.300.300-20', '(37) 9999 - 9090', '90.900.900-0', '123456', 'Endrócina')
            medico.imprimirDetalhes()
        case 2:
            consultorio.cadastrarPaciente()
            consultorio.cadastrarConsulta()
            cont += 1
        case 3:
            if(cont == 0):
                print('\nNenhuma consulta cadastrada no sistema. Por favor, tente novamente.')
            else:
                consultorio.cancelar()
        case 4:
            if(cont == 0):
                print('\nNenhuma consulta cadastrada no sistema. Por favor, tente novamente.')
            else:
                cpf = str(input('\nDigite o CPF do paciente: '))
                consultorio.consultaPaciente(cpf)
        case 5:
            if(cont == 0):
                print('\nNenhuma consulta cadastrada no sistema. Por favor, tente novamente.')
            else:
                consultorio.imprimirTodasConsultas()
        case 6:
            if(cont == 0):
                print('\nNenhuma consulta cadastrada no sistema. Por favor, tente novamente.')
            else:
                consultorio.imprimirDados()
        case 7:
            exit()
        case _:
            print('\nOpção inválida. Por favor, tente novamente.')
