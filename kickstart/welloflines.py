# There is a deep magical well in a forest that has some lilies on its waters. You have a large empty basket and some coins, and are standing next to the well. You have more coins than there are lilies in the well. The well has taken note of the fact that your basket is empty.


#if you toss 1 coin, you get 1 lily
#if you toss 4 coins at once, the will note the number of lies you have
#if you toss 2 coins at once, the well will toss a many lilies as it last noted.

#you have unlimited coins, and you want all the lilys in the well
#You want to collect all the lilies in the well, and you want to do it with the least coins. What is the minimum number of tosses you need to collect all the lilies?


# For test case #2, first, we toss 5 coins, one at a time, into the well, and the well tosses out 5 lilies, one at a time, into our basket. Next, we toss 4 coins at once into the well, and the well takes note that it has tossed out 5 lilies into our basket so far. Then, we toss 2 coins at once into the well, and the well tosses out 5 lilies (that it took note of) into our basket. Then, we toss another 2 coins at once into the well, and the well tosses out another 5 lilies into our basket. Finally, we toss another 2 coins at once into the well, and the well tosses out the final 5 lilies into our basket. Total coins needed is 15. Getting 20 lilies out of the well is not possible with any lesser number of coins, so 15 is our answer.
def magicwell():
    lilies = int(input())
    coins = lilies
    for i in range(1, lilies + 1):
        if lilies % i == 0:
            if (i+4)+(((lilies-i)/i)*2) < coins:
                coins = (i+4)+(((lilies-i)/i)*2)
    return int(coins)

for case in range(int(input())):
    print('Case #{}: {}'.format(case+1, magicwell()))
