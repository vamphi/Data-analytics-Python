import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    fig = df.plot(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',xlabel="Date" , ylabel="Page Views", figsize=(20,10), legend =False, color='red')
    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
  
    df_bar = df.reset_index().copy()
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month
    df_bar = df_bar.groupby(["month",'year'])['value'].mean().reset_index()

    
    # Draw bar plot

    fig = sns.catplot(data=df_bar, x ='year', y ='value', hue = 'month', kind='bar', legend_out = False, palette = "bright")
    fig.set_axis_labels("Years", "Average Page Views")
    fig.set_xticklabels(rotation=90) 
    fig._legend.set_title('Months')
    new_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for t, l in zip(fig._legend.texts, new_labels):
        t.set_text(l)
      
    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    df_box = pd.DataFrame(df_box)

    plt.rcParams["figure.figsize"] = [18, 7]
    fig, axbar =plt.subplots(1,2)
    sns.boxplot(x="year", y="value", data=df_box, fliersize=2, linewidth=1, ax=axbar[0])
    sns.boxplot(x="month", y="value", data=df_box, fliersize=2, linewidth=1, order =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] , ax=axbar[1])
    axbar[0].set_title('Year-wise Box Plot (Trend)')
    axbar[1].set_title('Month-wise Box Plot (Seasonality)')
    axbar[0].set_ylabel('Page Views')
    axbar[1].set_ylabel('Page Views')
    axbar[0].set_xlabel('Year')
    axbar[1].set_xlabel('Month')
    axbar[0].set_ylim(0,200000)
    axbar[1].set_ylim(0,200000)
    axbar[0].set_yticks(range(0,200001,20000))
    axbar[1].set_yticks(range(0,200001,20000))

    fig = fig.figure
  
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
