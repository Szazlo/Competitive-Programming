count = int(input())
budget = int(input())
pubs = []
for i in range(count):
    pubs.append(int(input()))

pubs.sort(reverse=True)


bars = 0
while len(pubs)>0 and budget >= pubs[len(pubs)-1]:
    bars +=1
    budget -= pubs[len(pubs)-1]
    pubs.pop()
print(bars)

