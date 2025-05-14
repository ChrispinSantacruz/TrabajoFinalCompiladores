load "dataset/dataset_pacientes.csv";
filter column "pais" == "Argentina";
filter column "salario" <= 1100;
aggregate sum column "dias_laborados";
print;