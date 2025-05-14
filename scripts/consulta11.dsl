load "dataset/dataset_pacientes.csv";
filter column "pais" == "Perú";
filter column "pais" == "Chile";
aggregate sum column "salario";
print;