import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot.scatter(x='Year',y='CSIRO Adjusted Sea Level')

    # Create first line of best fit

    x=df['Year']
    x_ext=pd.Series([x for x in range(1880, 2051)])
    y=df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    plt.plot(x_ext, res.intercept + res.slope*x_ext, 'r')

    # Create second line of best fit

    df1 = df.loc[(df['Year'] >= 2000)].copy()
    x1=df1['Year']
    x_ext1=pd.Series([x for x in range(2000, 2051)])
    y1=df1['CSIRO Adjusted Sea Level']
    res1 = linregress(x1, y1)
    plt.plot(x_ext1, res1.intercept + res1.slope*x_ext1, 'g',label='Year')
  
    # Add labels and title

    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Sea Level (inches)', fontsize=14)
    plt.title('Rise in Sea Level', fontsize=18)
    plt.xticks(range(1850,2076,25))
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()