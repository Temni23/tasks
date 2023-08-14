def flower_field(n, list_for_work):
    list_for_work.sort()
    result = []
    i = 0
    start, end = list_for_work[i]
    while i < n:
        if start <= list_for_work[i][0] <= end:
            curr_end = list_for_work[i][1]
            i += 1
            if curr_end > end:
                end = curr_end
        else:
            result.append([start, end])
            start, end = list_for_work[i]
            i += 1
    result.append([start, end])

    return result


if __name__ == '__main__':
    num = int(input())
    example = [list(map(int, input().split())) for _ in range(num)]
    total = flower_field(num, example)
    for _, __ in total:
        print(_, __)
