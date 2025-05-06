load "dataset/dataset_pacientes.csv";
filter column "salario" > 1400;
aggregate sum column "dias_laborados";
print;