from collections import defaultdict
import sys
input = sys.stdin.readline


def main():
    start, end, quit = input().split(" ")
    startTime = int(start[:2])*60 + int(start[3:])
    endTime = int(end[:2])*60 + int(end[3:])
    quitTime = int(quit[:2])*60 + int(quit[3:])
    chatDict = defaultdict(int)
    ans = 0
    while True:
        inputData = input().rstrip()
        if not inputData:
            break
        time, name = inputData.split(" ")
        time = int(time[:2])*60+int(time[3:])
        if time <= startTime and chatDict[name] == 0:
            chatDict[name] = 1
        elif time >= endTime and time <= quitTime and chatDict[name] == 1:
            chatDict[name] = -1
            ans += 1
    print(ans)


main()
