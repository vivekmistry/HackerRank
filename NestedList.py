if __name__ == '__main__':

    n = int(input())
    nlist = [[input(), float(input())] for _ in range(n)]
    second_lowest = sorted(list(set([marks for name, marks in nlist])))[1]
    print('\n'.join([a for a, b in sorted(nlist) if b == second_lowest]))
