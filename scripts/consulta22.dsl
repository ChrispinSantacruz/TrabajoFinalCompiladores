load "dataset/dataset_pacientes.csv";
filter column "pais" == "México";
filter column "edad" < 25;
aggregate sum column "dias_laborados";
print;