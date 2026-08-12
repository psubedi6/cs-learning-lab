import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#loads csv file
#filr_path is parameter we'll pass later; location of csv

def load_data(file_path):
    return pd.read_csv(file_path)