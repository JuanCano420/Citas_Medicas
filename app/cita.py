# cita.py
class Cita:
    def __init__(self, paciente, medico, fecha, hora, motivo):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo

    def __str__(self):
        return f"Cita con el Dr. {self.medico.nombre} el {self.fecha} a las {self.hora} por {self.motivo}"

    def mover_cita(self, nueva_fecha, nueva_hora):
        if self._validar_intervalo(nueva_hora):
            self.fecha = nueva_fecha
            self.hora = nueva_hora
        else:
            raise ValueError("La nueva hora no respeta el intervalo de 20 minutos.")

    def _validar_intervalo(self, hora):
        # Implementa la lógica de validar que la hora esté en intervalos de 20 minutos
        return True  # Aquí puedes agregar la lógica real

