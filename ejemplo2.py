import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar datos
st.set_page_config(page_title="Encuesta Oficial delivery ") 
st.header('Resultados Encuestas Nacionales delivery Bolivia 2023') 
st.subheader('delivery Bolivia 2023') 

df = pd.read_spss("Basefinal.sav")

# Mapeo de categorías
def map_categories(column, mapping):
    return column.map(mapping).fillna('otros')

p20a_mapping = {
    'Mejores posibilidades de ingreso': 'Mejores posibilidades de ingreso',
    'Mayor libertad de horarios': 'Mayor libertad de horario',
    'Era la única opción de trabajo disponible': 'Era la única opción de trabajo disponible'
}

df['p20a'] = map_categories(df['p20a'], p20a_mapping)

def map_periodo(p67b):
    mapping = {
        'Semana': 4,
        'Quincena': 2,
        'Mes': 1,
        'Trimestre': 0.33
    }
    return mapping.get(p67b, 0.17)

df['p67b'] = df['p67b'].fillna('Mes')
df['periodo'] = df['p67b'].map(map_periodo)
df['p66a'] = df['p66a'].astype(int)
df['p66b'] = df['p66b'].astype(int)
df['periodo'] = df['periodo'].astype(int)
df['p67a'] = df['p67a'].astype(int)
# Cálculos adicionales
df['mantenimiento'] = df['p67a'] * df['periodo']
df['gastos'] = df['mantenimiento'] + df['p66a'] + df['p66b']
df['ingresom'] = df['p60a1'].apply(lambda x: 2000 if x == 'Ns/Nr' else x)
df['ingresor'] = df['ingresom'] - df['gastos']

def categorizar_ingresos(ingresor):
    if ingresor < 2250:
        return 'minimo'
    elif ingresor < 4500:
        return 'medio'
    else:
        return 'alto'

df['categoria'] = df['ingresor'].apply(categorizar_ingresos)

def map_years_of_study(p4):
    if p4 in ('Ninguno', 'Primaria completa', 'Secundaria incompleta', 'Secundaria completa'):
        return 'Secundario'
    else:
        return 'Alto'

df['educacion'] = df['p4'].map(map_years_of_study)

def map_jefe(p8):
    return 'jefe' if p8 == 'Jefe o jefa del hogar' else 'no jefe'

df['jefe'] = df['p8'].map(map_jefe)

def map_pluriactividad(pluriactividad):
    return 'Solo trabaja como delivery' if pluriactividad == 'Solo trabaja como delivery' else 'Alterna con otro trabajo y/o estudios'

df['pluriactividad'] = df['p21'].map(map_pluriactividad)
def a(PrimeroTrabajo):
    if PrimeroTrabajo == 'Primertrabajo':
        return 'Primer trabajo'
    else:
        return'Tenia Trabajo'
def map_razones(razones):
    razones_mapping = {
        'Era un empleo temporal': 'Era un empleo temporal',
        'Fue despedido': 'Razones de la demanda',
        'La empresa, negocio, actividad se cerró': 'Razones de la demanda',
        'Por falta de capital o de clientes': 'Razones de la demanda',
        'Fue obligado a renunciar': 'Razones de la demanda',
        'Razones personales': 'Razones personales',
        'Razones económicas/ bajos ingresos': 'Razones económicas/ bajos ingresos'
    }
    return razones_mapping.get(razones, 'Renuncio')
df['edad'] = df['edad'].astype(int)
edad=df['edad'].unique().tolist()
df['razones'] = df['p14'].map(map_razones)
df['edad'] = df['edad'].astype(int)
edad=df['edad'].unique().tolist()
# Slider de edad
edad_selector = st.slider("Edad persona encuestada:",
                          min_value=df['edad'].min(),
                          max_value=df['edad'].max(),
                          value=(df['edad'].min(), df['edad'].max()))

# Filtrar datos
mask = (df['edad'].between(*edad_selector))
df_filtered = df[mask]
df['p12']=df['p12'].cat.add_categories('Primertrabajo').fillna('Primertrabajo')
df['PrimeroTrabajo']=df['p12']
df['PrimeroTrabajo'] = df['PrimeroTrabajo'].apply(a)
# Gráfico de barras
st.subheader('Porcentaje de Repartidores que tenían un trabajo antes')
df_agrupado = df_filtered.groupby('PrimeroTrabajo').size().reset_index(name='count')
total = df_agrupado['count'].sum()
df_agrupado['porcentaje'] = (df_agrupado['count'] / total * 100).round(0).astype(int)

bar_chart = px.bar(df_agrupado, 
                   x='PrimeroTrabajo',
                   y='porcentaje',
                   text='porcentaje',
                   color_discrete_sequence=['#f5b632']
                   )

bar_chart.update_traces(texttemplate='%{text}%', textposition='inside')

st.plotly_chart(bar_chart, use_container_width=True)

# Gráfico de torta
st.subheader('Razones para convertirse en repartidor')
fig_pie = px.pie(df_filtered, 
                 names='razones', 
                 title='Razones para convertirse en repartidor',
                 color_discrete_sequence=px.colors.qualitative.Set3)

st.plotly_chart(fig_pie, use_container_width=True)

# Gráfico de barras apiladas
st.subheader('Educación y categoría de ingresos')
df_educacion = df_filtered.groupby(['educacion', 'categoria']).size().reset_index(name='count')
df_educacion = df_educacion.pivot(index='educacion', columns='categoria', values='count').fillna(0)
df_educacion['total'] = df_educacion.sum(axis=1)
df_educacion['Secundario'] = df_educacion['Secundario'] / df_educacion['total'] * 100
df_educacion['Alto'] = df_educacion['Alto'] / df_educacion['total'] * 100
df_educacion['Medio'] = df_educacion['Medio'] / df_educacion['total'] * 100
df_educacion = df_educacion[['Secundario', 'Medio', 'Alto']]

stacked_bar_chart = px.bar(df_educacion,
                            title='Educación y categoría de ingresos',
                            labels={'value': 'Porcentaje (%)'},
                            color_discrete_sequence=px.colors.qualitative.Pastel1)

st.plotly_chart(stacked_bar_chart, use_container_width=True)

# Gráfico de dispersión
st.subheader('Relación entre gastos e ingresos')
scatter_plot = px.scatter(df_filtered,
                          x='gastos',
                          y='ingresor',
                          title='Relación entre gastos e ingresos',
                          color_discrete_sequence=['#0d76a8'])

scatter_plot.update_xaxes(title_text='Gastos')
scatter_plot.update_yaxes(title_text='Ingresos')

st.plotly_chart(scatter_plot, use_container_width=True)