import numpy as np 
import pandas as pd
from sklearn.neural_network import MLPRegressor

# Create sample neural network
net = MLPRegressor(hidden_layer_sizes=(300, 100), activation='relu', solver='adam', alpha=0.0001)

# Generate random weights 
weights_1 = np.random.uniform(0.01, 1, size=(100, 300)) 
weights_2 = np.random.uniform(0.1, 5, size=(1, 100))
net.coefs_ = [weights_1, weights_2]

# Transpose weights_1 to align dimensions for division
weights_1_transposed = weights_1.T  # Transpose to shape (300, 100)

# Calculate subatomic weight ratios
# Now, weights_1_transposed and weights_2 are both shaped (100, 300), allowing for element-wise division
hydrogen = weights_1_transposed / weights_2
helium = weights_1_transposed / weights_2  # Adjust this line as per your logic

# Interconnectedness between ratios
ratios = pd.DataFrame({'hydrogen': hydrogen.flatten(), 'helium': helium.flatten()})
ic = ratios.corr().loc['hydrogen', 'helium']

print("Interconnectedness: %.3f" % ic)