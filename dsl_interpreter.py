import csv
from grammar.PacienteQueryLexer import PacienteQueryLexer
from grammar.PacienteQueryParser import PacienteQueryParser
from grammar.PacienteQueryVisitor import PacienteQueryVisitor
from antlr4 import *
import os
from tabulate import tabulate

class DSLInterpreter(PacienteQueryVisitor):
    def __init__(self):
        self.data = []
        self.filtered_data = []
        self.filters = []
        self.aggregations = []
        self.consulta_info = {
            "id": None,
            "nombre": None,
            "tokens": [],
            "reglas": [],
            "filtros_aplicados": [],
            "valores_agregados": []
        }

    def visitScript(self, ctx):
        # Registramos la regla gramatical
        self.consulta_info["reglas"].append("script")
        # Recorremos cada declaración en el script
        for statement in ctx.statement():
            self.visit(statement)

    def visitLoad_stmt(self, ctx):
        # Registramos la regla gramatical
        self.consulta_info["reglas"].append("load_stmt")
        # Registramos el token
        self.consulta_info["tokens"].append("LOAD")
        
        # Carga el archivo CSV especificado
        path = ctx.STRING().getText().strip('"')
        try:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
            print(f"Archivo cargado: {path} ({len(self.data)} registros)")
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo {path}.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def visitFilter_stmt(self, ctx):
        # Registramos la regla gramatical
        self.consulta_info["reglas"].append("filter_stmt")
        # Registramos el token
        self.consulta_info["tokens"].append("FILTER")
        
        # Acumula filtros
        column = ctx.STRING().getText().strip('"')
        operator = ctx.operator().getText()
        value = self._get_value(ctx.value())
        self.filters.append((column, operator, value))
        print(f"Filtro acumulado: {column} {operator} {value}")
        
        # Almacenamos la información del filtro
        self.consulta_info["filtros_aplicados"].append({
            "columna": column,
            "operador": operator,
            "valor": value
        })

    def visitAggregate_stmt(self, ctx):
        # Registramos la regla gramatical
        self.consulta_info["reglas"].append("aggregate_stmt")
        # Registramos el token
        self.consulta_info["tokens"].append("AGGREGATE")
        
        # Acumula operaciones de agregación
        func = ctx.agg_func().getText()
        column = ctx.STRING().getText().strip('"')
        self.aggregations.append((func, column))
        print(f"Agregación acumulada: {func} sobre {column}")
        
        # Almacenamos la información de la agregación
        self.consulta_info["valores_agregados"].append({
            "funcion": func,
            "columna": column
        })

    def visitPrint_stmt(self, ctx):
        # Registramos la regla gramatical
        self.consulta_info["reglas"].append("print_stmt")
        # Registramos el token
        self.consulta_info["tokens"].append("PRINT")
        
        # Aplica filtros y ejecuta agregaciones al imprimir
        self._apply_filters()
        self._execute_aggregations()
        
        # Mostramos el resumen de la consulta
        self._mostrar_resumen_consulta()
        
        self._reset()

    def _apply_filters(self):
        # Aplica los filtros a los datos cargados
        self.filtered_data = self.data
        for col, op, val in self.filters:
            if col not in self.data[0]:
                print(f"Error: la columna {col} no existe.")
                continue
            try:
                if op == '>':
                    self.filtered_data = [r for r in self.filtered_data if float(r[col]) > float(val)]
                elif op == '<':
                    self.filtered_data = [r for r in self.filtered_data if float(r[col]) < float(val)]
                elif op == '>=':
                    self.filtered_data = [r for r in self.filtered_data if float(r[col]) >= float(val)]
                elif op == '<=':
                    self.filtered_data = [r for r in self.filtered_data if float(r[col]) <= float(val)]
                elif op == '==':
                    self.filtered_data = [r for r in self.filtered_data if r[col] == str(val)]
                elif op == '!=':
                    self.filtered_data = [r for r in self.filtered_data if r[col] != str(val)]
            except ValueError as e:
                print(f"Error de conversión en la columna {col}: {e}")

        if not self.filtered_data:
            print("No hay registros que coincidan con los filtros aplicados.")

    def _execute_aggregations(self):
        # Ejecuta las operaciones de agregación
        resultados = []
        for func, col in self.aggregations:
            if func == 'count':
                resultado = len(self.filtered_data)
                print(f"COUNT({col}) = {resultado}")
                resultados.append(f"COUNT({col}) = {resultado}")
            elif func == 'sum':
                total = sum(float(r[col]) for r in self.filtered_data)
                print(f"SUM({col}) = {total}")
                resultados.append(f"SUM({col}) = {total}")
            elif func == 'average':
                if self.filtered_data:
                    avg = sum(float(r[col]) for r in self.filtered_data) / len(self.filtered_data)
                    print(f"AVERAGE({col}) = {avg}")
                    resultados.append(f"AVERAGE({col}) = {avg}")
                else:
                    print(f"AVERAGE({col}) = 0")
                    resultados.append(f"AVERAGE({col}) = 0")
        
        # Guardamos los resultados de las agregaciones
        self.consulta_info["resultados_agregados"] = resultados

    def _get_value(self, val_ctx):
        # Obtiene el valor de la expresión
        if val_ctx.NUMBER():
            return float(val_ctx.NUMBER().getText())
        return val_ctx.STRING().getText().strip('"')

    def _mostrar_resumen_consulta(self):
        """Muestra un resumen detallado de la consulta ejecutada"""
        print("\n" + "="*50)
        print("RESUMEN DE LA CONSULTA")
        print("="*50)
        
        # Información básica
        if self.consulta_info["id"]:
            print(f"ID de consulta: {self.consulta_info['id']}")
        if self.consulta_info["nombre"]:
            print(f"Nombre de consulta: {self.consulta_info['nombre']}")
        
        # Tokens utilizados
        print("\nTokens utilizados:")
        for token in self.consulta_info["tokens"]:
            print(f"  - {token}")
        
        # Reglas gramaticales
        print("\nReglas gramaticales aplicadas:")
        for regla in self.consulta_info["reglas"]:
            print(f"  - {regla}")
        
        # Filtros aplicados
        if self.consulta_info["filtros_aplicados"]:
            print("\nFiltros aplicados:")
            for filtro in self.consulta_info["filtros_aplicados"]:
                print(f"  - Columna: '{filtro['columna']}' {filtro['operador']} {filtro['valor']}")
        
        # Valores agregados
        if self.consulta_info["valores_agregados"]:
            print("\nOperaciones de agregación:")
            for agg in self.consulta_info["valores_agregados"]:
                print(f"  - {agg['funcion'].upper()}('{agg['columna']}')")
        
        # Resultados
        if self.filtered_data:
            print(f"\nRegistros que cumplen los filtros: {len(self.filtered_data)}")
            
            # Mostramos todos los registros en formato de tabla
            if len(self.filtered_data) > 0:
                try:
                    self._mostrar_tabla_registros()
                except ImportError:
                    # Si no está disponible tabulate, usamos formato alternativo
                    self._mostrar_registros_formato_simple()
        
        print("="*50)

    def _mostrar_tabla_registros(self):
        """Muestra los registros en formato de tabla"""
        # Determinamos qué columnas mostrar
        columnas_a_mostrar = set()
        columnas_filtradas = set([f["columna"] for f in self.consulta_info["filtros_aplicados"]])
        
        # Siempre incluimos id y nombre si existen
        for registro in self.filtered_data:
            # Buscamos cualquier columna que pueda representar un ID de usuario
            for posible_id in ["id", "ID", "id_usuario", "usuario_id", "paciente_id", "id_paciente"]:
                if posible_id in registro:
                    columnas_a_mostrar.add(posible_id)
            if "nombre" in registro:
                columnas_a_mostrar.add("nombre")
        
        # Añadimos columnas de filtros
        columnas_a_mostrar.update(columnas_filtradas)
        
        # Si no hay filtros, incluimos todas las columnas
        if not columnas_filtradas:
            # Tomamos las columnas del primer registro
            if self.filtered_data:
                columnas_a_mostrar.update(self.filtered_data[0].keys())
        
        # Convertimos a lista y ordenamos (id y nombre primero)
        columnas_ordenadas = []
        # Primero colocamos todas las columnas de ID
        for posible_id in ["id", "ID", "id_usuario", "usuario_id", "paciente_id", "id_paciente"]:
            if posible_id in columnas_a_mostrar:
                columnas_ordenadas.append(posible_id)
                columnas_a_mostrar.remove(posible_id)
        if "nombre" in columnas_a_mostrar:
            columnas_ordenadas.append("nombre")
            columnas_a_mostrar.remove("nombre")
        columnas_ordenadas.extend(sorted(columnas_a_mostrar))
        
        # Preparamos los datos para la tabla
        datos_tabla = []
        for registro in self.filtered_data:
            fila = [registro.get(col, "") for col in columnas_ordenadas]
            datos_tabla.append(fila)
        
        # Imprimimos la tabla
        print("\nTabla de registros:")
        print(tabulate(datos_tabla, headers=columnas_ordenadas, tablefmt="grid"))
        
        # Si hay muchos registros, mostramos un mensaje
        if len(self.filtered_data) > 20:
            print(f"\nSe muestran todos los {len(self.filtered_data)} registros en formato tabla.")

    def _mostrar_registros_formato_simple(self):
        """Muestra los registros en formato simple (alternativa si no está disponible tabulate)"""
        print("\nRegistros (formato simple):")
        
        # Determinamos qué columnas mostrar
        columnas_a_mostrar = set()
        columnas_filtradas = set([f["columna"] for f in self.consulta_info["filtros_aplicados"]])
        
        # Siempre incluimos id y nombre si existen
        for registro in self.filtered_data:
            # Buscamos cualquier columna que pueda representar un ID de usuario
            for posible_id in ["id", "ID", "id_usuario", "usuario_id", "paciente_id", "id_paciente"]:
                if posible_id in registro:
                    columnas_a_mostrar.add(posible_id)
            if "nombre" in registro:
                columnas_a_mostrar.add("nombre")
        
        # Añadimos columnas de filtros
        columnas_a_mostrar.update(columnas_filtradas)
        
        # Si no hay filtros, incluimos todas las columnas
        if not columnas_filtradas:
            # Tomamos las columnas del primer registro
            if self.filtered_data:
                columnas_a_mostrar.update(self.filtered_data[0].keys())
        
        # Convertimos a lista y ordenamos (id y nombre primero)
        columnas_ordenadas = []
        # Primero colocamos todas las columnas de ID
        for posible_id in ["id", "ID", "id_usuario", "usuario_id", "paciente_id", "id_paciente"]:
            if posible_id in columnas_a_mostrar:
                columnas_ordenadas.append(posible_id)
                columnas_a_mostrar.remove(posible_id)
        if "nombre" in columnas_a_mostrar:
            columnas_ordenadas.append("nombre")
            columnas_a_mostrar.remove("nombre")
        columnas_ordenadas.extend(sorted(columnas_a_mostrar))
        
        # Imprimimos encabezado
        print(" | ".join(columnas_ordenadas))
        print("-" * (sum(len(col) for col in columnas_ordenadas) + 3 * (len(columnas_ordenadas) - 1)))
        
        # Imprimimos filas
        for registro in self.filtered_data:
            fila = [str(registro.get(col, "")) for col in columnas_ordenadas]
            print(" | ".join(fila))

    def _reset(self):
        # Resetea los filtros y agregaciones para la próxima ejecución
        self.filters = []
        self.aggregations = []
        self.consulta_info = {
            "id": None,
            "nombre": None,
            "tokens": [],
            "reglas": [],
            "filtros_aplicados": [],
            "valores_agregados": [],
            "resultados_agregados": []
        }

