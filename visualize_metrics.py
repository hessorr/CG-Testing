import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file_path:str) -> pd.DataFrame:
    '''
    Reads in a csv file and returns a pandas dataframe.
    param file_path: the path to the csv file
    '''   
    colNames = ['name', 'pval', 'samplesize', 'degree', 'TPR', 'TDR', 'FPR', 'ACC', 'SHD']
    return pd.read_csv(file_path, header=0, names=colNames)

if __name__ == '__main__':
    lcd_metrics = read_csv("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/Metrics/r_lcd_learned_cg_metrics.csv")
    cglearn_stable_metrics = read_csv("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/Metrics/r_pc_learned_stable_cg_metrics.csv")
    cglearn_original_metrics = read_csv("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/Metrics/r_pc_learned_stable_cg_metrics.csv")
    
    # need to filter by pval, sample size, and degree (get n = 2 first)
    pval05lcd = lcd_metrics[(lcd_metrics['pval'] == 0.05) & (lcd_metrics['degree'] == 2)]
    pval005lcd = lcd_metrics[(lcd_metrics['pval'] == 0.005) & (lcd_metrics['degree'] == 2)]
    pval05stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.05) & (cglearn_stable_metrics['degree'] == 2)]
    pval005stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.005) & (cglearn_stable_metrics['degree'] == 2)]
    pval05original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.05) & (cglearn_original_metrics['degree'] == 2)]
    pval005original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.005) & (cglearn_original_metrics['degree'] == 2)]
    ss200lcd = lcd_metrics[(lcd_metrics['samplesize'] == 200) & (lcd_metrics['degree'] == 2)]
    ss2000lcd = lcd_metrics[(lcd_metrics['samplesize'] == 2000) & (lcd_metrics['degree'] == 2)]
    ss200stable = cglearn_stable_metrics[(cglearn_stable_metrics['samplesize'] == 200) & (cglearn_stable_metrics['degree'] == 2)]
    ss2000stable = cglearn_stable_metrics[(cglearn_stable_metrics['samplesize'] == 2000) & (cglearn_stable_metrics['degree'] == 2)]
    ss200original = cglearn_original_metrics[(cglearn_original_metrics['samplesize'] == 200) & (cglearn_original_metrics['degree'] == 2)]
    ss2000original = cglearn_original_metrics[(cglearn_original_metrics['samplesize'] == 2000) & (cglearn_original_metrics['degree'] == 2)]
