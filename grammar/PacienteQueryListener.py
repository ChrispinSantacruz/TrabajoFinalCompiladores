# Generated from PacienteQuery.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PacienteQueryParser import PacienteQueryParser
else:
    from PacienteQueryParser import PacienteQueryParser

# This class defines a complete listener for a parse tree produced by PacienteQueryParser.
class PacienteQueryListener(ParseTreeListener):

    # Enter a parse tree produced by PacienteQueryParser#script.
    def enterScript(self, ctx:PacienteQueryParser.ScriptContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#script.
    def exitScript(self, ctx:PacienteQueryParser.ScriptContext):
        pass


    # Enter a parse tree produced by PacienteQueryParser#statement.
    def enterStatement(self, ctx:PacienteQueryParser.StatementContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#statement.
    def exitStatement(self, ctx:PacienteQueryParser.StatementContext):
        pass


    # Enter a parse tree produced by PacienteQueryParser#load_stmt.
    def enterLoad_stmt(self, ctx:PacienteQueryParser.Load_stmtContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#load_stmt.
    def exitLoad_stmt(self, ctx:PacienteQueryParser.Load_stmtContext):
        pass


    # Enter a parse tree produced by PacienteQueryParser#filter_stmt.
    def enterFilter_stmt(self, ctx:PacienteQueryParser.Filter_stmtContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#filter_stmt.
    def exitFilter_stmt(self, ctx:PacienteQueryParser.Filter_stmtContext):
        pass


    # Enter a parse tree produced by PacienteQueryParser#aggregate_stmt.
    def enterAggregate_stmt(self, ctx:PacienteQueryParser.Aggregate_stmtContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#aggregate_stmt.
    def exitAggregate_stmt(self, ctx:PacienteQueryParser.Aggregate_stmtContext):
        pass


    # Enter a parse tree produced by PacienteQueryParser#print_stmt.
    def enterPrint_stmt(self, ctx:PacienteQueryParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#print_stmt.
    def exitPrint_stmt(self, ctx:PacienteQueryParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by PacienteQueryParser#operator.
    def enterOperator(self, ctx:PacienteQueryParser.OperatorContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#operator.
    def exitOperator(self, ctx:PacienteQueryParser.OperatorContext):
        pass


    # Enter a parse tree produced by PacienteQueryParser#logic_op.
    def enterLogic_op(self, ctx:PacienteQueryParser.Logic_opContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#logic_op.
    def exitLogic_op(self, ctx:PacienteQueryParser.Logic_opContext):
        pass


    # Enter a parse tree produced by PacienteQueryParser#agg_func.
    def enterAgg_func(self, ctx:PacienteQueryParser.Agg_funcContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#agg_func.
    def exitAgg_func(self, ctx:PacienteQueryParser.Agg_funcContext):
        pass


    # Enter a parse tree produced by PacienteQueryParser#value.
    def enterValue(self, ctx:PacienteQueryParser.ValueContext):
        pass

    # Exit a parse tree produced by PacienteQueryParser#value.
    def exitValue(self, ctx:PacienteQueryParser.ValueContext):
        pass



del PacienteQueryParser