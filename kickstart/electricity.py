# Ben works as an engineer in a city with N electric junctions. These junctions form a network and can be visualised as a connected graph with N vertices and N−1 edges. The city is facing a power outage, due to which none of the junctions are receiving electricity, and Ben is in charge of handling the situation.

# Each junction has a fixed electric capacity. Ai is the electric capacity of the i-th junction. Due to resource constraints, Ben can provide electricity to only one junction, but other junctions can receive electricity depending on their connections and capacities. If the i-th junction receives electricity, then it will also get transmitted to all the junctions directly connected to the i-th junction whose capacity is strictly less than Ai. Transmission stops if no eligible junction is present. Help Ben determine the maximum number of junctions that can receive electricity.

# Input
# The first line of the input gives the number of test cases, T. T test cases follow.
# The first line of each test case contains an integer N which represents the number of junctions in the city.
# The next line contains N integers. The i-th integer is Ai, which is the electric capacity of the i-th junction.
# The next N−1 lines each contain two integers Xi and Yi, meaning that the junctions Xi and Yi are directly connected to each other.

# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of junctions that can receive electricity.

def electric():
    N = int(input())
    junctions = list(map(int, input().split()))
    connections = []
    lenght=0
    for i in range(N-1):
        connections.append(list(map(int, input().split())))




for case in range(int(input())):
    print('Case #{}: {}'.format(case+1, electric()))