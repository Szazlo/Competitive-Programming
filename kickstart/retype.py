def retype():
    N, K, S = map(int, input().split())
    return min(K+N, (K-1)+(K-S)+(N+1-S))

for case in range(int(input())):
    print('Case #{}: {}'.format(case+1, retype()))