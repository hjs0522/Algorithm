def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book)
    
    for i in range(n-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return answer