N = int(input())
signal = input()
answer = ''

signal_length= N// 5 # 40이면 8

idx = 0
while idx < signal_length:

    if signal[idx] == '.': # 공백
        idx += 1
        continue
    #여기부터는 다 숫자.
    if signal[idx+1*signal_length] == '.': #2번째가공백. =>2,3,7
        if signal[idx+2*signal_length] == '.': #3번째 공백 => 2,3은 아니고 7은 맞음
            answer += '7'
        elif signal[idx + 3 * signal_length] == '.':  # 4번째 공백 => 3
            answer += '3'
        else:
            answer += '2'
        idx += 4 # 3개랑 공백 무조건 1개니까 4를 더해줌.
        continue
    if signal[idx+3*signal_length] == '.': # 4번째가 공백 => 4,5,9
        if signal[idx+4*signal_length] == '.': # => 4
            answer += '4'
        elif signal[idx + 2 + 1*signal_length] == '.':
            answer += '5'
        else:
            answer += '9'
        idx += 4 # 3개랑 공백 무조건 1개니까 4를 더해줌.
        continue
    #0,1,6,8
    if idx + 1 >= signal_length:
        answer += '1'
        break
    if signal[idx+1] == '.':
        answer += '1'
        idx += 2
        continue
    elif signal[idx+1+2*signal_length] == '.':
        answer += '0'
    elif signal[idx+2+1*signal_length] == '.':
        answer += '6'
    else:
        answer += '8'
    idx += 4
    continue

print(answer)