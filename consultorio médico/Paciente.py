from Medico import Medico
class Paciente(Medico):
    def __init__(self, nome, sexo, endereco, cpf, telefone, identidade, medConti):
        super().__init__(nome, sexo, endereco, cpf, telefone, identidade)
        self.medicacaoContinua = medConti
        
    def imprimirDescricao(self):
        super().imprimirDetalhes(self)
        print("Medicação contínua: " + self.medicacaoContinua)
        