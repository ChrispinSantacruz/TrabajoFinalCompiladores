load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "hipertensión";
filter column "edad" >= 50;
aggregate average column "salario";
print;