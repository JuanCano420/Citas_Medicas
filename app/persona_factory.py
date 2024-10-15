# persona_factory.py
from medico import Medico
from paciente import Paciente

class PersonasFactory:
    @staticmethod
    def crear_persona(tipo_persona, identificacion, nombre, celular, especialidad=None, correo=None):
        if tipo_persona.lower() == "medico":
            return Medico(identificacion, nombre, celular, especialidad, correo)
        elif tipo_persona.lower() == "paciente":
            return Paciente(identificacion, nombre, celular, correo)
        else:
            raise ValueError(f"Tipo de persona '{tipo_persona}' inválido. Solo se aceptan 'medico' o 'paciente'.")

