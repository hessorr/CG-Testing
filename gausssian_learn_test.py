import numpy as np
import pandas as pd
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

if __name__ == "__main__":
    pLearnedMetrics = pd.DataFrame(columns=['name', 'pval', 'samplesize', 'degree', 'TPR', 'TDR', 'FPR', 'ACC', 'SHD'])
    # learn the pattern
    for i in range(2, 3):
        for j in range(1, 30):
            for p in {.05, .005}:
                for n in {200, 2000}:
                    # read in the adjacency matrix cg_", i,"_50/cg50_", i,"_", j, "_data_", n,".csv
                    truecg = create_amat("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/cg_" + str(i) + "_50/cg50_" + str(i) + "_" + str(j) + ".csv")
                    datatruecg = create_amat("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/cg_" + str(i) + "_50/cg50_" + str(i) + "_" + str(j) + "_data_" + str(n) + ".csv")
                    patterntruecg = create_amat("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/cg_" + str(i) + "_50/cg50_" + str(i) + "_" + str(j) + ".csv")
                    # find covariance of dataset to send into learning function
                    cov = create_cov(datatruecg)
                    # learn the pattern and then compare the pattern, getting the metrics back
                    metrics = learn(truecg, cov, n, p)
                    # declare name of cg
                    name = ''
                    # add metrics to dataframe
                    pLearnedMetrics.loc[len(pLearnedMetrics)] = {'name' : name, 'pval' : p, 'samplesize' : n, 'degree' : i, 'TPR' : metrics['tpr'], 'TDR' : metrics['tdr'], 'FPR' : metrics['fpr'], 'ACC' : metrics['acc'], 'SHD' : metrics['shd']}

    pLearnedMetrics.to_csv("python_pc_original_learned_metrics.csv", index=False)

