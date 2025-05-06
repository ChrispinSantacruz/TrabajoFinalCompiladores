load "dataset/dataset_pacientes.csv";
filter column "edad" < 25;
aggregate average column "salario";
print;