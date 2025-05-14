load "dataset/dataset_pacientes.csv";
filter column "dias_laborados" >= 28;
filter column "dias_laborados" <= 12;
aggregate average column "salario";
print;