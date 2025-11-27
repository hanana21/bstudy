def solution(phone_book):
    answer = True
    phone_book_set = set(phone_book)
    
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in phone_book_set:
                answer = False
                return answer
    return answer