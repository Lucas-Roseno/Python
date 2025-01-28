from Paciente import Paciente
class Consulta(Paciente):
    def _init_(self, p, relato, medicamentos):
        self.p = p
        self.relato = relato
        self.medicamentos = medicamentos
