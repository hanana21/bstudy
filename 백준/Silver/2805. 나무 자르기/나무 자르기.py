import sys
input =sys.stdin.readline

n,target = map(int,input().split()) # 나무수,필요한 나무길이
trees = list(map(int,input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) //2
    sum = 0

    for t in trees:
        if t >= mid:
            sum += t-mid
    if sum >= target:
        start = mid + 1
    else:
        end = mid - 1
print(end)