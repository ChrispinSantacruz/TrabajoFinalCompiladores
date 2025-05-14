load "dataset/dataset_pacientes.csv";
filter column "edad" >= 50;
filter column "salario" <= 1100;
aggregate average column "dias_laborados";
print;