# rich_interface.py
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def mostrar_menu():
    console.print("[bold green]--- Menú Principal ---[/bold green]", style="bold underline")
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Opción", style="dim", width=12)
    table.add_column("Descripción", justify="left")
    
    table.add_row("1", "Agregar persona")
    table.add_row("2", "Pedir cita")
    table.add_row("3", "Cancelar cita")
    table.add_row("4", "Asignar médico de preferencia")
    table.add_row("5", "Ver citas pendientes")
    table.add_row("6", "Salir")
    
    console.print(table)
