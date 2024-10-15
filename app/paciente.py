# paciente.py
class Paciente:
    def __init__(self, identificacion, nombre, celular, correo=None):
        self.identificacion = identificacion
        self.nombre = nombre
        self.celular = celular
        self.correo = correo
        self.medico_preferencia = None  # No necesita agenda

    def pedir_cita(self, medico, fecha, hora, motivo):
        medico.agendar_cita(self, fecha, hora, motivo)
        print(f"Cita solicitada con el Dr. {medico.nombre} para el {fecha} a las {hora}.")

    def cancelar_cita(self, cita):
        medico = cita.medico
        medico.cancelar_cita(cita)
        print(f"Cita con el Dr. {medico.nombre} cancelada.")

