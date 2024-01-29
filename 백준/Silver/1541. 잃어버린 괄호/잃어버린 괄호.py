input_data = input().split('-')
result = 0

# 첫 번째 부분은 더하기
for i in input_data[0].split('+'):
    result += int(i)

# 나머지 부분들은 빼기
for part in input_data[1:]:
    for num in part.split('+'):
        result -= int(num)

print(result)

