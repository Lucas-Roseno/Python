class Pessoa: 
    def __init__(self, nome, sexo, endereco, cpf, telefone, identidade):
        self.nome = nome
        self.sexo = sexo
        self.endereco = endereco
        self.cpf = cpf
        self.telefone = telefone
        self.identidade = identidade

    def imprimirDetalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Sexo: {self.sexo}")
        print(f"Endereço: {self.endereco}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print(f"Identidade: {self.identidade}")
