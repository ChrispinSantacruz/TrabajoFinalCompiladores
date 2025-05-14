load "dataset/dataset_pacientes.csv";
filter column "dias_laborados" < 15;
filter column "salario" <= 1000;
aggregate sum column "dias_laborados";
print;