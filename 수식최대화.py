import itertools


def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n+1, e)
                   for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e)
                   for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e)
                   for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0

    oper_prior = list(itertools.permutations(['*', '+', '-'], 3))
    for oper in oper_prior:
        answer = max(abs(int(calc(oper, 0, expression))), answer)

    return answer
