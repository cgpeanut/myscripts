from keras.models import Sequential
from keras.layers import Dense

# Create a sequential model
model = Sequential()

# Add an input layer with 784 neurons
model.add(Dense(64, activation='relu', input_shape=(784,)))

# Add a hidden layer with 32 neurons
model.add(Dense(32, activation='relu'))

# Add an output layer with 10 neurons
model.add(Dense(10, activation='softmax'))
