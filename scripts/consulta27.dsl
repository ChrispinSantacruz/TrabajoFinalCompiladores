load "dataset/dataset_pacientes.csv";
filter column "dias_laborados" < 15;
aggregate sum column "salario";
print;