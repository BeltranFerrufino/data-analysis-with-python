import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2050))
    ax.plot(years_extended, intercept + slope * years_extended, 'r', label='Best Fit Line 1880-2050')

    # Create second line of best fit
    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2050))
    ax.plot(years_recent, intercept_recent + slope_recent * years_recent, 'b', label='Best Fit Line 2000-2050')

    # Add labels, title, and legend
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
