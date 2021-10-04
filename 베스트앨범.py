from collections import defaultdict


def solution(genres, plays):
    answer = []
    # 장르별 얼마나 재생 됬는지 기록
    playDict = {}
    # 장르 안에서 많이 재생 된 것의 번호가 몇번인지 기록
    d = {}
    for i in range(len(genres)):
        playDict[genres[i]] = playDict.get(genres[i], 0)+plays[i]
        d[genres[i]] = d.get(genres[i], [])+[(plays[i], i)]
    genreSort = sorted(playDict.items(), key=lambda x: x[1], reverse=True)
    print(playDict)
    print(d)
    for(genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0]))
        answer += [idx for (play, idx) in d[genre][:2]]
    return answer
