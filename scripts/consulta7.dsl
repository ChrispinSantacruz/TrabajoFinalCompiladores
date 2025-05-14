load "dataset/dataset_pacientes.csv";
filter column "edad" > 40;
filter column "salario" > 1200;
filter column "dias_laborados" >= 20;
aggregate average column "salario";
print;