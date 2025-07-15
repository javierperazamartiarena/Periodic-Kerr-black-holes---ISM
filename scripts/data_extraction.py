import numpy as np
import os

"""
This script loads and displays the contents of a .npz data file used in the paper.

To use:
- Replace the filename below with one of the following:
    - Run_final_geom_param_area_fixed_v2.npz
    - Run_final_geom_param_area_fixed.npz
    - Run_final_geom_param_new_computation.npz
    - Run_final_geom_param.npz
    - kasner_exp.npz
"""

# Load data
# Replace filename in here: #
filename = 'Run_final_geom_param_area_fixed_v2.npz' 
#############################
data_dir = 'data/'
filepath = os.path.join(data_dir, filename)
data = np.load(filepath)

# List all array names contained in the file
print("Available keys:", data.files)

# Loop through the arrays and print their contents
for key in data.files:
    array = data[key]
    print(f"\033[1mKey:\033[0m {key}")  
    print(f"\033[1mValue:\033[0m", array)
