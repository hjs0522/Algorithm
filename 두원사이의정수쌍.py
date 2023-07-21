from math import sqrt

def solution(r1, r2):
    answer = 0
    for i in range(0, r1):
        # x**2 + y**2 = r**2 이므로 y = sqrt(r**2-x**2)
        # 반지름이 r2인 원이 x가 i일때 최대 높이는 int(sqrt(r2**2 - i**2))
        # 반지름이 r1인 원이 x가 i일때 최대 높이는 int(sqrt(r1**2 - i**2))
        answer += int((r2**2 - i**2)**0.5) - int((r1**2 - i**2)**0.5)
        if int((r1**2 - i**2)**0.5) == (r1**2 - i**2)**0.5:
            answer+=1
    for i in range(r1,r2):
        answer += int((r2**2 - i**2)**0.5)
    return answer*4

print(solution(2,3))