def check(result):
    col, row = 0, 1
    for x, y, a in result:
        if a == col:
            if y != 0 and (x, y-1, col) not in result and (x-1, y, row) not in result and (x, y, row) not in result:
                return True
        else:
            if (x, y-1, col) not in result and (x+1, y-1, col) not in result and\
                    not((x-1, y, row) in result and (x+1, y, row) in result):
                return True
    return False


def solution(n, build_frame):
    answer = []
    result = set()
    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:
            result.add(item)
            if check(result):
                result.remove(item)
        else:
            result.remove(item)
            if check(result):
                result.add(item)
    answer = list(result)
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer
