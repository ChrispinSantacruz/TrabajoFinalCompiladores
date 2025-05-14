load "dataset/dataset_pacientes.csv";
filter column "dias_laborados" < 20;
aggregate sum column "salario";
print;