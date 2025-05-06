load "dataset/dataset_pacientes.csv";
filter column "dias_laborados" >= 10;
aggregate sum column "salario";
print;