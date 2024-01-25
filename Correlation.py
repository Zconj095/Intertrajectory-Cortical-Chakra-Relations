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
# Adjust this to align with your intended logic
hydrogen = weights_1_transposed / weights_2
helium = weights_1_transposed / weights_2  # Same as hydrogen; adjust as per your logic

# Create a DataFrame from the ratios
ratios = pd.DataFrame({
    'hydrogen': hydrogen.flatten(),  # Flatten to convert 2D arrays to 1D
    'helium': helium.flatten()       # Flatten to convert 2D arrays to 1D
})

# Calculate the correlation
ic = ratios.corr().loc['hydrogen', 'helium']

print("Interconnectedness: %.3f" % ic)