import numpy as np

# Define cortical map  
map_size = (100,100)
cortex = np.zeros(map_size)

# Define sectors
sectors = {
   "V1": (slice(0,30), slice(0,30)),
   "V2": (slice(30,60), slice(0,30)), 
   "V3": (slice(60,80), slice(0,30)),
   "M1": (slice(0,40), slice(30,70)),
   "PFC": (slice(60,100), slice(30,100)),
}

# Location feedback  
feedback_locs = [
   (20,10), # V1
   (45,15), # V2 
   (75,25)  # V3
]

# Calculate sector ranges 
sector_ranges = {}
for name, sector in sectors.items():
    locs_in_sector = [loc for loc in feedback_locs if loc[0] >= sector[0].start  
                      and loc[0] < sector[0].stop and loc[1] >= sector[1].start
                      and loc[1] < sector[1].stop]
    
    if locs_in_sector:
        x_range = [min(x for x,_ in locs_in_sector),  
                   max(x for x,_ in locs_in_sector)] 
        y_range = [min(y for _,y in locs_in_sector),
                   max(y for _,y in locs_in_sector)]
        sector_ranges[name] = x_range, y_range
        
print(sector_ranges)
# {'V1': ([20, 20], [10, 10]), 'V2': ([45, 45], [15, 15])}

import numpy as np
# Cortical sectors 
sectors = {
   "V1": (slice(0,30), slice(0,30)),
   "V2": (slice(30,60), slice(0,30)),
   "M1": (slice(0,40), slice(30,70)), 
   "PFC": (slice(60,100), slice(30,100))
}

# Input data
inputs = [
   (10, 12), # V1
   (40, 25), # M1
   (55, 60)  # PFC
]

# Map inputs to sectors
mapped_inputs = {}
for loc in inputs:
    for name, sector in sectors.items():
        if loc[0] >= sector[0].start and loc[0] < sector[0].stop and loc[1] >= sector[1].start and loc[1] < sector[1].stop:
            mapped_inputs[name] = loc


# Example output 
# The economic outlook is promising