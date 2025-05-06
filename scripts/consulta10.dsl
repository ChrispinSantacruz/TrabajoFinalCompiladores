load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "hipertensión";
aggregate count column "id_paciente";
print;