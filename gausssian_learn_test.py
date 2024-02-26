import numpy as np
########################################################################
# Created by Olivia Hess
# Last Modified: 2/26/24
# Description: Test file for the Gaussian PC Learn function. 
########################################################################

def create_amat(file_path:str) -> np.array:
    return np.genfromtxt(file_path, delimiter=',', skip_header=0, dtype=int)

def create_cov(adj:np.array) -> np.array:
    cov = np.cov(adj, rowvar=False, bias=True)
    return cov

def learn(cg:np.array, cov:float, n:int, p:float) -> dict:
    pc_skel = gaussian_pc_learn(cov, n, p, algMethod="stable")
    pat = learn_complex_norm(pc_skel, cov, n, p)
    retVal = comp_pat(get_pattern_matrix(cg), pat)
    return retVal