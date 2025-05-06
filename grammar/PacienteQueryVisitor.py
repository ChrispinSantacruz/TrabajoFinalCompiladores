# Generated from PacienteQuery.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PacienteQueryParser import PacienteQueryParser
else:
    from PacienteQueryParser import PacienteQueryParser

# This class defines a complete generic visitor for a parse tree produced by PacienteQueryParser.

class PacienteQueryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PacienteQueryParser#script.
    def visitScript(self, ctx:PacienteQueryParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PacienteQueryParser#statement.
    def visitStatement(self, ctx:PacienteQueryParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PacienteQueryParser#load_stmt.
    def visitLoad_stmt(self, ctx:PacienteQueryParser.Load_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PacienteQueryParser#filter_stmt.
    def visitFilter_stmt(self, ctx:PacienteQueryParser.Filter_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PacienteQueryParser#aggregate_stmt.
    def visitAggregate_stmt(self, ctx:PacienteQueryParser.Aggregate_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PacienteQueryParser#print_stmt.
    def visitPrint_stmt(self, ctx:PacienteQueryParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PacienteQueryParser#operator.
    def visitOperator(self, ctx:PacienteQueryParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PacienteQueryParser#logic_op.
    def visitLogic_op(self, ctx:PacienteQueryParser.Logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PacienteQueryParser#agg_func.
    def visitAgg_func(self, ctx:PacienteQueryParser.Agg_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PacienteQueryParser#value.
    def visitValue(self, ctx:PacienteQueryParser.ValueContext):
        return self.visitChildren(ctx)



del PacienteQueryParser