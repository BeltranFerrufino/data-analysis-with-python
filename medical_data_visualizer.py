import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

df

# 2: Agregue una overweightcolumna a los datos. Para determinar si una persona tiene sobrepeso, primero calcule su IMC dividiendo su peso en kilogramos por el cuadrado de su altura en metros. Si ese valor es > 25, entonces la persona tiene sobrepeso. Use el valor 0de NO sobrepeso y el valor 1de sobrepeso.
# df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['weight']/((df['height']/100)**2) > 25).astype(int)

# df['overweight'] = None

# 3: Normalice los datos haciendo que 0siempre sean buenos y 1siempre malos. Si el valor de cholesterolo gluces 1, establezca el valor en 0. Si el valor es mayor que 1, establezca el valor en 1.
df[['gluc','cholesterol']] = (df[['gluc','cholesterol']] > 1).astype(int)



# 4: Dibuje la gráfica categórica en la draw_cat_plotfunción.

def draw_cat_plot():

    # 5: Cree un DataFrame para el gráfico de gatos utilizando pd.meltvalores de cholesterol, gluc, smoke, alco, activey overweighten la df_catvariable.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # df_cat = None


    # 6: Agrupe y reformatee los datos df_catpara dividirlos por cardio. Muestre los recuentos de cada característica. Deberá cambiar el nombre de una de las columnas para que catplotfuncione correctamente.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # df_cat = None
    

    # 7: Convierta los datos en longformato y cree un gráfico que muestre los recuentos de valores de las características categóricas utilizando el siguiente método proporcionado por la importación de la biblioteca seaborn: sns.catplot().
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig
    # fig = None




    # 8: Obtenga la cifra de la salida y almacénela en la figvariable 
    fig.savefig('catplot.png')
    return fig

    # fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11: Limpie los datos de la df_heatvariable filtrando los siguientes segmentos de pacientes que representan datos incorrectos:
    # La presión diastólica es más alta que la sistólica (Mantenga los datos correctos con (df['ap_lo'] <= df['ap_hi']))
    # La altura es menor que el percentil 2,5 (Mantenga los datos correctos con (df['height'] >= df['height'].quantile(0.025)))
    # La altura es mayor que el percentil 97,5
    # El peso es menor que el percentil 2,5
    # El peso es mayor que el percentil 97,5
    df_heat = df[ 
        ( df['ap_lo'] <= df['ap_hi'] ) & 
        ( df['height'] >= df['height'].quantile(0.025) ) & 
        ( df['height'] <= df['height'].quantile(0.975) ) & 
        ( df['weight'] >= df['weight'].quantile(0.025) ) & 
        ( df['weight'] <= df['weight'].quantile(0.975) ) 
    ]


    # df_heat = None

    # 12 : Calcular la matriz de correlación y almacenarla en la corrvariable.
    corr = df_heat.corr()

    # corr = None

    # 13: Genere una máscara para el triángulo superior y guárdela en la maskvariable.
    mask = np.triu(corr)
    # mask = None



    # 14: Configurar la matplotlibfigura.
    fig, ax = plt.subplots(figsize=(11, 9))

    #
    # fig, ax = None

    # 15: Grafique la matriz de correlación utilizando el método proporcionado por la seabornbiblioteca de importación: sns.heatmap().
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=.5, square=True, ax=ax)




    # 16
    fig.savefig('heatmap.png')
    return fig
