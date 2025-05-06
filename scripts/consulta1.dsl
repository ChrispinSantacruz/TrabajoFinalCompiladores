load "dataset/dataset_pacientes.csv";
filter column "edad" > 30;
aggregate sum column "salario";
print;