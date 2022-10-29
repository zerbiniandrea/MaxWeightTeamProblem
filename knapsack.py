"""
    0-1 Knapsack
    Dynamic Programming
    https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem

    This solution will therefore run in O (nW) time and O(nW) space. 
    n = number of players
    W = maximum weight capacity
"""

# useful in testing
"""
save to excel file to easily view the solution
need to import pandas

# import pandas as pd

# df = pd.DataFrame(K)
# df.to_excel(excel_writer = "C:/Users/zerbi/Desktop/test.xlsx")
"""

import random

# the input file with player's data
input_file = "C:/Users/zerbi/Desktop/giocatori.txt"

# main algorithm
def knapSack(capacity, weights, n):
    # initialize matrix of size capacity+1 and n+1
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # for every element (player)
    for i in range(n + 1):
        for j in range(capacity + 1):
            # first row or column
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weights[i-1] <= j:
                # the "object" is taken
                K[i][j] = max(weights[i-1] + K[i-1][j-weights[i-1]],  K[i-1][j])
            else:
                # the "object" is not taken
                K[i][j] = K[i-1][j]

    # the max value obtained will always be in the
    # last cell of the matrix
    # return K[n][capacity]
    return K

"""
Function that, given a matrix K containing the solution,
returns the list of the players that are part of the solution.

To get it, compare the current value (starting from the one in the bottom right corner of the matrix)
with the one in the previous row. If the value is different, it means that the N-th player was chosen.
If that's the case, add it to the list of included players and decrease the column index by the value of the 
N-th player's weight.
Otherwise, the player was not taken.
"""
def knapSack_sol(K, capacity, weights, n):
    # the max value obtained will always be in the
    # last cell of the matrix
    print("The maximum weight is:", K[n][capacity])

    included_players_ids = []

    while n > 0 and capacity > 0:
        if K[n-1][capacity] != K[n][capacity]:
            included_players_ids.append(n-1)
            capacity = capacity - weights[n-1]
        
        n=n-1

    # check the input file for the ids
    print("The solution includes the players having ids: ",included_players_ids)

"""
Create a file with n rows where each row contains (each value separated by a space):
    # id
    # weight(random between min and max)
    # role (random between roles)

Change the file's location in the global variable input_file
"""
def create_input_file(n):
    roles = ["interno", "centrale", "esterno"]

    f = open(input_file,"w")

    min_weight = 40
    max_weight=80

    for i in range(0,n):
        f.write(" ".join([str(i),str(random.randrange(min_weight,max_weight,1)),random.choice(roles),"\n"]))
    
    f.close()

if __name__ == "__main__":
    # number of players to be generated
    # in the input file
    n_players = 4

    # maximum weight capacity of a team
    max_weight = 150

    create_input_file(n_players)

    # read the input
    f = open(input_file,"r")
    players_weights = []
    lines = f.readlines()
    f.close() 
    for line in lines:
            line = line.split(" ")
            players_weights.append(int(line[1]))

    n = len(players_weights)

    K = knapSack(max_weight, players_weights, n)

    knapSack_sol(K, max_weight, players_weights, n)
