import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    P = int(input())
    point = [0]*(P+1)
    
    for _ in range(P):
        a,b = map(int,input().split())
        point[a] = b

    count = 0
    pivot = int(1e9)

    for j in range(1,len(point)):
        if pivot > point[j]:
            count += 1
            pivot = point[j]  
    print(count)



