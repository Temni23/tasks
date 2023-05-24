def is_correct(s):
    for _ in range(len(s) // 2):
        s = s.replace('()', '')
    return len(s) == 0


def gen_binary(n, f=''):
    if n == 0 and is_correct(f):
        print(f)
    elif n == 0:
        pass
    else:
        gen_binary(n - 1, f + '(')
        gen_binary(n - 1, f + ')')


if __name__ == '__main__':
    n = int(input()) * 2
    gen_binary(n)
