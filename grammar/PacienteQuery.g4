grammar PacienteQuery;

script          : statement+ EOF;

statement
    : load_stmt
    | filter_stmt
    | aggregate_stmt
    | print_stmt
    ;

load_stmt       : 'load' STRING ';';
filter_stmt     : 'filter' 'column' STRING operator value (logic_op filter_stmt)? ';'; // Punto y coma obligatorio aquí
aggregate_stmt  : 'aggregate' agg_func 'column' STRING ';';
print_stmt      : 'print' ';';

operator        : '>' | '<' | '>=' | '<=' | '==' | '!=';
logic_op        : 'AND' | 'OR';
agg_func        : 'count' | 'sum' | 'average' | 'between';

value           : NUMBER | STRING;

STRING          : '"' (~["\r\n])* '"';
NUMBER          : '-'?[0-9]+ ('.' [0-9]+)?;
WS              : [ \t\r\n]+ -> skip;
