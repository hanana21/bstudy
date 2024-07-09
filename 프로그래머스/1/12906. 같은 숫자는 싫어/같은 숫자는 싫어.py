def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i])
        if len(answer) >= 2 and answer[-1] == answer[-2]:
            answer.pop()
    return answer