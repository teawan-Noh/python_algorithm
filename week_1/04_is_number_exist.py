def is_number_exist(number, array):
    if number in array:
        return True
    else:
        return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3,[3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7,[6,6,6]))
print("정답 = True 현재 풀이 값 =", result(6,[6,9,2,7,1888]))