def solution(brown, yellow):
    for i in range(1,int(yellow**0.5)+1):
        #i는 yellow의 세로길이
        if yellow%i !=0:
            continue
        if brown == (i+yellow//i)*2+4:
            return[yellow//i+2,i+2]