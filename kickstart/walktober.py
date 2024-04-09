T = int(input())
for i in range(T):
    M, N, P = map(int, input().split()) # M participants, N days, P is John's ID
    scoreboard = [] 
    for j in range(M):  #participants
        scoreboard.append(list(map(int, input().split())))  # add their daily steps to scoreboard
    max_score = 0   # max score for each day
    for j in range(N):  # days
        max_score += max(scoreboard[k][j] for k in range(M))    # add max score for each day
    print('Case #{}: {}'.format(i+1, max_score - sum(scoreboard[P-1])))   # print John's score