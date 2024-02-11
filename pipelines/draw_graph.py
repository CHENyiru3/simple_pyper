import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import NewType

file_path = NewType('file_path', str)
column_name = NewType('column_name', str)

def read_file(file_path: file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.csv':
        return pd.read_csv(file_path)
    elif file_extension == '.tsv':
        return pd.read_csv(file_path, sep='\t')
    else:
        raise ValueError("Invalid file extension. Only .csv and .tsv files are supported.")

def plot_histogram(df: pd.DataFrame, column: column_name, output_file: file_path):
    df[column].hist()
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column}')
    plt.savefig(output_file)

def main(file_path: file_path, column: column_name, output_file: file_path):
    df = read_file(file_path)
    plot_histogram(df, column, output_file)

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2], sys.argv[3])