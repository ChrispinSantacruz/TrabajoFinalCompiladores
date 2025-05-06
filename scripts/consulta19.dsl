load "dataset/dataset_pacientes.csv";
filter column "dias_laborados" >= 30;
aggregate sum column "salario";
print;