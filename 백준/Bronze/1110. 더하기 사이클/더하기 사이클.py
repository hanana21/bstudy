n = int(input())
original_n = n
answer = []

while True:
    if n in answer:
        break
    answer.append(n)
    n_str = str(n).zfill(2)  # 10보다 작은 수는 앞에 0을 붙여 두 자리로 만듭니다.
    sum_result = int(n_str[0]) + int(n_str[1])
    n = int(str(n_str[1]) + str(sum_result)[-1])

print(len(answer))