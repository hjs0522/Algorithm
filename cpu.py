dict = {'ADD':'00000','ADDC':'00001','SUB':'00010','SUBC':'00011','MOV':'00100','MOVC':'00101','AND':'00110','ANDC':'00111',
'OR':'01000','ORC':'01001','NOT':'01010','MULT':'01100','MULTC':'01101','LSFTL':'01110','LSFTLC':'01111','LSFTR':'10000','LSFTRC':'10001',
'ASFTR':'10010','ASFTRC':'10011','RL':'10100','RLC':'10101','RR':'10110','RRC':'10111'}

n = int(input())
for i in range(n):
    oper = list(input().split())
    temp = ''
    temp += dict[oper[0]]
    temp += '0'
    rd = bin(int(oper[1]))[2:].rjust(3,'0')
    temp += rd
    ra = bin(int(oper[2]))[2:].rjust(3,'0')
    temp += ra
    if temp[4] == '0':
        rb = bin(int(oper[3]))[2:].rjust(3,'0')
        temp += rb
        temp += '0'
    else:
        c = bin(int(oper[3]))[2:].rjust(4,'0')
        temp+= c
    print(temp)