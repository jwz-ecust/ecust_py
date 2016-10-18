def next_bigger(n):
    to_list = list(int(i) for i in str(n))
    length = len(to_list)
    if length == 1:
        return -1
    i = -1
    while to_list[i] <= to_list[i - 1]:
        i -= 1
        if i + length == 0:
            return -1
    process_list = to_list[i - 1:]
    replace = 0
    for num in sorted(process_list):
        if num > process_list[0]:
            replace = num
            break
    process_list.remove(replace)
    result = to_list[:i - 1] + [replace] + sorted(process_list)
    return int("".join(str(i) for i in result))


print next_bigger(1123344)
