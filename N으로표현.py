def solution(N, number):
    answer = 0
    if N == number:
        return 1

    # 최솟값이 8보다 크면 -1을 반환하므로 집합 8개까지 만듬
    s = [set() for i in range(8)]
    # 숫자를 이어 붙인 경우를 집함에 포함시켜줌
    for i, x in enumerate(s):
        x.add(int(str(N)*(i+1)))

    # n을 i개 쓰는 경우는 i-j-1개로 만든 수들의 집합과 j개로 만든 수들의 집합의 연산으로 구함
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer -= 1
    return answer
