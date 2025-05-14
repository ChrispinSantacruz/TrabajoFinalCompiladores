load "dataset/dataset_pacientes.csv";
filter column "edad" > 30;
filter column "salario" > 1200;
aggregate average column "dias_laborados";
print;