import ast
import operator as op

OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
    ast.USub: op.neg
}


def eval_(node):
    if isinstance(node, ast.Num):
        return node.n

    elif isinstance(node, ast.BinOp):
        return OPERATORS[type(node.op)](eval_(node.left), eval_(node.right))

    elif isinstance(node, ast.UnaryOp):
        return OPERATORS[type(node.op)](eval_(node.operand))

    else:
        raise TypeError(node)


def eval_expr(expr):
    return eval_(ast.parse(expr, mode='eval').body)


all_sum = 0

with open('calc.txt', 'r', encoding='utf-8') as f_calc:
    for line in f_calc:
        line = line.replace('\n', '')
        arr = line.split()
        try:
            all_sum += eval_expr(line)
        except (SyntaxError, TypeError):
            msg = f'Обнаружена ошибка в строке: {line}  Хотите исправить? '
            answer = input(msg).lower()
            if answer == 'да' or answer == 'yes':
                new_line = input('Введите исправленную строку: ')
                all_sum += eval_expr(new_line)

print('Сумма результатов:', all_sum)
