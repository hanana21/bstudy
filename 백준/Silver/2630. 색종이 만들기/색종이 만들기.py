n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
blueCout = 0
WhiteCout = 0

def search(x,y,n):
    global blueCout
    global WhiteCout
    color = array[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != array[i][j]:
                search(x,y+n//2,n//2)
                search(x+n//2,y,n//2)
                search(x,y,n//2)
                search(x+n//2,y+n//2,n//2)
                return 
    if color == 0:
        WhiteCout += 1
    else:
        blueCout += 1 
search(0,0,n)
print(WhiteCout)
print(blueCout)