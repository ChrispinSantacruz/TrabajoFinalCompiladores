load "dataset/dataset_pacientes.csv";
filter column "salario" > 1300;
filter column "pais" == "Colombia";
aggregate count column "id_paciente";
print;