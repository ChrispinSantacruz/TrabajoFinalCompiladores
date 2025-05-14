load "dataset/dataset_pacientes.csv";
filter column "salario" > 1300;
filter column "dias_laborados" >= 25;
aggregate sum column "salario";
print;