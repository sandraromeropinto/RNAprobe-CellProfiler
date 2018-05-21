# reads data from CellProfiler output Nuclei.csv
import pandas as pd
import numpy as np

def DataReader(file):
    f = open(file)
    # read data into a dictionary where each entry is the nuclei number
    data = pd.read_csv(f)
    assert isinstance(data, object)

    #select only important fields
    data = data.apply(pd.to_numeric)
    return data[['ObjectNumber', 'Children_FinalDots_C2_Count', 'Children_FinalDots_C3_Count']]

