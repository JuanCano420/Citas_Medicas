# email_notificacion.py
from notificacion import Notificacion

class EmailNotificacion(Notificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando correo electrónico: {mensaje}")
