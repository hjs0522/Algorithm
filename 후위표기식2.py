"""
첫째 줄에 피연산자의 개수
둘째 줄에는 후위 표기식
셋째 줄부터는 각 피연산자에 대응하는 값

"""

def main():
    stack = []
    n = int(input())
    expression = input()
    number = []
    for i in range(n):
        number.append(int(input()))
    
    for i in expression:
        if 'A' <= i <='Z':
            stack.append(number[ord(i)-ord('A')])
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            
            if i == '+':
                stack.append(num1+num2)
            elif i == '-':
                stack.append(num1-num2)
            elif i== '*':
                stack.append(num1*num2)
            elif i == '/':
                stack.append(num1/num2)
    print('%.2f' %stack[0])
main()