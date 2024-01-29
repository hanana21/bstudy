# LCS
arr1=input() 
arr2=input()
graph = [[0]*(len(arr1)+1) for _ in range(len(arr2)+1)]

for i in range(1,len(arr2)+1):
    for j in range(1,len(arr1)+1):
        if arr2[i-1] == arr1[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j]=max(graph[i][j-1],graph[i-1][j])
print(graph[-1][-1])