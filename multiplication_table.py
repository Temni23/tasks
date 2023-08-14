n, m = int(input()), int(input())
res = [[str(i * j).ljust(3) for i in range(m)] for j in range(n)]
for list_ in res:
    print(*list_)
