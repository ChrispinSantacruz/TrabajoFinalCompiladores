import csv
import random
from faker import Faker

fake = Faker()

# Generar archivo CSV con 300 registros
header = ['id_paciente', 'nombre', 'edad', 'dias_laborados', 'diagnostico', 'salario', 'fecha_ingreso', 'fecha_nacimiento', 'pais', 'telefono']
rows = []

for i in range(1, 301):
    nombre = fake.name()
    edad = random.randint(18, 70)
    dias_laborados = random.randint(20, 31)
    diagnostico = random.choice(['diabetes', 'hipertensión', 'asma', 'ansiedad', 'depresión'])
    salario = random.randint(1000, 1500)
    fecha_ingreso = fake.date_this_decade().strftime('%Y-%m-%d')
    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d')
    pais = random.choice(['Colombia', 'México', 'Argentina', 'Chile', 'Perú'])
    telefono = fake.phone_number()

    rows.append([i, nombre, edad, dias_laborados, diagnostico, salario, fecha_ingreso, fecha_nacimiento, pais, telefono])

# Escribir el CSV
with open('dataset_pacientes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Escribir encabezado
    writer.writerows(rows)   # Escribir filas de datos

print("Archivo CSV generado con 300 registros.")
