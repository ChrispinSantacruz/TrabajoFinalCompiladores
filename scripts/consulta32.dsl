load "dataset/dataset_pacientes.csv";
filter column "pais" == "México";
aggregate count column "id_paciente";
print;