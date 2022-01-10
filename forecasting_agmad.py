import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N = int(input("\nEnter the number of days: "))

#array of states probability values and current state as a vector
transMatrix = np.array([[0.5, 0.4, 0.1], [0.3, 0.4, 0.3], [0.2, 0.3, 0.5]])
currentState = np.array([[1.0, 0.0, 0.0]])

#This part calculates steady state values and plots them
stateHistogram = currentState
stateHistDataframe = pd.DataFrame(currentState)

for x in range(15):
    currentState = np.dot(currentState, transMatrix)
    stateHistogram = np.append(stateHistogram, currentState, axis=0)
    #Construct a dataframe from the values to show it using matplotlib
    stateHistDataframe = pd.DataFrame(stateHistogram, columns = ["Sunny", "Rainy", "Cloudy"])

print("\nsteady state values: (𝜋_0, 𝜋_1, 𝜋_2) = " + str(currentState))
stateHistDataframe.plot()

#This part calculates transition matrix after N days
currentState = transMatrix
stateHistogram = currentState

for x in range(N-1):
    currentState = np.dot(currentState, transMatrix)

print("\nMatrix after N days:\n" + str(currentState))

#Plot the values
plt.show()

