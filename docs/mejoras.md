# Mejoras Implementadas en el Proyecto

Este documento detalla los cambios realizados en el proyecto para cumplir con los requerimientos especificados. A continuación, se describen las 12 modificaciones principales y dos mejoras adicionales realizadas.

## Cambios Solicitados

### 1. Corregir las Notificaciones
- **Descripción**: Los datos de contacto (correo, celular, etc.) fueron asignados a la clase `Persona` en lugar de la clase `Notificación`.
- **Acción**: El método `enviar_notificación()` fue heredado por todas las formas de notificación (correo, SMS, y WhatsApp).
- **Modificación realizada en**: `persona.py` y `notificaciones.py`.

### 2. Agregar WhatsApp como una forma de Notificación
- **Descripción**: Se agregó WhatsApp como una nueva forma de notificación.
- **Acción**: Se creó una clase `NotificacionWhatsApp` que extiende la funcionalidad de notificaciones.
- **Modificación realizada en**: `notificaciones.py`.

### 3. Corregir Agenda - Cita
- **Descripción**: La agenda se eliminó de la clase `Paciente`. Se implementó una agenda general en el hospital, con agendas específicas para cada médico.
- **Acción**: Se reorganizó la clase `Cita` y `Agenda`, asociando las citas a los médicos y no a los pacientes.
- **Modificación realizada en**: `hospital.py` y `medico.py`.

### 4. Corregir Usuarios
- **Descripción**: Se eliminó el concepto de `Usuario`. Ahora solo hay `Pacientes` en el sistema.
- **Acción**: Se ajustó el código para manejar solo pacientes.
- **Modificación realizada en**: `persona_factory.py`.

### 5. Crear métodos `buscar_paciente()` y `buscar_medico()` en el hospital
- **Descripción**: Se agregaron los métodos `buscar_paciente()` y `buscar_medico()` en la clase `Hospital`.
- **Acción**: Los métodos buscan pacientes y médicos por su identificación.
- **Modificación realizada en**: `hospital.py`.

### 6. Corregir agendar y cancelar cita
- **Descripción**: Se trasladó la funcionalidad de agendar y cancelar citas a la clase `Medico`, ya que la agenda pertenece al médico.
- **Acción**: Se movieron los métodos `agendar_cita()` y `cancelar_cita()` de la clase `Paciente` a la clase `Medico`.
- **Modificación realizada en**: `medico.py`.

### 7. Cómo buscar los datos de una cita
- **Descripción**: Ahora las citas se buscan tanto desde el paciente como desde el hospital.
- **Acción**: Se implementó una búsqueda más eficiente desde ambas entidades.
- **Modificación realizada en**: `hospital.py` y `paciente.py`.

### 8. Revisar qué hacer con "mover" citas
- **Descripción**: Se añadió la opción de mover citas a una nueva fecha y hora desde la clase `Medico`.
- **Acción**: Se implementó el método `mover_cita()` en la clase `Medico`.
- **Modificación realizada en**: `medico.py`.

### 9. Mejorar la interfaz de texto utilizando la librería `Rich`
- **Descripción**: Se mejoró la presentación de menús, la captura de datos y los reportes usando la librería `Rich`.
- **Acción**: Se implementaron menús con colores y formatos atractivos, y la visualización de citas y pacientes se mejoró.
- **Modificación realizada en**: `rich_interface.py`.

### 10. Cargar datos iniciales desde archivos CSV y JSON
- **Descripción**: Se agregó funcionalidad para cargar pacientes, médicos y citas desde archivos CSV y JSON.
- **Acción**: Se implementó un cargador de datos en la clase `Hospital`.
- **Modificación realizada en**: `hospital.py`.

### 11. Citas con Fecha y Hora en intervalos de 20 minutos
- **Descripción**: Las citas ahora se registran con fecha y hora, y los intervalos entre citas son de 20 minutos.
- **Acción**: Se añadió validación para asegurar que las citas se programen en intervalos de 20 minutos.
- **Modificación realizada en**: `cita.py`.

### 12. Selección de especialidad para nueva cita
- **Descripción**: El sistema ahora permite que el paciente seleccione una especialidad, y se le muestran los médicos disponibles en esa especialidad.
- **Acción**: Se implementó un filtro por especialidad en la selección de médicos.
- **Modificación realizada en**: `main.py` y `hospital.py`.

## Mejoras Propias

### A. Implementar validaciones de datos
- **Descripción**: Se añadieron validaciones adicionales para las entradas de usuario, como formatos de fechas y horas.
- **Acción**: Se creó una clase de validación que asegura que los datos ingresados sigan los formatos adecuados.
- **Modificación realizada en**: `validaciones.py`.

### B. Mejorar el manejo de errores
- **Descripción**: Se mejoró el manejo de excepciones y errores para hacer el sistema más robusto.
- **Acción**: Se añadieron bloqueos `try-except` en todo el sistema para manejar errores comunes, como datos faltantes o identificaciones inválidas.
- **Modificación realizada en**: `main.py`, `hospital.py` y `medico.py`.
