load "dataset/dataset_pacientes.csv";
filter column "edad" > 50;
aggregate average column "dias_laborados";
print;