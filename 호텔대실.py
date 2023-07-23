def solution(book_time):
    time_table = [0 for _ in range(24*60+10)]
    for book in book_time:
        s_h,s_m = book[0].split(':')
        e_h,e_m = book[1].split(':')
        start_time = int(s_h)*60 + int(s_m)
        end_time = int(e_h)*60 +int(e_m) +10
        time_table[start_time] += 1
        time_table[end_time] -=1
    num = 0
    for i in range(len(time_table)):
        num += time_table[i]
        time_table[i] = num
    answer= max(time_table)
    return answer