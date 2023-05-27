from collections import defaultdict
import sys
input = sys.stdin.readline


def main():
    trees = defaultdict(int)
    cnt = 0
    while True:
        tree = input().rstrip()
        if not tree:
            break
        trees[tree] += 1
        cnt += 1
    treeList = sorted(trees.keys())
    for tree in treeList:
        print("%s %.4f" % (tree, trees[tree]/cnt*100))


main()
