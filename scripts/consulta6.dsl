load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "diabetes";
aggregate count column "id_paciente";
print;