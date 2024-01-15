import sys
stack = []
input = sys.stdin.readline
n=int(input())

for i in range(n):
    input_data = input().split()
    if input_data[0] =='push' :
        stack.append(input_data[1])
    elif input_data[0] == 'pop':
        if len(stack) == 0:
            print (-1)
        else:
            print(stack.pop())
    elif input_data[0] == 'size':
        print(len(stack))
    elif input_data[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif input_data[0] == 'top':
        if len(stack) == 0:
            print (-1)
        else:
            print(stack[-1])

