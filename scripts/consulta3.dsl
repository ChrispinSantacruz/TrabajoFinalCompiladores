load "dataset/dataset_pacientes.csv";
filter column "dias_laborados" >= 25;
aggregate average column "salario";
print;