import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight']/((df['height']/100)**2)
df['overweight'] = (df['overweight']>25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.cholesterol = df.cholesterol.replace({1: 0, (2,3): 1})
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active',  'overweight'])
  
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat=df_cat.groupby(["cardio","variable","value"]).size().to_frame("total").reset_index()
    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, x ='variable', y ='total', hue = 'value', col='cardio', kind='bar')
    fig.set_axis_labels('variable', 'total')
    # Do not modify the next two lines
    fig.set_ylabels('total')
    fig.savefig('catplot.png')
    fig = fig.fig
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[ (df['ap_lo']<= df['ap_hi']) & (df['height']>=df['height'].quantile(0.025)) & (df['height']<=df['height'].quantile(0.975)) & (df['weight']>=df['weight'].quantile(0.025)) & (df['weight']<=df['weight'].quantile(0.975))]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr,fmt='.1f', mask=mask, annot = True, square=True, linewidth = 1, vmax = 0.3)

    # Do not modify the next two lines
    fig=fig.figure
    fig.savefig('heatmap.png')
    return fig
