from antlr4 import *
from grammar.PacienteQueryLexer import PacienteQueryLexer
from grammar.PacienteQueryParser import PacienteQueryParser
from antlr4.tree.Trees import Trees

def mostrar_arbol_textual(tree, parser, indent=0):
    texto = Trees.getNodeText(tree, parser.ruleNames)
    print("  " * indent + f"- {texto}")
    for i in range(tree.getChildCount()):
        mostrar_arbol_textual(tree.getChild(i), parser, indent + 1)

def visualizar_arbol_consulta(numero_consulta):
    try:
        ruta_script = f"scripts/consulta{numero_consulta}.dsl"
        input_stream = FileStream(ruta_script, encoding='utf-8')
        lexer = PacienteQueryLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PacienteQueryParser(stream)
        tree = parser.script()

        print(f"\nÁrbol de análisis sintáctico para consulta {numero_consulta}:")
        print(f"Archivo: {ruta_script}")
        print("-" * 50)
        mostrar_arbol_textual(tree, parser)
        print("-" * 50)
        return True
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_script}")
        return False
    except Exception as e:
        print(f"Error al procesar la consulta: {e}")
        return False

def main():
    print("Visualizador de árboles de análisis sintáctico en modo texto")
    print("=" * 60)
    
    while True:
        try:
            entrada = input("\nIngrese el número de consulta (1-40) o 'salir' para terminar: ")
            
            if entrada.lower() == 'salir':
                print("¡Hasta luego!")
                break
                
            numero = int(entrada)
            if 1 <= numero <= 40:
                visualizar_arbol_consulta(numero)
            else:
                print("Error: Por favor ingrese un número entre 1 y 40")
        except ValueError:
            print("Error: Ingrese un número válido")

if __name__ == "__main__":
    main()
