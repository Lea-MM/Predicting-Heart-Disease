import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# initializing the constants
file = 'heart_disease.csv'
categorical_columns = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope', 'HeartDisease', 'FastingBS']

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
    df (Pandas DataFrame containing the data).

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

def plot_categorical_counts(df, categorical_columns, columns_per_row):
    """
    Plots bar charts for each categorical column in the given DataFrame.
    
    Parameters:
    df (Pandas DataFrame containing the data).
    categorical_columns (List of strings representing categorical column names to analyze).
    
    The function generates bar charts for each column and displays them in a clean layout.
    """
    
    # Calculate the number of rows needed
    num_columns = len(categorical_columns)
    num_rows = math.ceil(num_columns / columns_per_row)
    
    # setting up the plot
    fig, axes = plt.subplots(num_rows, columns_per_row, figsize=(columns_per_row * 3, num_rows * 5))
    axes = axes.flatten()  # flatten axes array for easy indexing

    for i, column in enumerate(categorical_columns):
        category_counts = df[column].value_counts() 
        
        # plotting bar chart
        axes[i].bar(category_counts.index, category_counts.values, color='skyblue')
        
        # adding labels and title
        axes[i].set_title(f'{column}', fontsize=10, fontweight='bold')
        axes[i].set_xlabel('Categories', fontsize=9)
        axes[i].set_ylabel('Count', fontsize=9)
        axes[i].tick_params(axis='x', rotation=45) 
        
        # adding data labels on top of the bars
        for j, value in enumerate(category_counts.values):
            axes[i].text(j, value + 1, str(value), ha='center', fontsize=8)
    
    # hiding unused subplots if any
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    
    # adjusting layout
    plt.tight_layout()
    plt.show()
    

### Execute Functions
analyze_numerical_columns(data)
plot_categorical_counts(data, categorical_columns=categorical_columns, columns_per_row=4)