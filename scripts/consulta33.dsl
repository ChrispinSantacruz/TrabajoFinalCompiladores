load "dataset/dataset_pacientes.csv";
filter column "edad" < 35;
aggregate average column "salario";
print;