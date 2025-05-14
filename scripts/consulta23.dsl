load "dataset/dataset_pacientes.csv";
filter column "salario" > 1500;
filter column "salario" < 900;
aggregate count column "id_paciente";
print;