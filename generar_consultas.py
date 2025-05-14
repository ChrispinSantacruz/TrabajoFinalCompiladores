import os
import random

# Consultas con un solo filtro
consultas_simples = [
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" > 30;\naggregate sum column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "dias_laborados" >= 25;\naggregate average column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "diagnostico" == "asma";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "Perú";\naggregate sum column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" < 40;\naggregate average column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "diagnostico" == "diabetes";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "salario" > 1200;\naggregate sum column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "Chile";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" >= 60;\naggregate average column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "diagnostico" == "hipertensión";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "dias_laborados" < 20;\naggregate sum column "salario";\nprint;',
]

# Consultas con múltiples filtros - Corregidas para asegurar que cada filtro termine con punto y coma
consultas_multiples = [
    # Consultas con AND
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" > 30;\nfilter column "salario" > 1200;\naggregate average column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "Perú";\nfilter column "diagnostico" == "asma";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" < 40;\nfilter column "dias_laborados" >= 25;\naggregate sum column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "salario" > 1300;\nfilter column "pais" == "Colombia";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "diagnostico" == "hipertensión";\nfilter column "edad" >= 50;\naggregate average column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "Argentina";\nfilter column "salario" <= 1100;\naggregate sum column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" < 35;\nfilter column "diagnostico" == "ansiedad";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "dias_laborados" >= 30;\nfilter column "salario" > 1400;\naggregate average column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "México";\nfilter column "edad" < 25;\naggregate sum column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "diagnostico" == "depresión";\nfilter column "salario" <= 1000;\naggregate count column "id_paciente";\nprint;',
    
    # Consultas con OR (ahora separadas en múltiples filtros)
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "Chile";\nfilter column "pais" == "Argentina";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "diagnostico" == "asma";\nfilter column "diagnostico" == "diabetes";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" < 30;\nfilter column "edad" > 60;\naggregate average column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "dias_laborados" < 15;\nfilter column "salario" <= 1000;\naggregate sum column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "México";\nfilter column "pais" == "Colombia";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "diagnostico" == "hipertensión";\nfilter column "diagnostico" == "asma";\naggregate average column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" >= 40;\nfilter column "edad" <= 25;\naggregate sum column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "salario" > 1500;\nfilter column "salario" < 900;\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "dias_laborados" >= 28;\nfilter column "dias_laborados" <= 12;\naggregate average column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "Perú";\nfilter column "pais" == "Chile";\naggregate sum column "salario";\nprint;',
    
    # Consultas con combinaciones más complejas (ahora con múltiples filtros separados)
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" > 40;\nfilter column "salario" > 1200;\nfilter column "dias_laborados" >= 20;\naggregate average column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "Perú";\nfilter column "pais" == "Chile";\nfilter column "pais" == "Argentina";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "diagnostico" == "ansiedad";\nfilter column "edad" < 35;\naggregate average column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "salario" > 1300;\nfilter column "dias_laborados" >= 25;\naggregate sum column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "Colombia";\nfilter column "diagnostico" == "hipertensión";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" >= 50;\nfilter column "salario" <= 1100;\naggregate average column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "diagnostico" == "depresión";\nfilter column "diagnostico" == "ansiedad";\naggregate count column "id_paciente";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "dias_laborados" < 20;\nfilter column "edad" < 30;\naggregate sum column "salario";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "pais" == "México";\nfilter column "salario" > 1400;\naggregate average column "dias_laborados";\nprint;',
    'load "dataset/dataset_pacientes.csv";\nfilter column "edad" > 60;\nfilter column "diagnostico" == "diabetes";\naggregate count column "id_paciente";\nprint;',
]

# Mezclar las consultas para distribuirlas al azar
todas_consultas = consultas_simples + consultas_multiples
random.shuffle(todas_consultas)

# Crear directorio scripts si no existe
os.makedirs("scripts", exist_ok=True)

# Generar los archivos .dsl
for i, consulta in enumerate(todas_consultas, start=1):
    filename = f"scripts/consulta{i}.dsl"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(consulta)

# Mostrar estadísticas
print(f"Se han generado {len(todas_consultas)} archivos de consulta DSL en la carpeta 'scripts/':")
print(f"- {len(consultas_simples)} consultas con un solo filtro")
print(f"- {len(consultas_multiples)} consultas con múltiples filtros")
print("Las consultas han sido distribuidas aleatoriamente.")
print("\nNOTA: Se ha corregido el formato de las consultas para asegurar que cada filtro termine con punto y coma.")