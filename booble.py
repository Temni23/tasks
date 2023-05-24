def bubble(list_for_sort):
    count = 0
    cikle = 0
    while True:
        for i in range(len(list_for_sort)-1):
            a = list_for_sort[i]
            b = list_for_sort[i+1]
            if a > b:
                list_for_sort[i], list_for_sort[i + 1] = b, a
                count +=1
        if count == 0 and cikle == 0:
            print(*list_for_sort)
            break
        if count == 0:
            break
        print(*list_for_sort)
        count = 0
        cikle += 1




if __name__ == '__main__':
    n = input()
    fibo_list = [int(i) for i in input().split()]
    bubble(fibo_list)
