def solution(storey):
    answer = 0
    while storey:
        value = storey%10
        if value > 5:
            answer += (10-value)
            storey += 10
        elif value < 5:
            answer += value
        else:
            if (storey//10) %10>4:
                storey += 10
            answer += value
        storey //= 10
    return answer