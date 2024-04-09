def smaller_strings():
    N, K = map(int, input().split())
    S = input().strip()

    result = 0
    for i in range((len(S)+1)//2):
        result = (result*K+(ord(S[i])-97))%(10**9+7)
    for i in range((len(S)+1)//2, len(S)):
        if S[-1-i] != S[i]:
            result = (result+int(S[-1-i] < S[i]))%(10**9+7)
            break
    return result

for case in range(int(input())):
    print('Case #{}: {}'.format(case+1, smaller_strings()))