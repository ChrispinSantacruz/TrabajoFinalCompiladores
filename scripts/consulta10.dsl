load "dataset/dataset_pacientes.csv";
filter column "edad" < 35;
filter column "diagnostico" == "ansiedad";
aggregate count column "id_paciente";
print;