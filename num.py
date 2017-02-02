
num = int(raw_input('what is your number? '))


def sum_num():
    sum_nums = 0
    while sum_nums < num:
        total = sum_nums + 1
        print total
    return total

print sum_num()
