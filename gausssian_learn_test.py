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
    # should i use the pattern csv or use this function? 
    retVal = comp_pat(get_pattern_matrix(cg), pat)
    return retVal

def add_metrics_to_adj(metrics:dict, adj:np.array) -> np.array:
    # add metrics to the adjacency matrix
    # need to set up columns for the metrics
    # extract the metrics from the dictionary
    # create new row
    # then add the new row to the matrix
    pass

if __name__ == "__main__":
    
    # learn the pattern
    for i in range(2, 3):
        for j in range(1, 30):
            for p in {.05, .005}:
                for n in {200, 2000}:
                    # read in the adjacency matrix
                    truecg = create_amat("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing")
                    datatruecg = create_amat("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing")
                    patterntruecg = create_amat("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing")
                    # find covariance of dataset
                    cov = create_cov(datatruecg)
                    metrics = learn(truecg, cov, n, p)
                    # add metrics to the adjacency matrix
                    amat = add_metrics_to_adj(metrics, amat)
                    # write the new adjacency matrix to a csv

    np.savetxt("python_learned_metrics.csv", amat, delimiter=",")

