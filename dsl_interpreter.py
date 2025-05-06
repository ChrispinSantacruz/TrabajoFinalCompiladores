import csv
from grammar.PacienteQueryLexer import PacienteQueryLexer
from grammar.PacienteQueryParser import PacienteQueryParser
from grammar.PacienteQueryVisitor import PacienteQueryVisitor
from antlr4 import *

class DSLInterpreter(PacienteQueryVisitor):
    def __init__(self):
        self.data = []
        self.filtered_data = []
        self.filters = []
        self.aggregations = []

    def visitScript(self, ctx):
        # Recorremos cada declaración en el script
        for statement in ctx.statement():
            self.visit(statement)

    def visitLoad_stmt(self, ctx):
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
        # Acumula filtros
        column = ctx.STRING().getText().strip('"')  # Elimina el índice (0)
        operator = ctx.operator().getText()
        value = self._get_value(ctx.value())
        self.filters.append((column, operator, value))
        print(f"Filtro acumulado: {column} {operator} {value}")

    def visitAggregate_stmt(self, ctx):
        # Acumula operaciones de agregación
        func = ctx.agg_func().getText()
        column = ctx.STRING().getText().strip('"')
        self.aggregations.append((func, column))
        print(f"Agregación acumulada: {func} sobre {column}")

    def visitPrint_stmt(self, ctx):
        # Aplica filtros y ejecuta agregaciones al imprimir
        self._apply_filters()
        self._execute_aggregations()
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
        for func, col in self.aggregations:
            if func == 'count':
                print(f"COUNT({col}) = {len(self.filtered_data)}")
            elif func == 'sum':
                total = sum(float(r[col]) for r in self.filtered_data)
                print(f"SUM({col}) = {total}")
            elif func == 'average':
                if self.filtered_data:
                    avg = sum(float(r[col]) for r in self.filtered_data) / len(self.filtered_data)
                    print(f"AVERAGE({col}) = {avg}")
                else:
                    print(f"AVERAGE({col}) = 0")

    def _get_value(self, val_ctx):
        # Obtiene el valor de la expresión
        if val_ctx.NUMBER():
            return float(val_ctx.NUMBER().getText())
        return val_ctx.STRING().getText().strip('"')

    def _reset(self):
        # Resetea los filtros y agregaciones para la próxima ejecución
        self.filters = []
        self.aggregations = []

# Función principal para ejecutar un archivo DSL
def ejecutar_script(ruta_script):
    input_stream = FileStream(ruta_script, encoding='utf-8')
    lexer = PacienteQueryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PacienteQueryParser(stream)
    tree = parser.script()
    
    interpreter = DSLInterpreter()
    interpreter.visit(tree)

# Ejemplo de uso:
ejecutar_script("scripts/consulta6.dsl")
