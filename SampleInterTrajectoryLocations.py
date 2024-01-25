import numpy as np
from numpy.random import permutation

# Weights
w1 = np.random.randn(100, 50)
w2 = np.random.randn(50, 25)

# Permute w1 rows 
perm_idx = permutation(np.arange(len(w1)))    
w1 = w1[perm_idx]

# Modulo transforming w2  
w2 = np.mod(w2+5, 10) 

# Divinity transform    
def divinity_transform(arr):
    return np.sqrt(arr) - np.cbrt(arr)

w1_dt = divinity_transform(w1[:, :-1])
w2_dt = divinity_transform(w2[:, 1:])   


# Convert to array
ratios = np.array(ratios)

import numpy as np

# Generate weights 
w1 = np.random.uniform(size=(100, 50)) 
w2 = np.random.uniform(size=(50, 25))

# Twist keys 
np.random.shuffle(w1)
np.random.shuffle(w2)



# Create neural network 
net = MLPRegressor(hidden_layer_sizes=(100,), activation='tanh', alpha=0.1)

# Generate subatomic weights
w1 = np.random.uniform(size=(100, 50)) 
w2 = np.random.uniform(size=(50, 25))
net.coefs_ = [w1, w2]


# Sample inter trajectory locations  
locs = [[0.2, 0.5], [0.7, 0.9]]
inter_locs = []
for loc in locs: 
    inter_pts = np.linspace(loc[0], loc[1], 10)
    inter_locs.append(inter_pts)
inter_locs = np.concatenate(inter_locs)    


import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor

import numpy as np

# Adjusted shapes for compatibility
w1 = np.random.randn(100, 50)
w2 = np.random.randn(50, 50)  # Changed from (50, 25) to (50, 50)

# Existing code for permutation and modulo transformation
perm_idx = np.random.permutation(np.arange(len(w1)))    
w1 = w1[perm_idx]
w2 = np.mod(w2+5, 10) 
import numpy as np

def divinity_transform(arr):
    return np.sqrt(arr) - np.cbrt(arr)

# Generate sample weights
w1 = np.random.uniform(size=(100, 50))
w2 = np.random.uniform(size=(50, 25))

# Apply divinity transform
w1_dt = divinity_transform(w1)
w2_dt = divinity_transform(w2)

# Slice arrays to match shapes before division
w1_dt_sliced = w1_dt[:, :25]  # Slice w1_dt to match the second dimension of w2_dt
w2_dt_sliced = w2_dt         # No slicing needed for w2_dt as its second dimension is already 25


