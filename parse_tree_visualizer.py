from antlr4 import *
from grammar.PacienteQueryLexer import PacienteQueryLexer
from grammar.PacienteQueryParser import PacienteQueryParser
from graphviz import Digraph
from antlr4.tree.Trees import Trees

def exportar_parse_tree(ruta_script, salida_png):
    # Cargar el script de prueba
    input_stream = FileStream(ruta_script, encoding='utf-8')
    
    # Crear el lexer y el parser
    lexer = PacienteQueryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PacienteQueryParser(stream)
    
    # Generar el árbol de análisis sintáctico
    tree = parser.script()
    
    # Crear un objeto Digraph para Graphviz
    dot = Digraph(comment="Parse Tree")
    agregar_nodos(dot, tree, parser, None)
    
    # Guardar la imagen como archivo PNG
    dot.render(filename=salida_png, format='png', cleanup=True)
    print(f"Parse Tree exportado a {salida_png}.png")

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

# Ejecutar con un archivo de prueba
if __name__ == "__main__":
    # Cambia la ruta al archivo DSL que deseas analizar
    ruta_script = "scripts/consulta1.dsl"
    salida_png = "parse_tree"
    exportar_parse_tree(ruta_script, salida_png)