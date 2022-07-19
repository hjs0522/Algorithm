from collections import defaultdict


def main():
    n = int(input())
    extensionDict = defaultdict(int)
    for i in range(n):
        name,extension = input().split(".")
        extensionDict[extension] += 1
    ans = sorted(extensionDict.items())
    for i in range(len(ans)):
        print(ans[i][0],end=" ")
        print(ans[i][1])
main()