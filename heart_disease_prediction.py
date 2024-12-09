import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# initializing the constants
file = 'heart_disease.csv'

# reading the dataset into a pandas dataframe
data = pd.read_csv(file)

def analyze_numerical_columns(df):
    """
    Analyzes numerical columns in a DataFrame by performing the following tasks:
    
    1. Displays the first five rows of the DataFrame.
    2. Prints the number of features (columns) and observations (rows).
    3. Identifies and displays the data types of the columns.
    4. Provides descriptive statistics for the numerical columns.
    5. Checks and displays the count of missing values for each column.

    Parameters:
    df (A globally defined DataFrame).

    Returns:
    None (Prints the analysis results directly).
    """
    
    # displaying the first five rows of the dataframes
    print(df.head())

    # printing the number of features and observations
    print(f"Number of features (columns): {df.shape[1]}")
    print(f"Number of observation (rows): {df.shape[0]}")

    # identifying the data types
    print("\nColumn Data Types:")
    print(df.dtypes)

    # displaying the descriptive statistics for the numerical columns
    print("\nDescriptive Statistics:")
    print(df.describe())

    # checking for missing values 
    print(f"\n Missing Values: \n{df.isnull().sum()}")


### Execute Functions
# analyze_numerical_columns(data)
