load "dataset/dataset_pacientes.csv";
filter column "dias_laborados" < 20;
filter column "edad" < 30;
aggregate sum column "salario";
print;