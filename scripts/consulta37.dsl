load "dataset/dataset_pacientes.csv";
filter column "edad" between 20 and 40;
aggregate average column "dias_laborados";
print;