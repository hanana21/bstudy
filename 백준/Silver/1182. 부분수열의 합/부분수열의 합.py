N,S = map(int,input().split())
array = list(map(int,input().split()))
anser=0

def search(n,s,count):
    global anser
    if n == N:
        if s == S and count>0: #크기가 양수여야 count>0 들어간 갯수 체크
            anser += 1
        return 
    search(n+1,s+array[n],count+1) # 현재 값을 포함하여 더하는경우
    search(n+1,s,count)# 현재 값 포함X

search(0,0,0)
print(anser)
