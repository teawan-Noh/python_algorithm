def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


result = find_max_occurred_alphabet("Hello my name is sparta")
print(max(result))
# print("정답 = a 현재 풀이 값 =", result())
# print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
# print("정답 = s 현재 풀이 값 =", result("best of best sparta"))