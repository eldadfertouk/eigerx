def count_max(num, max_val, count):
    if num == 0:
        print(count)
    elif num == max_val:
        count += 1
        count_max(input(), max_val, count)
    else:
        max_val = max(max_val, num)
        count_max(input(), max_val, count)

count_max(input(), 0, 0)
