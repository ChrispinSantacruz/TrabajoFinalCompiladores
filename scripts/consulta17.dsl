load "dataset/dataset_pacientes.csv";
filter column "pais" == "Colombia";
filter column "diagnostico" == "hipertensión";
aggregate count column "id_paciente";
print;