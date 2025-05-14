load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "depresión";
filter column "salario" <= 1000;
aggregate count column "id_paciente";
print;