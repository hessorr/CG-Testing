import numpy as np
########################################################################
# Created by Olivia Hess
# Last Modified: 9/26/23
# Description: Used to read in csv of a generated adjacency matrix. 
#   **Putting this here so I can use it in multple files while I test.**
########################################################################

def create_amat(file_path:str) -> np.array:
    return np.genfromtxt(file_path, delimiter=',', skip_header=0, dtype=int)
