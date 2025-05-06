load "dataset/dataset_pacientes.csv";
filter column "pais" == "Argentina";
aggregate count column "id_paciente";
print;