import numpy as np
from graph import Graph
import igraph
import random
import pandas

########################################################################
# Created by Olivia Hess
# Last Modified: 9/23/23
# Description: Generates 1 random chain graph and saves them as csv files 
# in the current working directory. 
########################################################################

def get_interval(number:int, interval_sequence:list) -> int: 
    for i in range(len(interval_sequence) - 1):
        if number > interval_sequence[i] and number <= interval_sequence[i + 1]:
            return i
    return -1

def create_symetric_mat (p:int, n:int) -> np.array:
    # TODO: this line is generating too many 0's, need to fix that. No undirected edges are occuring.
    raw_mat = np.random.choice([0, 1], size=(p, p), p=[1 - n / (p - 1), n / (p - 1)])
    raw_mat[np.triu_indices(p)] = 0
    raw_mat = np.maximum(raw_mat, raw_mat.T)
    return raw_mat

def create_random_chordless_mat (p:int, n:int) -> np.array:
    # TODO: or it is this generating too many 0's, need to fix that. No undirected edges are occuring.
    ch_l_matrix = create_symetric_mat(p, n)
    k = random.randint(2, p)
    I = [0.999999] + [i * (p / k) for i in range(1, k + 1)]
    for i in range(p):
        for j in range(p):
            if get_interval(i, I) > get_interval(j, I):
                ch_l_matrix[i][j] = 0
    return ch_l_matrix

def create_matrix(n:int ,p:int)-> np.array:
    n_values = [n]
    p_values = [p]
    for n in n_values:
        for p in p_values:
            cg = create_random_chordless_mat(p,n)
    return cg

def write_results(n:int,p:int) -> None:
    file_path = "cg" + str(p) + "_" + str(n) + ".csv"
    data = create_matrix(n,p)
    np.savetxt(file_path, data, delimiter=',', fmt='%d')

if __name__ == "__main__":
    write_results(2,30)
    