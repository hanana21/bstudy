array = [int(input()) for _ in range(9)]
array.sort()
num = sum(array) - 100
index1=0
index2=0

for i in range(len(array)):
    for j in range(len(array)):
        if array[i]+array[j] == num:
            index1 = i
            index2 = j
            break
array.remove(array[index1])
array.remove(array[index2])

for i in array:
    print(i)





