def solution(nums):
    type = [0] * 200001
    count = 0
    answer = 0
    
    for n in nums:
        if type[n] == 0 :
            type[n] = 1
            count += 1
        else : 
            continue
    
    if len(nums)/2 >= count :
        answer = count
    else:
        answer = len(nums)/2

    return answer