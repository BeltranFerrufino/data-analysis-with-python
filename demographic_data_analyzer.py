import pandas as pd
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
census_income = fetch_ucirepo(id=20) 

df = census_income.data.features

# Filtrar personas que ganan más de 50k
df['>50K'] = df['fnlwgt'] > 50000  # Suponiendo que fnlwgt indica ingresos (ajusta esto si es necesario)

def respuesta_2():
    # Pregunta 1: ¿Cuántas personas de cada raza están representadas en este conjunto de datos?
    cantidad_raza = df['race'].value_counts()

    # Pregunta 2: ¿Cuál es la edad promedio de los hombres?
    edad_media_hombre = df[df['sex'] == 'Male']['age'].mean().round(1)

    # Pregunta 3: ¿Cuál es el porcentaje de personas que tienen un grado de licenciatura?
    porcentaje_licenciatura = ((df['education'] == 'Bachelors').mean() * 100).round(1)

    # Pregunta 4: ¿Qué porcentaje de personas con una educación avanzada (Bachelors, Masters, Doctorate) ganan más de 50k?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    educacion_avanzada = ((higher_education['>50K']).mean() * 100).round(1)

    # Pregunta 5: ¿Qué porcentaje de personas sin una educación avanzada generan más de 50k?
    poca_educacion = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    educacion_no_avanzada = ((poca_educacion['>50K']).mean() * 100).round(1)

    # Pregunta 6: ¿Cuál es el mínimo número de horas que una persona trabaja por semana?
    min_horas = df['hours-per-week'].min()

    # Pregunta 7: ¿Qué porcentaje de personas que trabajan el mínimo de horas por semana tiene un salario de más de 50k?
    min_trabajo = df[df['hours-per-week'] == min_horas]
    min_50k = ((min_trabajo['>50K']).mean() * 100).round(1)

    # Pregunta 8: ¿Qué país tiene el porcentaje más alto de personas que ganan >50k y cuál es ese porcentaje?
    pais_porcentaje = (df[df['>50K']].groupby('native-country').size() / df.groupby('native-country').size() * 100).dropna()
    pais_gana_mas = pais_porcentaje.idxmax()
    pais_gana_mas_porcentaje = round(pais_porcentaje.max(), 1)

    # Pregunta 9: Identifica la ocupación más popular de aquellos que ganan >50k en India
    india = df[(df['native-country'] == 'India') & (df['>50K'])]['occupation'].value_counts().idxmax()

    # Devuelve las respuestas
    return {
        'cantidad_raza': cantidad_raza,
        'Edad_media_hombre': edad_media_hombre,
        'porcentaje_licenciatura': porcentaje_licenciatura,
        'educacion_avanzada': educacion_avanzada,
        'educacion_no_avanzada': educacion_no_avanzada,
        'min_horas': min_horas,
        'min_50k': min_50k,
        'pais_gana_mas': pais_gana_mas,
        'pais_gana_mas_porcentaje': pais_gana_mas_porcentaje,
        'india': india
    }

# Ejecuta la función
respuesta = respuesta_2()
display(respuesta)
