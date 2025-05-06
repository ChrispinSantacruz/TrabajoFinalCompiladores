load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "ansiedad";
aggregate count column "id_paciente";
print;