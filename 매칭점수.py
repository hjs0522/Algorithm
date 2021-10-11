import re


def solution(word, pages):
    urlIdx = {}
    urlScore = {}
    urlLink = {}
    word = word.lower()

    for i in range(len(pages)):
        page = pages[i].lower()
        url = re.search(
            r'<meta[^>]*content="https://([\S]*)"/>', page).group(1)
        urlIdx[url] = i
        cnt = 0
        # cnt는 단어의 갯수
        for find in re.findall(r'[a-zA-Z]+', page):
            if find == word:
                cnt += 1

        s = set()
        # s는 외부링크 정보
        for e in re.findall(r'<a href="https://[\S]*">', page):
            s.add(re.search(r'"https://([\S]*)"', e).group(1))
        s = list(s)
        urlScore[url] = list()
        # urlScore 에는 0번째에 기본점수 1번째에 외부링크수 저장
        urlScore[url].append(cnt)
        urlScore[url].append(len(s))

        for e in s:
            if e not in urlLink:
                urlLink[e] = list()
            urlLink[e].append(url)

    result = []
    for k, v in urlScore.items():
        score = v[0]
        # 만약 다른 페이지에서 이용한 경우
        if k in urlLink:
            for u in urlLink[k]:
                # 링크 점수를 더해줌
                score += urlScore[u][0] / urlScore[u][1]
        result.append([score, urlIdx[k]])
    return sorted(result, key=lambda x: [-x[0], x[1]])[0][1]
