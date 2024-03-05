import numpy as np
import pandas as pd
from gaussianpclearn import gaussian_pc_learn
from comp_pat import comp_pat
from learn_complex_norm import learn_complex_norm
from pattern import get_pattern_matrix
########################################################################
# Created by Olivia Hess
# Last Modified: 3/2/24
# Description: Test file for the Gaussian PC Learn function. 
########################################################################

def create_amat(file_path:str, type) -> np.array:
    return np.loadtxt(file_path, delimiter=',', skiprows=1, dtype=type)

def create_cov(adj:np.array) -> np.array:
    cov = np.cov(adj, rowvar=False, bias=True)
    return cov

def learn(truecg:np.array, cov:float, n:int, p:float) -> dict:
    pc_skel = gaussian_pc_learn(cov, n, p, algMethod="stable")
    pat = learn_complex_norm(pc_skel, cov, n, p)
    # should i use the pattern csv or use this function? 
    retVal = comp_pat(get_pattern_matrix(truecg), pat)
    return retVal

if __name__ == "__main__":
    pLearnedMetrics = pd.DataFrame(columns=['name', 'pval', 'samplesize', 'degree', 'TPR', 'TDR', 'FPR', 'ACC', 'SHD'])
    # learn the pattern
    for i in range(2, 3):
        for j in range(1, 30):
            for p in {.005, .05}:
                for n in {200, 2000}:
                    # read in the adjacency matrix cg_", i,"_50/cg50_", i,"_", j, "_data_", n,".csv
                    truecg = create_amat("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/cg_" + str(i) + "_50/cg50_" + str(i) + "_" + str(j) + ".csv", int)
                    datatruecg = create_amat("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/cg_" + str(i) + "_50/cg50_" + str(i) + "_" + str(j) + "_data_" + str(n) + ".csv", float)
                    # patterntruecg = create_amat("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/cg_" + str(i) + "_50/cg50_" + str(i) + "_" + str(j) + "_pattern.csv")
                    # find covariance of dataset to send into learning function
                    cov = create_cov(datatruecg)
                    # learn the pattern and then compare the pattern, getting the metrics back
                    metrics = learn(truecg, cov, n, p)
                    # declare name of cg
                    name = "cg50_" + str(i) + "_" + str(j)
                    # add metrics to dataframe
                    pLearnedMetrics.loc[len(pLearnedMetrics)] = {'name' : name, 'pval' : p, 'samplesize' : n, 'degree' : i, 'TPR' : metrics['tpr'], 'TDR' : metrics['tdr'], 'FPR' : metrics['fpr'], 'ACC' : metrics['acc'], 'SHD' : metrics['shd']}

    pLearnedMetrics.to_csv("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/Metrics/python_pc_original_learned_metrics.csv", index=False)