# Función principal para ejecutar un archivo DSL
def ejecutar_script(ruta_script):
    input_stream = FileStream(ruta_script, encoding='utf-8')
    lexer = PacienteQueryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PacienteQueryParser(stream)
    tree = parser.script()
    
    interpreter = DSLInterpreter()
    
    # Extraemos el ID y nombre de la consulta del nombre del archivo
    nombre_archivo = os.path.basename(ruta_script)
    if nombre_archivo.startswith("consulta"):
        try:
            consulta_id = nombre_archivo.replace("consulta", "").replace(".dsl", "")
            interpreter.consulta_info["id"] = consulta_id
            interpreter.consulta_info["nombre"] = f"Consulta {consulta_id}"
        except:
            pass
    
    interpreter.visit(tree)

def main():
    # Intentamos importar tabulate, si no está instalado mostramos mensaje
    try:
        import tabulate
    except ImportError:
        print("Nota: Para una mejor visualización de resultados, instale la biblioteca 'tabulate':")
        print("      pip install tabulate")
    
    print("Bienvenido al intérprete DSL para consultas de pacientes")
    while True:
        try:
            numero_consulta = input("Ingrese el número de consulta que desea ejecutar (1-40) o 'salir' para terminar: ")
            
            if numero_consulta.lower() == 'salir':
                print("¡Hasta luego!")
                break
                
            numero = int(numero_consulta)
            if 1 <= numero <= 40:
                ruta_script = f"scripts/consulta{numero}.dsl"
                try:
                    print(f"\nEjecutando consulta {numero}...")
                    ejecutar_script(ruta_script)
                    print("Consulta ejecutada con éxito\n")
                except FileNotFoundError:
                    print(f"Error: No se encontró el archivo {ruta_script}")
                except Exception as e:
                    print(f"Error al ejecutar la consulta: {e}")
            else:
                print("Error: Por favor ingrese un número entre 1 y 40")
        except ValueError:
            print("Error: Ingrese un número válido")
        
        print("-" * 50)

# Ejecutar el programa principal cuando se ejecuta el script
if __name__ == "__main__":
    main()
