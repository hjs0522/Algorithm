def solution(gems):
    answer = [0, 100001]
    start, end = 0, 0
    gem_kind = len(set(gems))
    gem_dict = {gems[0]: 1}

    while(start < len(gems) and end < len(gems)):
        # 아직 한 종류씩 다 못 골랐다면
        if len(gem_dict) < gem_kind:
            if end == len(gems)-1:
                break
            end += 1
            # get을 사용하면 키가 없을때 에러발생하지 않고 None반환
            # 새로운 종류의 보석을 고른 경우 value에 1대입, 원래 가지고 있는 것을 고른 경우 1 더해줌
            if gem_dict.get(gems[end]) is None:
                gem_dict[gems[end]] = 1
            else:
                gem_dict[gems[end]] += 1
        else:
            # answer에 담겨진 값 보다 거리가 작은 경우
            if end - start < answer[1] - answer[0]:
                answer = [start+1, end+1]

            # 똑같은 종류의 보석이 범위내에 하나 있는 경우 딕셔너리에서 삭제, 더 많은 경우 -1
            if gem_dict[gems[start]] == 1:
                del gem_dict[gems[start]]
            else:
                gem_dict[gems[start]] -= 1
            start += 1
    return answer
