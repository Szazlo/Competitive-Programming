def boring():
    N, K = map(int, input().split())
    return((sum([1 for i in range(K+1) if i % 2 != 0]))-(sum([1 for i in range(N) if i % 2 == 0])))
for case in range(int(input())):
    print('Case #{}: {}'.format(case+1, boring()))