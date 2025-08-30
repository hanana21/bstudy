def solution(participant, completion):
    answer = {}
    
    for i in participant:  
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1
        
    for j in completion:
        answer[j] -= 1 
        
    for k in answer:
        if answer[k] == 1:
            return k

        
    
    
        