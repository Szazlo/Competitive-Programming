def alien_generator():
    G = int(input())
    result, day = 0, 1
    while (1+day)*day//2 <= G:
        if (G-(1+day)*day//2)%day == 0:
            result += 1
        day += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, alien_generator()))