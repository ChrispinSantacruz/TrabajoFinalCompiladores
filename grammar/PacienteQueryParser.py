# Generated from PacienteQuery.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,3,3,46,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,
        0,4,1,0,7,12,1,0,13,14,1,0,15,18,1,0,19,20,61,0,21,1,0,0,0,2,31,
        1,0,0,0,4,33,1,0,0,0,6,37,1,0,0,0,8,49,1,0,0,0,10,55,1,0,0,0,12,
        58,1,0,0,0,14,60,1,0,0,0,16,62,1,0,0,0,18,64,1,0,0,0,20,22,3,2,1,
        0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,
        1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,32,3,4,2,0,28,32,3,6,3,0,29,
        32,3,8,4,0,30,32,3,10,5,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,1,0,
        0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,5,1,0,0,34,35,5,19,0,0,35,36,
        5,2,0,0,36,5,1,0,0,0,37,38,5,3,0,0,38,39,5,4,0,0,39,40,5,19,0,0,
        40,41,3,12,6,0,41,45,3,18,9,0,42,43,3,14,7,0,43,44,3,6,3,0,44,46,
        1,0,0,0,45,42,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,5,2,0,0,
        48,7,1,0,0,0,49,50,5,5,0,0,50,51,3,16,8,0,51,52,5,4,0,0,52,53,5,
        19,0,0,53,54,5,2,0,0,54,9,1,0,0,0,55,56,5,6,0,0,56,57,5,2,0,0,57,
        11,1,0,0,0,58,59,7,0,0,0,59,13,1,0,0,0,60,61,7,1,0,0,61,15,1,0,0,
        0,62,63,7,2,0,0,63,17,1,0,0,0,64,65,7,3,0,0,65,19,1,0,0,0,3,23,31,
        45
    ]

class PacienteQueryParser ( Parser ):

    grammarFileName = "PacienteQuery.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'aggregate'", "'print'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'AND'", "'OR'", "'count'", "'sum'", 
                     "'average'", "'between'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "NUMBER", 
                      "WS" ]

    RULE_script = 0
    RULE_statement = 1
    RULE_load_stmt = 2
    RULE_filter_stmt = 3
    RULE_aggregate_stmt = 4
    RULE_print_stmt = 5
    RULE_operator = 6
    RULE_logic_op = 7
    RULE_agg_func = 8
    RULE_value = 9

    ruleNames =  [ "script", "statement", "load_stmt", "filter_stmt", "aggregate_stmt", 
                   "print_stmt", "operator", "logic_op", "agg_func", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    STRING=19
    NUMBER=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PacienteQueryParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PacienteQueryParser.StatementContext)
            else:
                return self.getTypedRuleContext(PacienteQueryParser.StatementContext,i)


        def getRuleIndex(self):
            return PacienteQueryParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = PacienteQueryParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 106) != 0)):
                    break

            self.state = 25
            self.match(PacienteQueryParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def load_stmt(self):
            return self.getTypedRuleContext(PacienteQueryParser.Load_stmtContext,0)


        def filter_stmt(self):
            return self.getTypedRuleContext(PacienteQueryParser.Filter_stmtContext,0)


        def aggregate_stmt(self):
            return self.getTypedRuleContext(PacienteQueryParser.Aggregate_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(PacienteQueryParser.Print_stmtContext,0)


        def getRuleIndex(self):
            return PacienteQueryParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PacienteQueryParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.load_stmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.filter_stmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.aggregate_stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.print_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Load_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PacienteQueryParser.STRING, 0)

        def getRuleIndex(self):
            return PacienteQueryParser.RULE_load_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad_stmt" ):
                listener.enterLoad_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad_stmt" ):
                listener.exitLoad_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoad_stmt" ):
                return visitor.visitLoad_stmt(self)
            else:
                return visitor.visitChildren(self)




    def load_stmt(self):

        localctx = PacienteQueryParser.Load_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_load_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(PacienteQueryParser.T__0)
            self.state = 34
            self.match(PacienteQueryParser.STRING)
            self.state = 35
            self.match(PacienteQueryParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Filter_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PacienteQueryParser.STRING, 0)

        def operator(self):
            return self.getTypedRuleContext(PacienteQueryParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(PacienteQueryParser.ValueContext,0)


        def logic_op(self):
            return self.getTypedRuleContext(PacienteQueryParser.Logic_opContext,0)


        def filter_stmt(self):
            return self.getTypedRuleContext(PacienteQueryParser.Filter_stmtContext,0)


        def getRuleIndex(self):
            return PacienteQueryParser.RULE_filter_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter_stmt" ):
                listener.enterFilter_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter_stmt" ):
                listener.exitFilter_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilter_stmt" ):
                return visitor.visitFilter_stmt(self)
            else:
                return visitor.visitChildren(self)




    def filter_stmt(self):

        localctx = PacienteQueryParser.Filter_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filter_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(PacienteQueryParser.T__2)
            self.state = 38
            self.match(PacienteQueryParser.T__3)
            self.state = 39
            self.match(PacienteQueryParser.STRING)
            self.state = 40
            self.operator()
            self.state = 41
            self.value()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13 or _la==14:
                self.state = 42
                self.logic_op()
                self.state = 43
                self.filter_stmt()


            self.state = 47
            self.match(PacienteQueryParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregate_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agg_func(self):
            return self.getTypedRuleContext(PacienteQueryParser.Agg_funcContext,0)


        def STRING(self):
            return self.getToken(PacienteQueryParser.STRING, 0)

        def getRuleIndex(self):
            return PacienteQueryParser.RULE_aggregate_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregate_stmt" ):
                listener.enterAggregate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregate_stmt" ):
                listener.exitAggregate_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregate_stmt" ):
                return visitor.visitAggregate_stmt(self)
            else:
                return visitor.visitChildren(self)




    def aggregate_stmt(self):

        localctx = PacienteQueryParser.Aggregate_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggregate_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(PacienteQueryParser.T__4)
            self.state = 50
            self.agg_func()
            self.state = 51
            self.match(PacienteQueryParser.T__3)
            self.state = 52
            self.match(PacienteQueryParser.STRING)
            self.state = 53
            self.match(PacienteQueryParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PacienteQueryParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = PacienteQueryParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(PacienteQueryParser.T__5)
            self.state = 56
            self.match(PacienteQueryParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PacienteQueryParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = PacienteQueryParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PacienteQueryParser.RULE_logic_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_op" ):
                listener.enterLogic_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_op" ):
                listener.exitLogic_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_op" ):
                return visitor.visitLogic_op(self)
            else:
                return visitor.visitChildren(self)




    def logic_op(self):

        localctx = PacienteQueryParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Agg_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PacienteQueryParser.RULE_agg_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgg_func" ):
                listener.enterAgg_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgg_func" ):
                listener.exitAgg_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgg_func" ):
                return visitor.visitAgg_func(self)
            else:
                return visitor.visitChildren(self)




    def agg_func(self):

        localctx = PacienteQueryParser.Agg_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_agg_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PacienteQueryParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(PacienteQueryParser.STRING, 0)

        def getRuleIndex(self):
            return PacienteQueryParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = PacienteQueryParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





