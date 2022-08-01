# def solution(id_list, report, k):
#     answer = []
#
#     romove_duplication = []
#     for check_duple in report:
#         if check_duple not in romove_duplication:
#             romove_duplication.append(check_duple)
#
#     print(romove_duplication)
#
#     check_count = []
#     for checkCount in romove_duplication:
#         check_count.append(checkCount.split()[1])
#
#     print(check_count)
#
#     block = []
#     for i in id_list:
#         if check_count.count(i) >= k:
#             block.append(i)
#
#     for b in block:
#         for check in romove_duplication:
#             if b == check.split()[1]:
#
#
#
#
#
#     return answer
#
#
# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
