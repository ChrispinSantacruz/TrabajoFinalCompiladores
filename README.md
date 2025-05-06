# Trabajo Final - Compiladores

## Christian Santacruz - Luis inguilan

## Descripción

El objetivo principal de este proyecto es desarrollar un compilador funcional que pueda analizar, interpretar y ejecutar un lenguaje de programación diseñado específicamente para este trabajo. El compilador incluye las siguientes etapas:

1. **Análisis Léxico**: Identificación de tokens en el código fuente.
2. **Análisis Sintáctico**: Verificación de la estructura gramatical del código.
3. **Análisis Semántico**: Validación de reglas semánticas del lenguaje.
4. **Generación de Código Intermedio**: Creación de una representación intermedia del programa.
5. **Optimización**: Mejora del código intermedio para mayor eficiencia.
6. **Generación de Código Final**: Traducción del código intermedio a un lenguaje ejecutable.

## Especificaciones del DSL

El DSL desarrollado está diseñado para realizar consultas dinámicas sobre archivos CSV. A continuación, se detallan las características y comandos soportados:

### Comandos del DSL

1. **Cargar datos desde un archivo CSV**:
    ```dsl
    load "archivo.csv";
    ```
    Este comando carga un archivo CSV con 10 columnas y 300 registros.

2. **Aplicar filtros sobre campos**:
    ```dsl
    filter column "campo" operador valor;
    ```
    - Operadores soportados: `>=`, `<=`, `>`, `<`, `==`, `!=`.
    - Los filtros pueden combinarse con `AND` y `OR`.

3. **Realizar operaciones de agregación**:
    ```dsl
    aggregate COUNT | SUM | AVERAGE column "campo";
    ```

4. **Imprimir resultados**:
    ```dsl
    print;
    ```
    - Los filtros y operaciones de agregación se acumulan y se ejecutan únicamente al recibir el comando `print`.

### Ejemplo de Script DSL

```dsl
load "pacientes.csv";
filter column "edad" >= 30;
filter column "sexo" == "F";
aggregate COUNT column "diagnostico";
print;
```

### Reglas del DSL

- Los filtros no se aplican inmediatamente; se acumulan hasta el comando `print`.
- La gramática y el compilador son fijos y no cambian entre consultas.
- Se deben demostrar combinaciones dinámicas de filtros y agregaciones sin modificar la definición base del DSL.

## Estructura del Proyecto

El proyecto está organizado en los siguientes directorios y archivos:

- `src/`: Contiene el código fuente del compilador.
     - `lexer/`: Implementación del análisis léxico.
     - `parser/`: Implementación del análisis sintáctico.
     - `semantic/`: Implementación del análisis semántico.
     - `codegen/`: Generación de código intermedio y final.
- `tests/`: Casos de prueba para validar el funcionamiento del compilador.
- `docs/`: Documentación adicional del proyecto.
- `README.md`: Este archivo, con la descripción general del proyecto.

## Requisitos

Para ejecutar este proyecto, se necesita:

- **Lenguaje de programación**: Python
- **Dependencias**: ANTLR4, pandas
- **Sistema operativo**: Compatible con Linux, Windows y macOS

## Instalación

1. Clonar el repositorio:
      ```bash
      git clone https://github.com/usuario/TrabajoFinalCompiladores.git
      ```
2. Navegar al directorio del proyecto:
      ```bash
      cd TrabajoFinalCompiladores
      ```
3. Instalar las dependencias:
      ```bash
      pip install -r requirements.txt
      ```

## Uso

Para ejecutar el compilador, utilice el siguiente comando:

```bash
python main.py script.dsl
```

Ejemplo de uso:

```bash
python main.py ejemplos/script1.dsl
```

## Ejemplo de Parse Tree

El siguiente es un ejemplo de un Parse Tree generado para el script:

```dsl
load "pacientes.csv";
filter column "edad" >= 30;
print;
```

El Parse Tree se genera automáticamente y puede visualizarse en formato gráfico o exportarse como archivo.

## Dataset

El archivo CSV utilizado contiene 10 columnas y 300 registros relacionados con la gestión de pacientes clínicos:

- `id_paciente`
- `nombre`
- `edad`
- `sexo`
- `diagnostico`
- `fecha_ingreso`
- `fecha_egreso`
- `medico_tratante`
- `tipo_seguro`
- `estado_actual`

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m "Descripción del cambio"`).
4. Sube tus cambios (`git push origin nueva-funcionalidad`).
5. Abre un pull request.




