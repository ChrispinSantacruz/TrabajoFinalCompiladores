load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "depresión";
filter column "diagnostico" == "ansiedad";
aggregate count column "id_paciente";
print;