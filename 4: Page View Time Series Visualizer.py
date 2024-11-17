import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig

 
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    fig = df_bar.plot.bar(legend=True, figsize=(10, 5), ylabel='Average Page Views', xlabel='Years').figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    fig
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  df_box['month_num'] = df_box['date'].dt.month
  df_box = df_box.sort_values('month_num')
  fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharex=False, sharey=False)
  axes[0] = sns.boxplot(x=df_box['year'], y=df_box['value'], ax=axes[0])
  axes[1] = sns.boxplot(x=df_box['month'], y=df_box['value'], ax=axes[1])
  axes[0].set_title('Year-wise Box Plot (Trend)')
  axes[0].set_ylabel('Page Views')
  axes[1].set_title('Month-wise Box Plot (Seasonality)')
  axes[1].set_xlabel('Month')
  axes[1].set_ylabel('Page Views')

  fig.savefig('box_plot.png')
  return fig


 
