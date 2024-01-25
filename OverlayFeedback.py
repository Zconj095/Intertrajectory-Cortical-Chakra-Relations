import numpy as np
# Generate test data
ratios = np.random.uniform(size=100) 

# Overlay feedback 
def overlay_feedback(x):
    return x + 0.1*np.sin(5*x)

ratios_of = overlay_feedback(ratios)

# Interlay measurements
def interlay(x):
    freq = np.arange(len(x))
    return x + 0.5*np.sin(freq)

ratios_il = interlay(ratios_of)

# Feed ratios through functions
for _ in range(10):
    ratios_of = overlay_feedback(ratios_il) 
    ratios_il = interlay(ratios_of)
    
final_ratios = ratios_il


