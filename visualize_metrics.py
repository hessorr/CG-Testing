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
    cglearn_metrics = read_csv("/Users/Oliviahess/Documents/Programs/Independent Study/CG-Testing/Metrics/r_lcd_learned_cg_metrics.csv")
    

    values1 = lcd_metrics['pval']
    values2 = cglearn_metrics['pval']
    # Prepare the data for plotting
    data_to_plot = [values1, values2]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Create the box plot
    # You can customize the labels to something more descriptive if you like
    ax.boxplot(data_to_plot, labels=['Dataset 1', 'Dataset 2'])

    # Add a title and axis labels
    ax.set_title('Comparison of Values in Two Datasets')
    ax.set_xlabel('Dataset')
    ax.set_ylabel('Value')

    # Show the plot
    plt.show()