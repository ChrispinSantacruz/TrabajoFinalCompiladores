load "dataset/dataset_pacientes.csv";
filter column "edad" >= 60;
aggregate average column "salario";
print;