x, y = map(int, input('Enter 2 numbers: ').split())


def arithmetic(a, b):

    total = x + y
    diff = x - y
    product = x * y
    div = x / y
    floor = x // y
    mod = x % y
    exp = x ** y

    print('\n', '*'*40, '\n')
    print(f'''Sum = {total}
Difference = {diff}
Product = {product}
Division = {div}
Floor Division = {floor}
Modulus = {mod}
Exponent = {exp} \n''')


def relation(a, b):
    eq = a == b
    noteq = a != b
    big = a > b
    small = a < b
    bigeq = a >= b
    smalleq = a <= b
    print('*' * 40, '\n')
    print(f'''Equal to: {eq}
Not equal to: {noteq}
Greater than: {big}
Less than: {small}
Greater or equal to: {bigeq}
Lesser or equal to: {smalleq}\n''')


def logical(a, b):
    print('*' * 40, '\n')
    print(f'And operator: {a < b and a < 200}')
    print(f'Or operator: {b < (a + b) or b > (a-b)}')
    print(f'Not operator: {not(a > b and a > (a-b))}\n')


arithmetic(x, y)
relation(x, y)
logical(x, y)
