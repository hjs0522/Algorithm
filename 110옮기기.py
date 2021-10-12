def solution(s):
    answer = []
    for i in range(len(s)):
        stack = []
        cnt = 0
        for j in range(len(s[i])):
            if s[i][j] == '0':
                if len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1':
                    cnt += 1
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(s[i][j])
            else:
                stack.append(s[i][j])
        if cnt == 0:
            answer.append(s[i])
        else:
            from collections import deque
            q = deque()
            while stack:
                if stack[-1] == '1':
                    q.append(stack.pop())
                elif stack[-1] == '0':
                    break

            while cnt > 0:
                q.appendleft('0')
                q.appendleft('1')
                q.appendleft('1')
                cnt -= 1

            while stack:
                q.appendleft(stack.pop())
            answer.append(''.join(q))

    return answer
