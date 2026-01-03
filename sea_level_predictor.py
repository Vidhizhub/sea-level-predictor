import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(years_all, intercept + slope * years_all, color='red', label='Best Fit: All Data')

    # Create second line of best fit (year 2000+)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, intercept2 + slope2 * years_recent, color='green', label='Best Fit: 2000+')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
