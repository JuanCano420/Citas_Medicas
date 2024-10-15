# data_loader.py
import csv
import json

def cargar_datos_csv(archivo_csv):
    with open(archivo_csv, newline='') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            # Lógica para cargar pacientes o médicos
            pass

def cargar_datos_json(archivo_json):
    with open(archivo_json) as jsonfile:
        datos = json.load(jsonfile)
        # Lógica para cargar citas
        pass
