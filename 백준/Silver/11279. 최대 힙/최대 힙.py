from queue import PriorityQueue
import sys
input = sys.stdin.readline
n=int(input())
queue= PriorityQueue()

for i in range(n):
    input_data = int(input())
    if input_data == 0:
        if queue.empty():
            print(0)
        else:
            print(-(queue.get()))
    else:
        queue.put(-input_data)
