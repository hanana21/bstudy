# 괄호의 값
bracket_list = input()
stack = []
ans = 0
tmp = 1

for bracket in range(len(bracket_list)):
    if bracket_list[bracket] == '(':
        tmp *= 2
        stack.append('(')
        
    elif bracket_list[bracket] == '[':
        tmp *= 3
        stack.append('[')

    elif bracket_list[bracket] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if bracket_list[bracket-1] == '(':
            ans += tmp
        tmp //= 2
        stack.pop()

    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if bracket_list[bracket-1] == '[':
            ans += tmp
        tmp //= 3
        stack.pop()
if stack:
    print(0)
else:
    print(ans)