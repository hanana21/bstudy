def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    
    for p1,p2 in zip(sorted_phone_book,sorted_phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True