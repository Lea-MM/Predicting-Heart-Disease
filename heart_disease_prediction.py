import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# initializing the constants
file = 'heart_disease.csv'

# reading the dataset into a pandas dataframe
df = pd.read_csv(file)

# displaying the first five rows of the dataframes
print(df.head())

# printing the number of features and observations
print(f"Number of features (columns): {df.shape[1]}")
print(f"Number of observation (rows): {df.shape[0]}")

