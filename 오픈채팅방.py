def solution(record):
    answer = []
    user = {}
    for r in record:
        if r.split(' ')[0] == 'Enter' or r.split(' ')[0] == 'Change':
            user[r.split(' ')[1]] = r.split(' ')[2]
    for r in record:
        if r.split(' ')[0] == "Enter":
            answer.append('{}님이 들어왔습니다.'.format(user[r.split(' ')[1]]))
        elif r.split(' ')[0] == "Leave":
            answer.append('{}님이 나갔습니다.'.format(user[r.split(' ')[1]]))

    return answer
