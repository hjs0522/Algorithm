def solution(numbers):
    answer = [0]*len(numbers)
    stack = []
    
    for idx,number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(idx)
    
    while stack:
        answer[stack.pop()] = -1
            
    return answer