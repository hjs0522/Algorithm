"""
시에 나오는 단어들의 첫 글자를 대문자로 바꾼 뒤 순서대로 이어서 제목을 만든다.
앞으로 스페이스 바와 영자판을 누를 수 있는 횟수가 정해져 있다.
같은 문자가 연속으로 나오거나 빈칸이 연속으로 나오는 경우 한번만 사용해서 좀 더 효율적으로 쓸 수 있다.
내용과 스페이스 바와 영자판을 누를 수 있는 횟수가 주어졌을 때,
시의 내용과 제목을 모두 기록할 수 있다면 시의 제목을 출력 아니면 -1 출력
"""

from collections import defaultdict



def main():
    content = input()
    space = int(input())
    keyboard = list(map(int,input().split()))
    keyboardDict = defaultdict(int)
    keyboardDict[" "]= space
    ans = ""
    for i in range(len(keyboard)):
        keyboardDict[chr(i+97)] = keyboard[i]
    
    if keyboardDict[content[0].lower()] >= 1:
        keyboardDict[content[0].lower()] -=1
        ans += content[0].upper()
    else:
        return -1
        
    for i in range(1,len(content)):
        if content[i] == content[i-1]:
            continue
        
        if keyboardDict[content[i].lower()] >=1:
            keyboardDict[content[i].lower()] -=1
            if content[i-1] == " ":
                ans += content[i].upper()
        else:
            return -1
            
    if ans[0].lower() != content[-1]:
        if keyboardDict[ans[0].lower()] >= 1:
            keyboardDict[ans[0].lower()] -=1
        else:
            return -1
    
    for i in range(1,len(ans)):
        if ans[i] == ans[i-1]:
            continue
        
        if keyboardDict[ans[i].lower()] >=1:
            keyboardDict[ans.lower()] -=1
        else:
            return -1
            
    return ans
print(main())