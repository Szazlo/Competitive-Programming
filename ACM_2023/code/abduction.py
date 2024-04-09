N = int(input())
K = int(input())

segments = []
for i in range (N):
    segments.append(int(input()))

shots = 0
for i in range(N):
    targetingIndex = i
    while segments[targetingIndex] > 0:
        shots += 1
        for i in range(K):
            segments[targetingIndex+i] -= 1

print(shots)
