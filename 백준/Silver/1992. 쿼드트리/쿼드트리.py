n = int(input())
array = [list(map(int, input().rstrip())) for _ in range(n)]

def search(x, y, n):
    num = array[x][y]
    if n == 1:
        print(num, end='')
        return
    
    same_num = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != array[i][j]:
                same_num = False
                break

    if same_num:
        print(num, end='')
    else:
        print('(', end='')
        search(x, y, n//2)
        search(x, y+n//2, n//2)
        search(x+n//2, y, n//2)
        search(x+n//2, y+n//2, n//2)
        print(')', end='')

search(0, 0, n)
