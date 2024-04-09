count = int(input())

inpt = input()

textarr = [] 
for i in range(count):
    textarr.append(inpt[i].upper())

counter = dict()
biggest = 0
biggestChar = ""
biggesttwo = 0
biggesttwoChar = ""

for i in range(count):
    if(not textarr[i] in counter):
        counter[textarr[i]] = 0
    counter[textarr[i]] += 1
    if(counter[textarr[i]] > biggest):
        biggest = counter[textarr[i]]
        biggestChar = textarr[i]
    elif (counter[textarr[i]] > biggesttwo):
        biggesttwo = counter[textarr[i]]
        biggesttwoChar = textarr[i]


print(biggestChar+biggesttwoChar)
