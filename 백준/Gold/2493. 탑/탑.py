n = int(input())
top = list(map(int,input().split()))
stack = []
anser=[0 for i in range(n)]

for i in range(len(top)):
    while stack:
        if stack[-1][1] > top[i]:
            anser[i] = stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append([i,top[i]])
print(*anser)


              

        


