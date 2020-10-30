""" Leetcode 134: There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1   """

'''Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.'''

# Approach 1: Brute Force. For each station check if we can take a circular route to that station
# Time Complexity : O(n^2) Space Complexity - O(1)


def circular_route_all(gas, cost):
    # For each gas station
    for s in range(len(gas)):
        tank = 0
        possible = True

        # Check if we hae sufficient gas in the tank to complete the circular route
        for i in range(s, len(gas) + s):
            station = i % len(gas)
            tank = tank + gas[station] - cost[station]
           # If there is no sufficient gas in the tank, we cannot start from that station
            if tank < 0:
                possible = False
                break
        # If the circular route is possible from the station, we get our answer
        if possible:
                return s
        # If there is no such possible route
    return -1

# Approach 2: Optimized solution Time complexity - O(n) and Space Complexity - O(1)


def circular_route(gas, cost):
    # Check if there is any circular route possible
    diff_total = 0
    for i in range(len(gas)):
        diff_total += gas[i] - cost[i]

    if diff_total < 0:
        return -1
    else:
        starting, tank = 0, 0
        for s in range(len(gas)):
            tank += gas[s] - cost[s]

            if tank < 0:
                starting = s + 1
                tank = 0
        return starting


# Driver code to test the code
if __name__ == '__main__':
     gas = [2, 3, 4]
     cost = [3, 4, 3]
     print(circular_route(gas,cost))
