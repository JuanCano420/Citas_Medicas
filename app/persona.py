from abc import ABC, abstractmethod
from notificacion import NotificacionEmail, NotificacionSMS, NotificacionWhatsApp

class Persona(ABC):
    def __init__(self, identificacion, nombre, celular, correo=None):
        self.identificacion = identificacion
        self.nombre = nombre
        self.celular = celular
        self.correo = correo
        self.notificaciones = []
        self._configurar_notificaciones()

    def _configurar_notificaciones(self):
        if self.celular:
            self.notificaciones.append(NotificacionSMS())
            self.notificaciones.append(NotificacionWhatsApp())
        if self.correo:
            self.notificaciones.append(NotificacionEmail())

    def notificar(self, mensaje):
        for notificacion in self.notificaciones:
            notificacion.enviar_notificacion(mensaje)

class Medico(Persona):
    def __init__(self, identificacion, nombre, telefono, especialidad, correo=None):
        super().__init__(identificacion, nombre, telefono, correo)
        self.especialidad = especialidad

    def notificar(self, mensaje):
        super().notificar(mensaje)
        print(f"Notificando al médico {self.nombre} por teléfono: {self.telefono}")

class Paciente(Persona):
    def __init__(self, identificacion, nombre, celular, correo=None):
        super().__init__(identificacion, nombre, celular, correo)
        self.medico_preferencia = None

    def asignar_medico_preferencia(self, medico):
        self.medico_preferencia = medico
        print(f"Médico de preferencia asignado: {medico.nombre}")
