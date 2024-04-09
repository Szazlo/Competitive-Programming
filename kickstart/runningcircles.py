#Example
# In Sample Case #1, the length of the circular track is 5 units. Ada is facing the clockwise direction in the beginning.

# First, Ada runs 8 units in the clockwise direction, touching the starting line in the process, and the number of laps in the machine increases by 1. The machine now reports 1 lap. Ada is now 3 units from the starting line in the clockwise direction.
# Next, she runs runs 4 units in the anticlockwise direction. She touches the starting line, but since she touches it running in the opposite direction to what she was running previously, this does not increase the number of laps in the machine. She is now 1 unit from the starting line in the anticlockwise direction.
# Finally, she runs 5 units in the clockwise direction. This time, again, she touches the starting line, but since she last touched it in the anticlockwise direction, this is not counted by the machine. She does not touch the starting line again and at the end, the machine reports 1 lap.

# Ada wants to focus only on running, so she decides to use a machine to count the number of laps she has run. The machine is placed at the starting line of the circular track and starts the count from 0. Every time Ada arrives at the starting line running in the same direction as the last time she departed from the starting line, the machine increases the number of laps that Ada has run by 1. If she crosses the starting line or changes direction at the starting line, the machine considers the new direction as the direction she last touched the starting line. The machine only remembers the last direction in which Ada touched the starting line. During a lap, Ada can change directions any number of times, but as long as she eventually touches the starting line in the same direction as she last touched it, the count of laps in the machine increases by 1.

# This is the first time Ada has practised running long distances, so she cannot run continuously. She runs some distance, then takes a break to regain her energy. However, when she starts running again after taking a break, she cannot remember which direction she was running in previously. So she picks one of the directions, clockwise or anticlockwise, and starts running from the same position where she stopped.

# Ada begins at the starting line and is initially facing in the direction of her first run. She runs a total of N times, taking breaks in between. Given the information of the distance Di units Ada has run, and the direction Ci she has taken (clockwise or anticlockwise) when she ran the i-th time, for all i from 1,…,N, can you tell the number of laps that would be reported by the machine at the end?
def running():
    #if the direction is the same, then the number of laps increases by 1
    #if the direction is different the starting line is reset
    length, runs = map(int, input().split())
    laps = 0
    d = 0
    for i in range(runs):
        distance, direction = input().split()
        distance = int(distance)
        if direction == 'C':
            d += distance
        else:
            d -= distance
        if d >= length:
            laps += d // length
            d %= length
        elif d < 0:
            laps -= (-d) // length
            d %= length
    return laps
    



for case in range(int(input())):
    print('Case #{}: {}'.format(case+1, running()))