from collections import defaultdict
def solution(numbers):
    costs =     [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3]
            ,[7, 1, 2, 4, 2, 3, 5, 4, 5, 6]
            ,[6, 2, 1, 2, 3, 2, 3, 5, 4, 5]
            ,[7, 4, 2, 1, 5, 3, 2, 6, 5, 4]
            ,[5, 2, 3, 5, 1, 2, 4, 2, 3, 5]
            ,[4, 3, 2, 3, 2, 1, 2, 3, 2, 3]
            ,[5, 5, 3, 2, 4, 2, 1, 5, 3, 2]
            ,[3, 4, 5, 6, 2, 3, 5, 1, 2, 4]
            ,[2, 5, 4, 5, 3, 2, 3, 2, 1, 2]
            ,[3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]
    left = 4
    right = 6
    all_dict = defaultdict(lambda :int(1e9))
    finger = (left,right)
    all_dict[finger] = 0
    
    for num in numbers:
        num = int(num)
        cur_dict = defaultdict(lambda: int(1e9))
        for finger,weight in all_dict.items():
            left,right = finger
            if right == num or left == num:
                if cur_dict[(left,right)] > weight+1:
                    cur_dict[(left,right)] = weight+1
            else:
                #오른손으로 새 숫자를 누른 경우
                if cur_dict[(left,num)]> weight+costs[right][num]:
                    cur_dict[(left,num)] = weight + costs[right][num]
                #왼손으로 새 숫자를 누른 경우
                if cur_dict[(num,right)] > weight+costs[left][num]:
                    cur_dict[(num,right)] = weight + costs[left][num]
        all_dict=cur_dict
    return min(list(all_dict.values()))