# hospital.py
from medico import Medico
from paciente import Paciente

class Hospital:
    def __init__(self):
        self.medicos = []
        self.pacientes = []

    def agregar_medico(self, medico: Medico):
        self.medicos.append(medico)

    def agregar_paciente(self, paciente: Paciente):
        self.pacientes.append(paciente)

    def buscar_paciente(self, identificacion):
        return next((p for p in self.pacientes if p.identificacion == identificacion), None)

    def buscar_medico(self, identificacion):
        return next((m for m in self.medicos if m.identificacion == identificacion), None)
