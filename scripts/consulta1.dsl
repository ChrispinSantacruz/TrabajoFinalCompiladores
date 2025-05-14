load "dataset/dataset_pacientes.csv";
filter column "edad" >= 40;
filter column "edad" <= 25;
aggregate sum column "dias_laborados";
print;