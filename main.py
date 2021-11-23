import sys
import numpy as np

# calculate topic specific page
M = np.array([[0, 0, 1/3, 0,  0, 0, 0, 0],
              [1, 0,  0, 0.5, 0, 0, 0, 0],
              [0, 1,  0,  0,  0, 0, 0, 0],
              [0, 0, 1/3, 0,  0, 0, 0, 0],
              [0, 0, 1/3, 0,  0, 0, 0, 0],
              [0, 0,  0, 0.5, 0, 0, 0, 1],
              [0, 0,  0,  0,  0, 1, 0, 0],
              [0, 0,  0,  0,  0, 0, 1, 0]
            ])
beta = 0.8
epsilon = 0.01
topic_set = {3, 4}
M = beta * M
teleport_set = (1 - beta) / len(topic_set)
r_old = np.array([0.125 for i in range(8)])
for i in range(8):
    for j in range(8):
        if (i + 1) in topic_set:
          M[i][j] = M[i][j] + teleport_set
        else:
          M[i][j] = M[i][j] + 0

count = 0
while True:
    count = count + 1
    r_new = np.dot(M, r_old)
    file_path = 'README.md'
    sys.stdout = open(file_path, "w")
    print ("\titeration #{0}:".format(count) + "\n")
    print ("\tr_old = " + str(r_old) + "\n")
    print ("\tr_new = " + str(r_new) + "\n")
    print ("\tDifference = " + str(np.abs(np.subtract(r_new, r_old))) + "\n")
    print ("\tTopic Set Power Iteration Converged At: " + str(r_new) + "\n")
    # Have about 33 iterations but converges to 33rd that is stored in the read
    print("\tAlgorithm produced",count, "iterations\n")
    if np.sum(np.abs(r_new - r_old)) < epsilon:
        break
    
    r_old = r_new

    #while()
