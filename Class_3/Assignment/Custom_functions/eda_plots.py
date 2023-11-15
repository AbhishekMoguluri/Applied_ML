# Import the required libraries for data manipulation and plotting
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def diagnostic_plots(df, variable):
    """
    Generate diagnostic plots for a given variable.
    
    Parameters:
    - df (pd.DataFrame): The input data frame containing the variable.
    - variable (str): The name of the variable for which to create the diagnostic plots.
    
    This function generates three diagnostic plots:
    1. Histogram for distribution visualization.
    2. Boxplot for outlier detection.
    3. Q-Q plot for normality assessment.
    """
    
    # Create a new figure for plotting
    plt.figure(figsize=(16, 4))
    
    # First subplot: Histogram
    plt.subplot(1, 3, 1)
    sns.histplot(df, x=variable, bins=30)
    plt.title('Histogram')
    
    # Second subplot: Boxplot
    plt.subplot(1, 3, 2)
    sns.boxplot(y=df[variable])
    plt.title('Boxplot')
    
    # Third subplot: Q-Q plot
    plt.subplot(1, 3, 3)
    stats.probplot(df[variable], dist="norm", plot=plt)
    plt.title('Q-Q plot')
    
    # Show all the subplots
    plt.show()

def plot_target_by_category(df, target, category, ylabel):
    """
    Plot the target variable as aggregated by a categorical variable.
    
    Parameters:
    - df (pd.DataFrame): The input data frame.
    - target (str): The name of the target variable.
    - category (str): The name of the categorical variable.
    - ylabel (str): The label for the y-axis.
    
    This function computes and plots the average value of the target variable per category.
    """
    
    # Compute the mean of the target variable by category
    percent_churn_by_category = df.groupby(category)[target].mean().round(2).reset_index()
    
    # Create a new figure for plotting
    plt.figure(figsize=(8, 5))
    
    # Create a bar plot for the target variable by category
    plt.bar(percent_churn_by_category[category].values, percent_churn_by_category[target].values)
    
    # Set the x and y labels and the title
    plt.xlabel(category)
    plt.ylabel(ylabel)
    plt.title(f'{ylabel} by {category}')
    
    # Show the plot
    plt.show()

