def binaryserach(array,start,end,target): #데이터가 십만 넘어가면 이진탐색이 빠르다
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] >target: # 타겟보다 값이 크니까 앞으로 땡겨져야
            end = mid - 1
        else:
            start = mid + 1 # 타겟보다 값이 작으니까 뒤로 땡겨져야
    return None

n = int(input())
array = list(map(int,input().split()))
array.sort() # 정렬된 상태에서 이진탐색해야함

m = int(input())
target_datas =list(map(int,input().split()))
for target in target_datas:
    result = binaryserach(array,0,len(array)-1,target)
    if result == None:
        print(0)
    else:
        print(1)
