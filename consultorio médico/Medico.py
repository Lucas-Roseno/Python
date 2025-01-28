from Pessoa import Pessoa
class Medico(Pessoa):
    
    def __init__(self, nome, sexo, endereco, cpf, telefone, identidade, crm, especialidade):
        super().__init__(nome, sexo, endereco, cpf, telefone, identidade)
        self.crm = crm
        self.especialidade = especialidade
        
    def imprimirDetalhes(self):
        super().imprimirDetalhes()
        print(f"CRM: {self.crm}")
        print(f"Especialidade: {self.especialidade}")