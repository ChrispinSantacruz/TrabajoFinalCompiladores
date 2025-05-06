load "dataset/dataset_pacientes.csv";
filter column "pais" == "Colombia";
aggregate count column "id_paciente";
print;