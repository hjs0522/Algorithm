#col번째 컬럼의 값을 기준으로 오름차순 정렬
#첫번째 컬럼의 값을 기준으로 내림차순 정렬
def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col-1],-x[0]))
    si_arr = []
    for i in range(row_begin-1,row_end):
        si = 0
        for d in data[i]:
            si+= d%(i+1)
        si_arr.append(si)
    answer = si_arr[0]
    for i in range(1,len(si_arr)):
        answer ^= si_arr[i]
    return answer