import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

df

# 2:  
df['overweight'] = (df['weight']/((df['height']/100)**2) > 25).astype(int)

# 3: 
df[['gluc','cholesterol']] = (df[['gluc','cholesterol']] > 1).astype(int)




def draw_cat_plot():

    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig




    fig.savefig('catplot.png')
    return fig



    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
  
    df_heat = df[ 
        ( df['ap_lo'] <= df['ap_hi'] ) & 
        ( df['height'] >= df['height'].quantile(0.025) ) & 
        ( df['height'] <= df['height'].quantile(0.975) ) & 
        ( df['weight'] >= df['weight'].quantile(0.025) ) & 
        ( df['weight'] <= df['weight'].quantile(0.975) ) 
    ]


    corr = df_heat.corr()

    mask = np.triu(corr)
    fig, ax = plt.subplots(figsize=(11, 9))

    #
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=.5, square=True, ax=ax)




    # 16
    fig.savefig('heatmap.png')
    return fig
