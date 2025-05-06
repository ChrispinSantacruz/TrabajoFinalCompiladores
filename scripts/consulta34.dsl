load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "depresión";
aggregate count column "id_paciente";
print;