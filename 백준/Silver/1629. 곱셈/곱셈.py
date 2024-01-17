import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
# 나머지 분배 법칙 
def func(a,b,c):
    if b == 1:
        return a%c
    elif b%2 == 0:
        return (func(a,b//2,c)**2)%c
    else:
        return (func(a,b//2,c)**2*a)%c
print(func(a,b,c))


