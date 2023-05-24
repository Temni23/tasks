def fibo(fibo_list, num):
    element = fibo_list[-2] + fibo_list[-1]
    fibo_list.append(element)
    if len(fibo_list) == num:
        return fibo_list
    else:
        return fibo(fibo_list, num)



if __name__ == '__main__':
    fibo_list = [0, 1]
    print(fibo(fibo_list, 50))
