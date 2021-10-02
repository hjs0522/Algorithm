from itertools import permutations


def solution(user_id, banned_id):
    # 순열을 쓰는 경우 (frodo,crodo) 와 (crodo,prodo)가 다른 경우가 되므로 중복 제거
    answer = set()
    banned_num = len(banned_id)

    allCase = permutations(user_id, banned_num)

    for case in allCase:
        # 안에 있는 for문을 순회하는 동안 flag값이 변하지 않았다는 것은 경우의 수에 포함 된다는 것
        flag = True

        for i in range(len(case)):
            # 길이가 다른 경우 비교할 필요가 없음
            if len(case[i]) != len(banned_id[i]):
                flag = False
                break

            # 다른 글자가 있는경우
            for j in range(len(case[i])):
                if case[i][j] != banned_id[i][j] and banned_id[i][j] != '*':
                    flag = False
                    break
        if flag:
            answer.add(tuple(sorted(case)))
    return len(answer)
