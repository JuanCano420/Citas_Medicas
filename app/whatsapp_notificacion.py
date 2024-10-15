# whatsapp_notificacion.py
from notificacion import Notificacion

class NotificacionWhatsApp(Notificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando WhatsApp: {mensaje}")
