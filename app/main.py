# main.py
from hospital import Hospital
from persona_factory import PersonasFactory
from rich_interface import mostrar_menu

hospital = Hospital()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tipo_persona = input("Ingrese el tipo de persona (médico o paciente): ")
        identificacion = input("Ingrese la identificación: ")
        nombre = input("Ingrese el nombre: ")
        celular = input("Ingrese el celular: ")

        if tipo_persona.lower() == "medico":
            especialidad = input("Ingrese la especialidad: ")
            persona = PersonasFactory.crear_persona("medico", identificacion, nombre, celular, especialidad)
            hospital.agregar_medico(persona)
        elif tipo_persona.lower() == "paciente":
            correo = input("Ingrese el correo: ")
            persona = PersonasFactory.crear_persona("paciente", identificacion, nombre, celular, correo=correo)
            hospital.agregar_paciente(persona)
        else:
            print("Tipo de persona inválido.")

    elif opcion == "2":
        id_paciente = input("Ingrese la identificación del paciente: ")
        id_medico = input("Ingrese la identificación del médico: ")
        fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
        hora = input("Ingrese la hora de la cita (HH:MM): ")
        motivo = input("Ingrese el motivo de la cita: ")

        paciente = hospital.buscar_paciente(id_paciente)
        medico = hospital.buscar_medico(id_medico)

        if paciente and medico:
            paciente.pedir_cita(medico, fecha, hora, motivo)
        else:
            print("Paciente o médico no encontrado.")

    elif opcion == "3":
        id_paciente = input("Ingrese la identificación del paciente: ")
        paciente = hospital.buscar_paciente(id_paciente)

        if paciente:
            print("Citas pendientes:")
            for i, cita in enumerate(paciente.agenda):
                print(f"{i+1}. {cita}")

            opcion_cita = int(input("Seleccione la cita a cancelar: "))
            if 1 <= opcion_cita <= len(paciente.agenda):
                cita_a_cancelar = paciente.agenda[opcion_cita - 1]
                paciente.cancelar_cita(cita_a_cancelar)
            else:
                print("Opción inválida.")
        else:
            print("Paciente no encontrado.")

    elif opcion == "4":
        id_paciente = input("Ingrese la identificación del paciente: ")
        id_medico = input("Ingrese la identificación del médico: ")

        paciente = hospital.buscar_paciente(id_paciente)
        medico = hospital.buscar_medico(id_medico)

        if paciente and medico:
            paciente.asignar_medico_preferencia(medico)
        else:
            print("Paciente o médico no encontrado.")

    elif opcion == "5":
        id_paciente = input("Ingrese la identificación del paciente: ")
        paciente = hospital.buscar_paciente(id_paciente)

        if paciente:
            print("Citas pendientes:")
            for cita in paciente.agenda:
                print(cita)
        else:
            print("Paciente no encontrado.")

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")
