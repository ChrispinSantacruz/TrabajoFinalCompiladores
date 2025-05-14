load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "hipertensión";
filter column "diagnostico" == "asma";
aggregate average column "salario";
print;