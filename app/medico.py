# medico.py
from cita import Cita

class Medico:
    def __init__(self, identificacion, nombre, celular, especialidad):
        self.identificacion = identificacion
        self.nombre = nombre
        self.celular = celular
        self.especialidad = especialidad
        self.agenda = []

    def agendar_cita(self, paciente, fecha, hora, motivo):
        nueva_cita = Cita(paciente, self, fecha, hora, motivo)
        self.agenda.append(nueva_cita)

    def cancelar_cita(self, cita):
        self.agenda.remove(cita)
