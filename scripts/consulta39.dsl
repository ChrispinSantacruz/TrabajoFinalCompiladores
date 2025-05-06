load "dataset/dataset_pacientes.csv";
filter column "salario" > 1300;
aggregate sum column "dias_laborados";
print;