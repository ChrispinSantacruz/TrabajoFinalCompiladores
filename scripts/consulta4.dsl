load "dataset/dataset_pacientes.csv";
filter column "pais" == "Perú";
aggregate sum column "salario";
print;