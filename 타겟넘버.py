def solution(numbers, target):
    n = len(numbers)
    cnt = 0

    def dfs(L, total):
        if L == n:
            # 타겟 넘버를 만든 경우
            if total == target:
                nonlocal cnt
                cnt += 1
        else:
            # 더하거나 빼거나
            dfs(L+1, total+numbers[L])
            dfs(L+1, total-numbers[L])

    dfs(0, 0)
    return cnt
