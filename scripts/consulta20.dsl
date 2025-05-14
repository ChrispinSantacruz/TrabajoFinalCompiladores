load "dataset/dataset_pacientes.csv";
filter column "edad" < 40;
filter column "dias_laborados" >= 25;
aggregate sum column "salario";
print;