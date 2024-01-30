#회의실 배정하기
import sys
input = sys.stdin.readline
N = int(input())
times= []
for i in range(N):
    start,end = map(int,input().split())
    times.append([start,end])
times.sort(key = lambda x: x[0])
times.sort(key = lambda x: x[1])

cnt = 1
end_time = times[0][1]
for i in range(1,N):
    if times[i][0] >= end_time:
        cnt += 1
        end_time = times[i][1]
print(cnt)




