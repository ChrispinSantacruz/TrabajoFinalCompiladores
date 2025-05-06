load "dataset/dataset_pacientes.csv";
filter column "edad" >= 40;
aggregate average column "salario";
print;