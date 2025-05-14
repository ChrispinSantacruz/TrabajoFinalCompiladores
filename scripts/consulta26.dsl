load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "asma";
aggregate count column "id_paciente";
print;