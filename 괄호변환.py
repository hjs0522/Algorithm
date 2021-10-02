def solution(p):
    answer = ''
    u = ''
    v = ''
    # 입력이 빈 문자열인 경우, 빈 문자열 반환
    if p == '':
        return ''

    while(True):
        u_aright = 0
        flag = True
        idx = 0
        # 균형잡힌 문자열 u 만들기
        while(True):
            u += p[idx]
            idx += 1
            if(u[-1] == '('):
                u_aright += 1
            else:
                u_aright -= 1
            if(u_aright < 0):
                flag = False
            if(u.count('(') == u.count(')')):
                break
        # 문자열 w에서 u가 빠진 v
        v = p[idx:]

        # 문자열 u가 올바른 균형잡힌 괄호 분자열인 경우 문자열 v에 대해 1단계부터 다시 수행후 결과 반환
        if flag == True:
            answer = u + solution(v)
            return answer
        else:
            # 문자열 u가 올바른 괄호 문자열이 아닌경우
            new_u = ''
            # u의 첫 번째와 마지막 문자 제거, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙힘
            for i in range(1, len(u)-1):
                if(u[i] == '('):
                    new_u += ')'
                else:
                    new_u += '('
            answer = '('+solution(v)+')'+new_u
            return answer
