load "dataset/dataset_pacientes.csv";
filter column "diagnostico" == "ansiedad";
filter column "edad" < 35;
aggregate average column "dias_laborados";
print;