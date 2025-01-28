class Consultorio():
    def __init__(self, p, m, consulta, cpfs, consultas, sexos, endereços, tels, rgs, medicação, medicações):
        self.p = []
        self.m = m
        self.consulta = consulta
        self.consultas = []
        self.cpfs = []
        self.sexos = []
        self.endereços = []
        self.tels = []
        self.rgs = []
        self.medicação = medicação
        self.medicações = []
    def imprimir(self):
        for i, j in zip(self.p, self.consulta):
            print(f'\nPaciente: {i.title()}\tConsulta de {i.title()}: {j.title()}')
    
    def cadastrarPaciente(self):
        self.nome = input('\nDigite o nome do paciente a ser cadastrado: ')
        self.sexo = input(f'Digite o sexo de {self.nome.title()}: ')
        self.endereço = input(f'Digite o endereço de {self.nome.title()}: ')
        self.cpf = str(input(f'Digite o CPF de {self.nome.title()}: '))
        self.tel = input(f'Digite o telefone de {self.nome.title()}: ')
        self.rg = input(f'Digite o RG de {self.nome.title()}: ')
        self.medicação = input(f'Digite a medicação contínua de {self.nome.title()}: ')

        self.p.append(self.nome)
        self.sexos.append(self.sexo)
        self.endereços.append(self.endereço)
        self.cpfs.append(self.cpf)
        self.tels.append(self.tel)
        self.rgs.append(self.rg)
        self.medicações.append(self.medicação)

    def cadastrarConsulta(self):
        self.consulta = input('Por fim, digite o motivo da consulta: ')

        self.consultas.append(self.consulta)

    def cancelar(self):
        self.cpf = str(input('\nDigite o CPF do paciente: '))
        
        for i, j, k in zip(self.cpfs, self.p, self.consultas):
            if i == self.cpf:
                self.cpfs.remove(i)
                self.p.remove(j)
                self.consultas.remove(k)
                print(f'\nA consulta de {j.title()} foi cancelada com sucesso!')
                return
        print('\nNenhum paciente encontrado com esse CPF.')
        
    def consultaPaciente(self, cpf):
        for i, j, k in zip(self.cpfs, self.p, self.consultas):
            if i == cpf:
                print(f'\nPaciente: {j.title()}\tMotivo da consulta: {k.title()}')
                return
        print('\nNenhum paciente encontrado com esse CPF.')

    def imprimirTodasConsultas(self):
        cont = 1
        print('\nAgenda de consultas: ')
        for i in self.consultas:
            print(f'\n- {cont}° consulta: {i.title()}')
            cont += 1
    
    def imprimirDados(self):
        print(f'\nNome: {self.p[-1]}\nSexo: {self.sexos[-1]}\nEndereço: {self.endereços[-1]}\nCPF: {self.cpfs[-1]}\nTelefone: {self.tels[-1]}\nRG: {self.rgs[-1]}\nMedicação: {self.medicações[-1]}')

