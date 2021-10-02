def solution(word):
    answer = 0

    for i in range(len(word)):
        temp = 0
        for j in range(5-i):
            temp += 5**j

        if word[i] == 'A':
            answer += 1
        elif word[i] == 'E':
            answer += temp+1
        elif word[i] == 'I':
            answer += 2*temp+1
        elif word[i] == 'O':
            answer += 3*temp+1
        else:
            answer += 4*temp+1
    return answer
