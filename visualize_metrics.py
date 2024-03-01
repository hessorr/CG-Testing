import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file_path:str) -> pd.DataFrame:
    '''
    Reads in a csv file and returns a pandas dataframe.
    param file_path: the path to the csv file
    '''   
    colNames = ['name', 'pval', 'samplesize', 'degree', 'TPR', 'TDR', 'FPR', 'ACC', 'SHD']
    return pd.read_csv(file_path, header=0, names=colNames)

def ten_plots(lcd_metrics, cglearn_stable_metrics, cglearn_original_metrics):
    # need to filter by pval, sample size, and degree (get n = 2 first)
    #### pval == 0.05
    pval05200lcd = lcd_metrics[(lcd_metrics['pval'] == 0.05) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 200)]
    pval052000lcd = lcd_metrics[(lcd_metrics['pval'] == 0.05) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 2000)]
    pval05200stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.05) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 200)]
    pval052000stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.05) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 2000)]
    pval05200original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.05) & (cglearn_original_metrics['degree'] == 2) & (cglearn_original_metrics['samplesize'] == 200)]
    pval052000original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.05) & (cglearn_original_metrics['degree'] == 2) &  (cglearn_original_metrics['samplesize'] == 2000)]
    #### pval == 0.005
    pval005200lcd = lcd_metrics[(lcd_metrics['pval'] == 0.005) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 200)]
    pval0052000lcd = lcd_metrics[(lcd_metrics['pval'] == 0.005) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 2000)]
    pval005200stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.005) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 200)]
    pval0052000stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.005) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 2000)]
    pval005200original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.005) & (cglearn_original_metrics['degree'] == 2) & (cglearn_original_metrics['samplesize'] == 200)]
    pval0052000original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.005) & (cglearn_original_metrics['degree'] == 2) & (cglearn_original_metrics['samplesize'] == 2000)]


    # plot the TPR, TDR, FPR, ACC, and SHD for each pval and sample size
    #### Initialize the plots
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8), (ax9, ax10)) = plt.subplots(nrows=5, ncols=2, figsize=(20, 8))

    #### Create the boxplots
        # precision
    positions = [1, 1.4, 3, 3.4, 4, 4.4]
    bplot1 = ax1.boxplot([pval05200lcd['TPR'], pval052000lcd['TPR'], pval05200stable['TPR'], pval052000stable['TPR'],  pval05200original['TPR'],pval052000original['TPR']], vert = True, positions=positions, patch_artist=True, labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax1.set_title('alpha = 0.05')
    bplot2 = ax2.boxplot([pval005200lcd['TPR'], pval0052000lcd['TPR'], pval005200stable['TPR'], pval0052000stable['TPR'],  pval005200original['TPR'],pval0052000original['TPR']], vert = True, patch_artist=True, labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax1.set_title('alpha = 0.005')
    ax1.set_ylabel('TPR')
        # recall
    bplot3 = ax3.boxplot([pval05200lcd['TDR'], pval052000lcd['TDR'], pval05200stable['TDR'], pval052000stable['TDR'],  pval05200original['TDR'],pval052000original['TDR']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax3.set_title('alpha = 0.05')
    bplot4 = ax4.boxplot([pval005200lcd['TDR'], pval0052000lcd['TDR'], pval005200stable['TDR'], pval0052000stable['TDR'],  pval005200original['TDR'],pval0052000original['TDR']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax4.set_title('alpha = 0.005')
    ax3.set_ylabel('TDR')
        # FPR
    bplot5 = ax5.boxplot([pval05200lcd['FPR'], pval052000lcd['FPR'], pval05200stable['FPR'], pval052000stable['FPR'],  pval05200original['FPR'],pval052000original['FPR']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax5.set_title('alpha = 0.05')
    bplot6 = ax6.boxplot([pval005200lcd['FPR'], pval0052000lcd['FPR'], pval005200stable['FPR'], pval0052000stable['FPR'],  pval005200original['FPR'],pval0052000original['FPR']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax6.set_title('alpha = 0.005')
    ax5.set_ylabel('FPR')
        # ACC
    bplot7 = ax7.boxplot([pval05200lcd['ACC'], pval052000lcd['ACC'], pval05200stable['ACC'], pval052000stable['ACC'],  pval05200original['ACC'],pval052000original['ACC']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax7.set_title('alpha = 0.05')
    bplot8 = ax8.boxplot([pval005200lcd['ACC'], pval0052000lcd['ACC'], pval005200stable['ACC'], pval0052000stable['ACC'],  pval005200original['ACC'],pval0052000original['ACC']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax8.set_title('alpha = 0.005')
    ax7.set_ylabel('ACC')
        # SHD
    bplot9 = ax9.boxplot([pval05200lcd['SHD'], pval052000lcd['SHD'], pval05200stable['SHD'], pval052000stable['SHD'],  pval05200original['SHD'],pval052000original['SHD']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax9.set_title('alpha = 0.05')
    bplot10 = ax10.boxplot([pval005200lcd['SHD'], pval0052000lcd['SHD'], pval005200stable['SHD'], pval0052000stable['SHD'],  pval005200original['SHD'],pval0052000original['SHD']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax10.set_title('alpha = 0.05')
    ax9.set_ylabel('SHD')

    # fill with colors
    colors = ['pink', 'lightblue','pink', 'lightblue','pink', 'lightblue']
    for bplot in (bplot1, bplot2, bplot3, bplot4, bplot5, bplot6, bplot7, bplot8, bplot9, bplot10):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
    # ax1.legend([bplot1["boxes"][0], bplot1["boxes"][1]], ["200 Samples", "2000 Samples"], loc='lower right')
    plt.subplots_adjust(hspace=0.7)
    plt.show()

def six_plots(lcd_metrics, cglearn_stable_metrics, cglearn_original_metrics):
    # need to filter by pval, sample size, and degree (get n = 2 first)
    #### pval == 0.05
    pval05200lcd = lcd_metrics[(lcd_metrics['pval'] == 0.05) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 200)]
    pval052000lcd = lcd_metrics[(lcd_metrics['pval'] == 0.05) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 2000)]
    pval05200stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.05) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 200)]
    pval052000stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.05) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 2000)]
    pval05200original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.05) & (cglearn_original_metrics['degree'] == 2) & (cglearn_original_metrics['samplesize'] == 200)]
    pval052000original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.05) & (cglearn_original_metrics['degree'] == 2) &  (cglearn_original_metrics['samplesize'] == 2000)]
    #### pval == 0.005
    pval005200lcd = lcd_metrics[(lcd_metrics['pval'] == 0.005) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 200)]
    pval0052000lcd = lcd_metrics[(lcd_metrics['pval'] == 0.005) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 2000)]
    pval005200stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.005) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 200)]
    pval0052000stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.005) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 2000)]
    pval005200original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.005) & (cglearn_original_metrics['degree'] == 2) & (cglearn_original_metrics['samplesize'] == 200)]
    pval0052000original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.005) & (cglearn_original_metrics['degree'] == 2) & (cglearn_original_metrics['samplesize'] == 2000)]


    # plot the TPR, TDR, FPR, ACC, and SHD for each pval and sample size
    #### Initialize the plots
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2, figsize=(20, 8))

    #### Create the boxplots
        # precision
    bplot1 = ax1.boxplot([pval05200lcd['TPR'], pval052000lcd['TPR'], pval05200stable['TPR'], pval052000stable['TPR'],  pval05200original['TPR'],pval052000original['TPR']], vert = True, patch_artist=True, labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax1.set_title('alpha = 0.05')
    bplot2 = ax2.boxplot([pval005200lcd['TPR'], pval0052000lcd['TPR'], pval005200stable['TPR'], pval0052000stable['TPR'],  pval005200original['TPR'],pval0052000original['TPR']], vert = True, patch_artist=True, labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax1.set_title('alpha = 0.005')
    ax1.set_ylabel('TPR')
        # recall
    bplot3 = ax3.boxplot([pval05200lcd['TDR'], pval052000lcd['TDR'], pval05200stable['TDR'], pval052000stable['TDR'],  pval05200original['TDR'],pval052000original['TDR']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax3.set_title('alpha = 0.05')
    bplot4 = ax4.boxplot([pval005200lcd['TDR'], pval0052000lcd['TDR'], pval005200stable['TDR'], pval0052000stable['TDR'],  pval005200original['TDR'],pval0052000original['TDR']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax4.set_title('alpha = 0.005')
    ax3.set_ylabel('TDR')
        # FPR
    bplot5 = ax5.boxplot([pval05200lcd['FPR'], pval052000lcd['FPR'], pval05200stable['FPR'], pval052000stable['FPR'],  pval05200original['FPR'],pval052000original['FPR']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax5.set_title('alpha = 0.05')
    bplot6 = ax6.boxplot([pval005200lcd['FPR'], pval0052000lcd['FPR'], pval005200stable['FPR'], pval0052000stable['FPR'],  pval005200original['FPR'],pval0052000original['FPR']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax6.set_title('alpha = 0.005')
    ax5.set_ylabel('FPR')

    # fill with colors
    colors = ['pink', 'lightblue','pink', 'lightblue','pink', 'lightblue']
    for bplot in (bplot1, bplot2, bplot3, bplot4, bplot5, bplot6):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
    # ax1.legend([bplot1["boxes"][0], bplot1["boxes"][1]], ["200 Samples", "2000 Samples"], loc='lower right')
    plt.subplots_adjust(hspace=0.7)
    plt.show()

def four_plots(lcd_metrics, cglearn_stable_metrics, cglearn_original_metrics):
    # need to filter by pval, sample size, and degree (get n = 2 first)
    #### pval == 0.05
    pval05200lcd = lcd_metrics[(lcd_metrics['pval'] == 0.05) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 200)]
    pval052000lcd = lcd_metrics[(lcd_metrics['pval'] == 0.05) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 2000)]
    pval05200stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.05) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 200)]
    pval052000stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.05) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 2000)]
    pval05200original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.05) & (cglearn_original_metrics['degree'] == 2) & (cglearn_original_metrics['samplesize'] == 200)]
    pval052000original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.05) & (cglearn_original_metrics['degree'] == 2) &  (cglearn_original_metrics['samplesize'] == 2000)]
    #### pval == 0.005
    pval005200lcd = lcd_metrics[(lcd_metrics['pval'] == 0.005) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 200)]
    pval0052000lcd = lcd_metrics[(lcd_metrics['pval'] == 0.005) & (lcd_metrics['degree'] == 2) & (lcd_metrics['samplesize'] == 2000)]
    pval005200stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.005) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 200)]
    pval0052000stable = cglearn_stable_metrics[(cglearn_stable_metrics['pval'] == 0.005) & (cglearn_stable_metrics['degree'] == 2) & (cglearn_stable_metrics['samplesize'] == 2000)]
    pval005200original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.005) & (cglearn_original_metrics['degree'] == 2) & (cglearn_original_metrics['samplesize'] == 200)]
    pval0052000original = cglearn_original_metrics[(cglearn_original_metrics['pval'] == 0.005) & (cglearn_original_metrics['degree'] == 2) & (cglearn_original_metrics['samplesize'] == 2000)]


    # plot the TPR, TDR, FPR, ACC, and SHD for each pval and sample size
    #### Initialize the plots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(20, 8))
        # ACC
    bplot1 = ax1.boxplot([pval05200lcd['ACC'], pval052000lcd['ACC'], pval05200stable['ACC'], pval052000stable['ACC'],  pval05200original['ACC'],pval052000original['ACC']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax1.set_title('alpha = 0.05')
    bplot2 = ax2.boxplot([pval005200lcd['ACC'], pval0052000lcd['ACC'], pval005200stable['ACC'], pval0052000stable['ACC'],  pval005200original['ACC'],pval0052000original['ACC']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax2.set_title('alpha = 0.005')
    ax1.set_ylabel('ACC')
        # SHD
    bplot3 = ax3.boxplot([pval05200lcd['SHD'], pval052000lcd['SHD'], pval05200stable['SHD'], pval052000stable['SHD'],  pval05200original['SHD'],pval052000original['SHD']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax3.set_title('alpha = 0.05')
    bplot4 = ax4.boxplot([pval005200lcd['SHD'], pval0052000lcd['SHD'], pval005200stable['SHD'], pval0052000stable['SHD'],  pval005200original['SHD'],pval0052000original['SHD']], vert = True, patch_artist=True,labels=['LCD', 'l', 'OPC', 'o', 'SPC', 's'])
    ax4.set_title('alpha = 0.05')
    ax3.set_ylabel('SHD')

    # fill with colors
    colors = ['pink', 'lightblue','pink', 'lightblue','pink', 'lightblue']
    for bplot in (bplot1, bplot2, bplot3, bplot4):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
    # ax1.legend([bplot1["boxes"][0], bplot1["boxes"][1]], ["200 Samples", "2000 Samples"], loc='lower right')
    plt.subplots_adjust(hspace=0.7)
    plt.show()

if __name__ == '__main__':
    lcd_metrics = read_csv("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/Metrics/r_lcd_learned_cg_metrics.csv")
    cglearn_stable_metrics = read_csv("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/Metrics/r_pc_learned_stable_cg_metrics.csv")
    cglearn_original_metrics = read_csv("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/Metrics/r_pc_learned_original_cg_metrics.csv")
    
    ten_plots(lcd_metrics, cglearn_stable_metrics, cglearn_original_metrics)
    # six_plots(lcd_metrics, cglearn_stable_metrics, cglearn_original_metrics)
    # four_plots(lcd_metrics, cglearn_stable_metrics, cglearn_original_metrics)