def dg(n):
    return 1 if n == 1 else n * dg(n - 1)

print(dg(7))


# def game_3_7(start, end):
#     res_arr = []
#     while start <= end:
#         if start % 3 == 0 and start % 7 == 0:
#             res_arr.append(start)
#         start += 1
#
#     return {'count': len(res_arr), 'res': sum(res_arr)}

def game_3_7(start, end, count = 0, res = 0):
    if start == end:
        return count, res

    if start % 3 == 0 and start % 7 == 0:
        count += 1
        res += start

    return game_3_7(start + 1, end, count, res)

print(game_3_7(1, 100))

ls1 = [11, 22, 33]
ls2 = [22, 33, 44]
print(list(set(ls1) & set(ls2)))