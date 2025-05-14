from antlr4 import *
from grammar.PacienteQueryLexer import PacienteQueryLexer
from grammar.PacienteQueryParser import PacienteQueryParser
from graphviz import Digraph
from antlr4.tree.Trees import Trees
import os

def exportar_parse_tree(ruta_script, salida_png, ruta_dot=None):
    # Cargar el script de prueba
    input_stream = FileStream(ruta_script, encoding='utf-8')
    
    # Crear el lexer y el parser
    lexer = PacienteQueryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PacienteQueryParser(stream)
    
    # Generar el árbol de análisis sintáctico
    tree = parser.script()
    
    # Crear un objeto Digraph para Graphviz
    if ruta_dot:
        dot = Digraph(comment="Parse Tree", format='png', engine='dot')
        # Configurar la ruta al ejecutable dot
        dot.attr(executable=ruta_dot)
    else:
        dot = Digraph(comment="Parse Tree", format='png')
    
    agregar_nodos(dot, tree, parser, None)
    
    # Guardar la imagen como archivo PNG
    try:
        dot.render(filename=salida_png, cleanup=True)
        print(f"Parse Tree exportado a {salida_png}.png")
        return True
    except Exception as e:
        print(f"Error al generar el gráfico: {e}")
        print("\nSugerencias para resolver el problema:")
        print("1. Instala Graphviz desde: https://graphviz.org/download/")
        print("2. Asegúrate de que el directorio 'bin' de Graphviz esté en la variable PATH")
        print("3. Reinicia tu terminal/IDE después de la instalación")
        print("4. Especifica la ruta al ejecutable 'dot' cuando se te solicite")
        return False

def agregar_nodos(dot, tree, parser, parent_id):
    # Obtener el texto del nodo actual
    node_id = str(id(tree))
    node_text = Trees.getNodeText(tree, parser.ruleNames)
    dot.node(node_id, node_text)
    
    # Conectar con el nodo padre si existe
    if parent_id:
        dot.edge(parent_id, node_id)
    
    # Recorrer los hijos del nodo actual
    for i in range(tree.getChildCount()):
        agregar_nodos(dot, tree.getChild(i), parser, node_id)

def visualizar_arbol_grafico(numero_consulta, ruta_dot=None):
    try:
        # Asegurarse de que existe el directorio para guardar las imágenes
        os.makedirs("parse_trees", exist_ok=True)
        
        ruta_script = f"scripts/consulta{numero_consulta}.dsl"
        salida_png = f"parse_trees/consulta{numero_consulta}"
        
        print(f"\nGenerando árbol gráfico para consulta {numero_consulta}...")
        print(f"Archivo: {ruta_script}")
        
        if exportar_parse_tree(ruta_script, salida_png, ruta_dot):
            print(f"El árbol de análisis sintáctico ha sido guardado en {salida_png}.png")
            return True
        return False
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_script}")
        return False
    except Exception as e:
        print(f"Error al procesar la consulta: {e}")
        return False

def main():
    print("Visualizador gráfico de árboles de análisis sintáctico")
    print("=" * 60)
    print("Las imágenes se guardarán en el directorio 'parse_trees/'")
    
    # Preguntar por la ruta de Graphviz
    print("\nSi Graphviz no está en PATH, puede especificar la ruta al ejecutable 'dot'")
    ruta_dot = input("Ruta al ejecutable 'dot' (dejar en blanco si está en PATH): ").strip()
    
    if ruta_dot and not os.path.exists(ruta_dot):
        print(f"Advertencia: La ruta especificada '{ruta_dot}' no existe.")
        print("Se intentará usar el ejecutable 'dot' del PATH del sistema.")
        ruta_dot = None
    
    while True:
        try:
            entrada = input("\nIngrese el número de consulta (1-40) o 'salir' para terminar: ")
            
            if entrada.lower() == 'salir':
                print("¡Hasta luego!")
                break
                
            numero = int(entrada)
            if 1 <= numero <= 40:
                visualizar_arbol_grafico(numero, ruta_dot)
            else:
                print("Error: Por favor ingrese un número entre 1 y 40")
        except ValueError:
            print("Error: Ingrese un número válido")

# Ejecutar el programa principal cuando se ejecuta el script
if __name__ == "__main__":
    main()