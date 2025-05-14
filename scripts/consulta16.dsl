load "dataset/dataset_pacientes.csv";
filter column "pais" == "México";
filter column "salario" > 1400;
aggregate average column "dias_laborados";
print;