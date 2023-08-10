def solution(numbers):
    answer = []
    for num in numbers:
        if num == 0:
            answer.append(1)
            continue
        if num == 1:
            answer.append(2)
            continue
        bin_num = list(bin(num)[2:])
        flag = False
        for i in range(len(bin_num)-1,-1,-1):
            if bin_num[i] == '0':
                if i != len(bin_num)-1:
                    bin_num[i+1] = '0'
                bin_num[i] = '1'
                flag = True
                break
        if flag == False:
            answer.append(int('10'+''.join(bin_num)[1:],2))
        else:
            answer.append(int(''.join(bin_num),2))
    return answer