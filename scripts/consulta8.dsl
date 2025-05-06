load "dataset/dataset_pacientes.csv";
filter column "pais" == "Chile";
aggregate count column "id_paciente";
print;