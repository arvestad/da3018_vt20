#
# A recursive descent parser for recognising S-expressions
#
def parse_sexpr(terminals):
    token, *more = terminals
    if token.isnumeric():
        return more
    elif token == '(':
        rest = parse_operator(more)
        rest = parse_sexpr(rest)
        rest = parse_sexpr(rest)
        rest = parse_rest_expr(rest)
        return rest

def parse_operator(terminals):
    token, *more = terminals
    if token in ['+', '-', '*', '/']:
        return more

def parse_rest_expr(terminals):
    token, *more = terminals
    if token == ')':
        return more
    else:
        rest = parse_sexpr(terminals)
        rest = parse_rest_expr(rest)
        return rest


def main():
    in1 = ['7']
    parse_sexpr(in1)
    in2 = ['(', '+', '(', '*', '7', '2', ')', '5', ')']
    parse_sexpr(in2)

    print('This will cause an exception because the input does not follow the grammar.')
    in3 = ['(', '(']
    parse_sexpr(in3)

if __name__ == '__main__':
    main()
