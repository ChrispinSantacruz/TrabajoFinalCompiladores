from antlr4 import *
from grammar.PacienteQueryLexer import PacienteQueryLexer
from grammar.PacienteQueryParser import PacienteQueryParser
from antlr4.tree.Trees import Trees

def mostrar_arbol_textual(tree, parser, indent=0):
    texto = Trees.getNodeText(tree, parser.ruleNames)
    print("  " * indent + f"- {texto}")
    for i in range(tree.getChildCount()):
        mostrar_arbol_textual(tree.getChild(i), parser, indent + 1)

if __name__ == "__main__":
    ruta_script = "scripts/consulta1.dsl"
    input_stream = FileStream(ruta_script, encoding='utf-8')
    lexer = PacienteQueryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PacienteQueryParser(stream)
    tree = parser.script()

    print("Árbol de análisis sintáctico:")
    mostrar_arbol_textual(tree, parser)
