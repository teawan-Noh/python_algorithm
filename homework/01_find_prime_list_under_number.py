# 소수 구하기
input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    arr = []
    for i in range(number + 1):
        if i == 0 or i == 1:
            continue
        if i == 2 or i == 3 or i == 5:
            arr.append(i)
        else:
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                continue
            arr.append(i)
    return arr


result = find_prime_list_under_number(input)
print(result)
