load "dataset/dataset_pacientes.csv";
filter column "edad" between 30 and 50;
aggregate average column "dias_laborados";
print;