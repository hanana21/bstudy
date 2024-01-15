n = int(input())
data = set()
for _ in range(n):
    data.add(input())
result = sorted(data,key=lambda x:(len(x),x))
for i in result:
    print(i)