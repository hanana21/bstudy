# 왼쪽 오른쪽 나눠서 힙을 만든다. => 왼쪽힙의 우선순위가 큰게 중간값이 되도록 한다.
import heapq
import sys 

input = sys.stdin.readline
n = int(input())
leftheap = []
rightheap = []

for i in range(n):
    input_data = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap,-input_data)
    else:
        heapq.heappush(rightheap,input_data)
    if leftheap and rightheap and leftheap[0] * -1 > rightheap[0]:
        min = heapq.heappop(rightheap)
        max = heapq.heappop(leftheap)

        heapq.heappush(leftheap,min* -1)
        heapq.heappush(rightheap,max* -1)

    print(leftheap[0]*-1)
        
