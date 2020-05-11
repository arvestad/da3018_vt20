#
# A recursive descent parser for evaluating S-expressions
#
def parse_sexpr(terminals):
    token, *more = terminals
    if token.isnumeric():
        return int(token), more
    elif token == '(':
        op, rest = parse_operator(more)
        elem1, rest = parse_sexpr(rest)
        elem2, rest = parse_sexpr(rest)
        elems, rest = parse_rest_expr(rest)
        operands = [elem1, elem2]
        operands.extend(elems)
        val = evaluate(op, operands)
        return val, rest

def parse_operator(terminals):
    token, *more = terminals
    if token in ['+', '-', '*', '/']:
        return token, more

def parse_rest_expr(terminals):
    token, *more = terminals
    if token == ')':
        return [], more
    else:
        val1, rest = parse_sexpr(terminals)
        more_vals, rest = parse_rest_expr(rest)
        return [val1].extend(more_vals), rest


def evaluate(op, operands):
    import functools
    import operator
    op_map = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    f = op_map[op]
    result = functools.reduce(f, operands)
    return result



def main():
    in1 = ['7']
    in2 = ['(', '+', '(', '*', '7', '2', ')', '5', ')']
    in3 = ['(', '+', ')']
    for input_terminals in [in1, in2, in3]:
        print(f'Evaluation of {input_terminals}:')
        try:
            result, remaining = parse_sexpr(input_terminals)
            print(f'\tResult is {result}')
        except:
            print(f'Parsing failed, so the input does not follow the grammar.')
        print()


if __name__ == '__main__':
    main()
