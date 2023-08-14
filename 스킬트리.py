def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx = 0
        skill = list(skill)
        pre = []
        flag = True
        for s in skill_tree:
            if s not in skill:
                continue
            else:
                if s in pre:
                    continue
                if skill[idx] == s:
                    idx+=1
                    pre.append(s)
                else:
                    flag = False
                    break
        if flag:
            answer+=1
    return answer