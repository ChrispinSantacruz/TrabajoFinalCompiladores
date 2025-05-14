load "dataset/dataset_pacientes.csv";
filter column "dias_laborados" >= 30;
filter column "salario" > 1400;
aggregate average column "salario";
print;