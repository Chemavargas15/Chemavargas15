
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import panel as pn
pn.extension('tabulator')
st.set_page_config(page_title="Encuesta Oficial delivery ") 
st.header('Resultados Encuestas Nacionales  delivery Bolivia 2023') 
st.subheader('delivery Bolivia 2023') 
image_path = "cedla.png"

# Add a radio button in the Streamlit sidebar using "with" notation
with st.sidebar:
    st.image(image_path, caption="Mi Imagen", use_column_width=True)
    st.header('Resultados Encuestas Nacionales  delivery Bolivia 2023') 
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus sit amet ante a risus fermentum malesuada luctus sed ante. Vestibulum bibendum dui ac diam feugiat, iaculis pretium massa faucibus. Nullam molestie convallis nisi ut gravida. Sed sed consequat purus, a fringilla tellus. Nunc sed pulvinar nisl. Curabitur lorem ex, facilisis a imperdiet dignissim, aliquam a mauris. Praesent blandit feugiat quam vitae tincidunt. Sed sem dui, consequat vel pharetra a, lobortis nec ex. Quisque dignissim pulvinar felis, auctor consectetur sem semper in. Ut congue dolor ac lorem venenatis, sed iaculis odio scelerisque. Fusce sodales eu metus vitae lacinia. Nam placerat vel mauris a scelerisque.')
df2=pd.read_csv('penguins_v1.csv')
df = pd.read_spss("/workspaces/Chemavargas15/BaseFinal.sav")
column_headers = list(df.columns.values)
def P(p20a):
    if p20a == 'Mejores posibilidades de ingreso':
        return 'Mejores posibilidades de ingreso' 
    if p20a == 'Mayor libertad de horarios':
        return 'Mayor libertad de horario' 
    if p20a == 'Era la única opción de trabajo disponible':
        return 'Era la única opción de trabajo disponible'
    else:
        return 'otros'
def f(p67b):
    if p67b == 'Semana':
        return 4
    if p67b == 'Quincena':
        return 2
    if p67b == 'Mes':
        return 1
    if p67b == 'Trimestre':
        return 0.33 
    else:
        return 0.17
def d(dependencia):
    if dependencia == 0:
        return 'Nadie'
    if dependencia == 1 or dependencia == 2:
        return 'Hasta dos' 
    else:
        return 'Mas de dos'
def x(p60a1):
    if p60a1 == 'Ns/Nr':
        return 2000
    else:
        return p60a1
def years_of_study(p4):
    if p4 == 'Ninguno' or p4 == 'Primaria completa' or p4 == 'Secundaria incompleta' or p4 == 'Secundaria completa':
        return 'Secundario'
    else:
        return 'Alto'
def asalariado(anterior):
    if anterior ==  'Empleado' or anterior == 'Obrero' or anterior == 'Profesional independiente/ Consultor':
        return 'asalariado'
    else:
        return 'no asalariado'
def jefe(p8):
    if p8 == 'Jefe o jefa del hogar':
        return 'jefe'
    else:
        return 'no jefe'
def m(pluriactividad):
    if pluriactividad == 'Solo trabaja como delivery':
        return 'Solo trabaja como delivery'
    else:
        return 'Alterna con otro trabajo y/o estudios'
def z(razones):
    if razones == 'Era un empleo temporal':
        return 'Era un empleo temporal'
    if razones == 'Fue despedido' or razones == 'La empresa, negocio, actividad se cerró' or razones == 'Por falta de capital o de clientes' or razones =='Fue obligado a renunciar':
        return 'Razones de la demanda'
    if razones == 'Razones personales':
        return 'Razones personales'
    if razones == 'Razones económicas/ bajos ingresos':
        return 'Razones económicas/ bajos ingresos'
    else:
        return 'Renuncio'
def t(menores):
    if menores == 0:
        return 'ninguno'
    else:
        return 'menores en el hogar'
def anti(antiguedad):
    if antiguedad <=  12:
        return 1
    if antiguedad <= 24:
        return 2
    if antiguedad <= 33:
        return 3
    else:
        return 4


def a(PrimeroTrabajo):
    if PrimeroTrabajo == 'Primertrabajo':
        return 'Primer trabajo'
    else:
        return'Tenia Trabajo'
df['WPESO']=df['WPESO'].round(0).astype(int)
df = df.set_index(['nt', 'dia', 'mes', 'ciudad', 'sexo', 'edad', 'edadan', 'EDADX', 'EDADG', 'p3', 'P3G', 'p4', 'P4G', 'p5', 'p6', 'P6X', 'p7', 'P7X', 'P7ME15', 'P7ME15X', 'p8', 'p9', 'p10', 'P10X', 'P10Y', 'p11', 'P11X', 'P11Y', 'P11Z', 'p12', 'p12a', 'p13a', 'p13b', 'P13', 'P13X', 'P13Y', 'p14', 'p10p15', 'p15', 'P15X', 'P15Y', 'p16', 'P16X', 'P16Y', 'P16Z', 'p17', 'p17a', 'p18a', 'p18b', 'P18', 'P18X', 'P18Y', 'p19a', 'p19b', 'P19', 'P19X', 'P19Y', 'p20a', 'p20b', 'p20c', 'p21', 'p15p22', 'p22', 'P22X', 'P22Y', 'p23', 'P23X', 'P23Y', 'P23Z', 'p24', 'p24a', 'p25', 'P25X', 'P25Y', 'p26', 'p27', 'P27X', 'P27Y', 'p28', 'p29a', 'p29b', 'p29c', 'p29d', 'p29e', 'p29f', 'P29AX', 'P29BX', 'P29CX', 'P29DX', 'P29EX', 'P29FX', 'P29SUM', 'P29SUMX', 'p30', 'P30WP', 'p30a', 'P30AX', 'P30AY', 'p31a', 'p31b', 'p31c', 'p31d', 'p31e', 'p31f', 'p31g', 'p31h', 'p31i', 'p31j', 'p31k', 'p31l', 'p31m', 'p31n', 'P31AY', 'P31BY', 'P31CY', 'P31DY', 'P31EY', 'P31FY', 'P31GY', 'P31HY', 'P31IY', 'P31JY', 'P31KY', 'p32', 'p32a', 'p33', 'p34', 'p35', 'p36a', 'p36b', 'p36c', 'p37', 'p37bs', 'p37t', 'p38', 'p39', 'p40a1', 'p40a2', 'p40b1', 'p40b2', 'p40c1', 'p40c2', 'p40d1', 'p40d2', 'p40e1', 'p40e2', 'p40f1', 'p40f2', 'P40A1Y', 'P40B1Y', 'P40C1Y', 'P40D2Y', 'P40E2Y', 'P40F2Y', 'P40A2Y', 'P40B2Y', 'P40C2Y', 'p41', 'p42', 'P42X', 'P42Y', 'p43a', 'p43b', 'p43c', 'p43d', 'p43e', 'P43AY', 'P43BY', 'P43CY', 'P43DY', 'P43EY', 'p43f', 'p43g', 'p43h', 'p44', 'p45a', 'p45b', 'P45AY', 'P45BY', 'p45c', 'p45d', 'p45e', 'p46', 'p46p52', 'p47', 'P47X', 'p48', 'p49', 'p50', 'P50X', 'P50Y', 'p51', 'p52', 'p53a', 'p53b', 'p53c', 'p54', 'p55a', 'p55b', 'p55c', 'p56', 'p57a1', 'P57A1X', 'P57A1Y', 'p58a1', 'P58A1X', 'P58A1Y', 'p58b1', 'P58B1X', 'P58B1Y', 'p57a2', 'P57A2X', 'P57A2Y', 'P57A3', 'P57A3X', 'P57A3Y', 'p58a2', 'P58A2X', 'P58A2Y', 'p58b2', 'P58B2X', 'P58B2Y', 'p59', 'p60a1', 'P60A1X', 'P60A1Y', 'p60a2', 'P60A2X', 'P60A2Y', 'P60A3', 'P60A3X', 'P60A3Y', 'p61', 'p62', 'p63', 'p64', 'p64a', 'p65', 'P65X', 'p66a', 'P66AX', 'P66AY', 'p66b', 'P66BX', 'P66BY', 'p67a', 'p67b', 'P67', 'P67X', 'P67Y', 'p68', 'P68X', 'P68Y', 'P68MES', 'P68MESX', 'P68MESY', 'p69a', 'P69AX', 'P69AY', 'p69b', 'P69BX', 'P69BY', 'p70', 'p71', 'p71a', 'p71b', 'p72m1lu1', 'p72m1lu2', 'p72m1lu3', 'p72m1lu4', 'p72m1lu5', 'p72m1ma1', 'p72m1ma2', 'p72m1ma3', 'p72m1ma4', 'p72m1ma5', 'p72m1mi1', 'p72m1mi2', 'p72m1mi3', 'p72m1mi4', 'p72m1mi5', 'p72m1ju1', 'p72m1ju2', 'p72m1ju3', 'p72m1ju4', 'p72m1ju5', 'p72m1vi1', 'p72m1vi2', 'p72m1vi3', 'p72m1vi4', 'p72m1vi5', 'p72m1sa1', 'p72m1sa2', 'p72m1sa3', 'p72m1sa4', 'p72m1sa5', 'p72m1do1', 'p72m1do2', 'p72m1do3', 'p72m1do4', 'p72m1do5', 'P72M1LUH', 'P72M1MAH', 'P72M1MIH', 'P72M1JUH', 'P72M1VIH', 'P72M1SAH', 'P72M1DOH', 'p72m2lu1', 'p72m2lu2', 'p72m2lu3', 'p72m2lu4', 'p72m2lu5', 'p72m2ma1', 'p72m2ma2', 'p72m2ma3', 'p72m2ma4', 'p72m2ma5', 'p72m2mi1', 'p72m2mi2', 'p72m2mi3', 'p72m2mi4', 'p72m2mi5', 'p72m2ju1', 'p72m2ju2', 'p72m2ju3', 'p72m2ju4', 'p72m2ju5', 'p72m2vi1', 'p72m2vi2', 'p72m2vi3', 'p72m2vi4', 'p72m2vi5', 'p72m2sa1', 'p72m2sa2', 'p72m2sa3', 'p72m2sa4', 'p72m2sa5', 'p72m2do1', 'p72m2do2', 'p72m2do3', 'p72m2do4', 'p72m2do5', 'P72M2LUH', 'P72M2MAH', 'P72M2MIH', 'P72M2JUH', 'P72M2VIH', 'P72M2SAH', 'P72M2DOH', 'p72m3lu1', 'p72m3lu2', 'p72m3lu3', 'p72m3lu4', 'p72m3lu5', 'p72m3ma1', 'p72m3ma2', 'p72m3ma3', 'p72m3ma4', 'p72m3ma5', 'p72m3mi1', 'p72m3mi2', 'p72m3mi3', 'p72m3mi4', 'p72m3mi5', 'p72m3ju1', 'p72m3ju2', 'p72m3ju3', 'p72m3ju4', 'p72m3ju5', 'p72m3vi1', 'p72m3vi2', 'p72m3vi3', 'p72m3vi4', 'p72m3vi5', 'p72m3sa1', 'p72m3sa2', 'p72m3sa3', 'p72m3sa4', 'p72m3sa5', 'p72m3do1', 'p72m3do2', 'p72m3do3', 'p72m3do4', 'p72m3do5', 'P72M3LUH', 'P72M3MAH', 'P72M3MIH', 'P72M3JUH', 'P72M3VIH', 'P72M3SAH', 'P72M3DOH', 'P72LU', 'P72LUX', 'P72LUY', 'P72MA', 'P72MAX', 'P72MAY', 'P72MI', 'P72MIX', 'P72MIY', 'P72JU', 'P72JUX', 'P72JUY', 'P72VI', 'P72VIX', 'P72VIY', 'P72SA', 'P72SAX', 'P72SAY', 'P72DO', 'P72DOX', 'P72DOY', 'P72HRS', 'P72HRSX', 'P72HRSY', 'p76a', 'P76AX', 'P76AY', 'P76AG', 'p76b', 'P76BX', 'P76BY', 'P76BG', 'p76c', 'P76CX', 'P76CY', 'P76CG', 'p77', 'p78a', 'p78b', 'p78c', 'p78d', 'p79', 'P79X', 'P79Y', 'p79km', 'P79KMX', 'p80', 'p80a', 'P80AX', 'P80AY', 'p80b', 'P80BX', 'P80BY', 'p82a', 'P82AY', 'p82b', 'P82BY', 'p82c', 'P82CY', 'p82d', 'P82DY', 'p82e', 'P82EY', 'p82f', 'P82FY', 'p82g', 'P82GY', 'p82h', 'p82i', 'p82j', 'p85a', 'P85AX', 'P85AY', 'P85AG', 'p85b', 'P85BX', 'P85BY', 'P85BG', 'p86a', 'P86AY', 'p86b', 'P86BY', 'p86c', 'P86CY', 'p86d', 'P86DY', 'p86e', 'p86f', 'p86g', 'p87', 'p88', 'p89a', 'p89b', 'p89c', 'p90', 'p90a', 'P90AY', 'p90b', 'P90BY', 'p90c', 'P90CY', 'p90d', 'P90DY', 'p91', 'p91a', 'P91AY', 'p91b', 'P91BY', 'p91c', 'P91CY', 'p91d', 'P91DY', 'p92a', 'P92AY', 'p92b', 'P92BY', 'p92c', 'P92CY', 'p92d', 'P92DY', 'p93', 'p94a', 'P94AY', 'p94b', 'P94BY', 'p94d', 'P94DY', 'p94c', 'P94CY', 'p95', 'p96', 'p97a', 'p97b', 'p97c', 'p98a1', 'p98a2', 'P98A2X', 'p98a3', 'p98b1', 'p98b2', 'P98B2X', 'P98B2DIA', 'P98B2SEM', 'P98B2FIN', 'P98B2MES', 'P98B2DIAG', 'P98B2SEMG', 'p98b3', 'p98c', 'p99a', 'P99AY', 'p99b', 'P99BY', 'p99c', 'P99CY', 'p99d', 'p100', 'p101a', 'P101AY', 'P101AG', 'p101b', 'P101BY', 'P101BG', 'p101c', 'P101CY', 'P101CG', 'p102a', 'P102AY', 'P102AG', 'p102b', 'P102BG', 'P102BY', 'p102c', 'P102CY', 'P102CG', 'p103', 'p104', 'p105', 'p106a', 'p106b', 'p106c', 'p107a', 'p107b', 'p107c', 'p107d', 'p107e', 'p108', 'p108a', 'P108AG', 'p108b', 'P108BG', 'p108c', 'P108CG', 'p109', 'p110', 'p110a', 'P110AG', 'p110b', 'P110BG', 'p110c', 'P110CG', 'p111a', 'P111AG', 'p111b', 'P111BG', 'p111c', 'P111CG', 'p112a', 'p112b', 'p112c', 'p112d', 'p112e', 'p112f', 'p112g', 'da1a', 'da1b', 'da1c', 'xnt', 'obs1', 'obs2', 'obs3', 'obs4', 'obs5', 'obs6', 'obs7', 'obs8', 'obs9', 'obs10', 'EMPR', 'LU0', 'LU1', 'LU2', 'LU3', 'LU4', 'LU5', 'LU6', 'LU7', 'LU8', 'LU9', 'LU10', 'LU11', 'LU12', 'LU13', 'LU14', 'LU15', 'LU16', 'LU17', 'LU18', 'LU19', 'LU20', 'LU21', 'LU22', 'LU23', 'P72M1LUHx', 'P72M2LUHx', 'P72M3LUHx', 'MA0', 'MA1', 'MA2', 'MA3', 'MA4', 'MA5', 'MA6', 'MA7', 'MA8', 'MA9', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'P72M1MAHx', 'P72M2MAHx', 'P72M3MAHx', 'MI0', 'MI1', 'MI2', 'MI3', 'MI4', 'MI5', 'MI6', 'MI7', 'MI8', 'MI9', 'MI10', 'MI11', 'MI12', 'MI13', 'MI14', 'MI15', 'MI16', 'MI17', 'MI18', 'MI19', 'MI20', 'MI21', 'MI22', 'MI23', 'P72M1MIHx', 'P72M2MIHx', 'P72M3MIHx', 'JU0', 'JU1', 'JU2', 'JU3', 'JU4', 'JU5', 'JU6', 'JU7', 'JU8', 'JU9', 'JU10', 'JU11', 'JU12', 'JU13', 'JU14', 'JU15', 'JU16', 'JU17', 'JU18', 'JU19', 'JU20', 'JU21', 'JU22', 'JU23', 'P72M1JUHx', 'P72M2JUHx', 'P72M3JUHx', 'VI0', 'VI1', 'VI2', 'VI3', 'VI4', 'VI5', 'VI6', 'VI7', 'VI8', 'VI9', 'VI10', 'VI11', 'VI12', 'VI13', 'VI14', 'VI15', 'VI16', 'VI17', 'VI18', 'VI19', 'VI20', 'VI21', 'VI22', 'VI23', 'P72M1VIHx', 'P72M2VIHx', 'P72M3VIHx', 'SA0', 'SA1', 'SA2', 'SA3', 'SA4', 'SA5', 'SA6', 'SA7', 'SA8', 'SA9', 'SA10', 'SA11', 'SA12', 'SA13', 'SA14', 'SA15', 'SA16', 'SA17', 'SA18', 'SA19', 'SA20', 'SA21', 'SA22', 'SA23', 'P72M1SAHx', 'P72M2SAHx', 'P72M3SAHx', 'DO0', 'DO1', 'DO2', 'DO3', 'DO4', 'DO5', 'DO6', 'DO7', 'DO8', 'DO9', 'DO10', 'DO11', 'DO12', 'DO13', 'DO14', 'DO15', 'DO16', 'DO17', 'DO18', 'DO19', 'DO20', 'DO21', 'DO22', 'DO23', 'P72M1DOHx', 'P72M2DOHx', 'P72M3DOHx', 'P72LU2', 'P72MA2', 'P72MI2', 'P72JU2', 'P72VI2', 'P72SA2', 'P72DO2', 'P72NDIAS', 'P72NDIASX', 'P72INILU', 'P72INIMA', 'P72INIMI', 'P72INIJU', 'P72INIVI', 'P72INISA', 'P72INIDO', 'P72PEDLU', 'P72PEDMA', 'P72PEDMI', 'P72PEDJU', 'P72PEDVI', 'P72PEDSA', 'P72PEDDO', 'P72PED', 'P72PEDLUX', 'P72PEDLUY', 'P72PEDMAX', 'P72PEDMAY', 'P72PEDMIX', 'P72PEDMIY', 'P72PEDJUX', 'P72PEDJUY', 'P72PEDVIX', 'P72PEDVIY', 'P72PEDSAX', 'P72PEDSAY', 'P72PEDDOX', 'P72PEDDOY', 'P72PEDX', 'P72PEDY', 'INGPED'])['WPESO']\
        .repeat(df['WPESO'])\
        .reset_index()
df['dependencia'] = df['p65'].astype(int)
df['dependencia'] = df['dependencia'].apply(d)
df1 = df[['edad']]
dfn1 = df['p60a1']
df['p67b'] = df['p67b'].fillna('Mes')
df['periodo'] = df['p67b'].apply(f)

df['periodo'] = df['periodo'].astype(int)
df['p67a'] = df['p67a'].astype(int)
df['mantenimiento'] = df['p67a'] * df['periodo']
df['p66a'] = df['p66a'].astype(int)
df['p66b'] = df['p66b'].astype(int)
df['gastos'] = df['mantenimiento'] + df['p66a'] + df['p66b']
df['ingresom'] = df['p60a1'].apply(x)
df['ingresor'] = df['ingresom'] - df['gastos']
df['categoria'] = df['ingresor'].apply(lambda x: 'minimo' if x < 2250 else 'medio' if x < 4500 else 'alto')
df['years of study'] = df['p4'].apply(years_of_study)
df.rename(columns={'years of study':'educacion'}, inplace=True)
df['jefe'] = df['p8'].apply(jefe)
df['jefe'].value_counts()
df['anterior'] = df['p12']
df['anterior'] = df['anterior'].apply(asalariado)
df['antiguedad'] = df['p27']
df['antiguedad'] = df['antiguedad'].apply(anti)
df['pluriactividad'] = df['p21']
df['pluriactividad'] = df['pluriactividad'].apply(m)
df['razones'] = df['p14']
#Crear un slider de edad
df['razones'] = df['razones'].apply(z)
df['p7'] = df['p7'].fillna(0)
df['menores'] = df['p7'].astype(int)
df['menores'] = df['menores'].apply(t)
df2 = df[['edad', 'razones','pluriactividad', 'antiguedad', 'ingresor', 'categoria', 'educacion', 'jefe','anterior','menores','dependencia']]
df2['edad'] = df2['edad'].astype(int)
df['p12']=df['p12'].cat.add_categories('Primertrabajo').fillna('Primertrabajo')
df['PrimeroTrabajo']=df['p12']
df['PrimeroTrabajo'] = df['PrimeroTrabajo'].apply(a)
df['menores'] = df['menores'].apply(t)
df2 = df[['PrimeroTrabajo','edad', 'razones','pluriactividad', 'antiguedad', 'ingresor', 'categoria', 'educacion', 'jefe','anterior','menores','dependencia','WPESO']]
df2['edad'] = df2['edad'].astype(int)
edad=df2['edad'].unique().tolist()
Primer_Trabajo = df2['PrimeroTrabajo'].unique().tolist()
Genero = df['sexo'].unique().tolist()
calificacion_selector = st.multiselect('Primero Trabajo:',
                                       Primer_Trabajo,
                                       default = Primer_Trabajo)
calificacion_genero = st.multiselect('Genero:',
                                       Genero,
                                       default = Genero)

edad_selector = st.slider("Edad persona encuestada:",
                          min_value = min(edad), #el valor minimo va a ser el valor mas pequeño que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          max_value = max(edad),#el valor maximo va a ser el valor mas grande que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          value = (min(edad),max(edad))) #que tome desde el minimo, hasta el maximo
mask = (df2['edad'].between(*edad_selector))& (df2['PrimeroTrabajo'].isin(calificacion_selector))&(df['sexo'].isin(calificacion_genero))
numero_resultados = df2[mask].shape[0]
st.markdown(f'*Resultados Disponibles:{numero_resultados}*')

df_agrupado = df2[mask].groupby(by=['PrimeroTrabajo']).count()[['edad']] #que me agrupe por CALIFICACION y me cuente por los datos de  EDAD PERSONA ENCUESTADA
df_agrupado =df_agrupado.reset_index()
df_agrupado =df_agrupado.rename(columns={'edad': 'Numero de repartidores'})
df_agrupado =df_agrupado.rename(columns={'PrimeroTrabajo': 'Fuente CEDLA encuesta delivery 2022'})
suma_edades = df_agrupado['Numero de repartidores'].sum( )
df_agrupado['porcentaje'] = ((df_agrupado['Numero de repartidores'] / suma_edades) * 100).round(0).astype(int)
primera_fila = df_agrupado['porcentaje'].iloc[1].copy()
colores_personalizados = ['Primer trabajo', 'Tenia trabajo']

df_agrupado['color'] = colores_personalizados
bar_chart = px.bar(df_agrupado, 
                   x='Fuente CEDLA encuesta delivery 2022',
                   y='porcentaje',
                   text='porcentaje',
                   color='color',
                   color_discrete_map = {'Primer trabajo': '#ff4e50', 'Tenia trabajo': '#fc913a'},
                    #color_discrete_sequence=colores_personalizados,
                   template = 'plotly_white')
mensaje = f"El porcentaje de repartidores que tenían un trabajo antes es **{primera_fila}%**"

st.plotly_chart(bar_chart) #mostrar el grafico de barras en streamlit
st.markdown(mensaje)
###Segunda tabla nivel de estudio 
st.subheader('Nivel de estudios de los delivery') 
edad2=df2['edad'].unique().tolist()
Nivel_Estudio = df['educacion'].unique().tolist()
Pruactividad = df['pluriactividad'].unique().tolist()
Ciudad = df['ciudad'].unique().tolist()

calificacion_Estudio = st.multiselect('Estudio:',
                                       Nivel_Estudio,
                                       default = Nivel_Estudio)
calificacion_Pruactividad = st.multiselect('Pruactividad:',
                                       Pruactividad,
                                       default = Pruactividad)

edad_selector2 = st.slider("Edad persona encuestada (estudios):",
                          min_value = min(edad2), #el valor minimo va a ser el valor mas pequeño que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          max_value = max(edad2),#el valor maximo va a ser el valor mas grande que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          value = (min(edad2),max(edad2))) #que tome desde el minimo, hasta el maximo
calificacion_ciudad = st.multiselect('ciudad:',
                                       Ciudad,
                                       default = Ciudad)

mask2 = (df2['edad'].between(*edad_selector2))& (df['educacion'].isin(calificacion_Estudio))&(df2['pluriactividad'].isin(calificacion_Pruactividad))&(df['ciudad'].isin(calificacion_ciudad))
numero_resultados2 = df[mask2].shape[0]
st.markdown(f'*Resultados Disponibles:{numero_resultados2}*')
df_agrupado2 = df2[mask2].groupby(by=['educacion']).count()[['edad']] #que me agrupe por CALIFICACION y me cuente por los datos de  EDAD PERSONA ENCUESTADA
df_agrupado2 =df_agrupado2.reset_index()
suma_edades2 = df_agrupado2['edad'].sum( )
df_agrupado2 =df_agrupado2.rename(columns={'edad': 'Numero de repartidores'})
df_agrupado2 =df_agrupado2.rename(columns={'educacion': 'Fuente CEDLA encuesta delivery 2022'})
df_agrupado2['porcentaje'] = ((df_agrupado2['Numero de repartidores'] / suma_edades2) * 100).round(0).astype(int)
primera_fila2 = df_agrupado2['porcentaje'].iloc[0].copy()

if len(df_agrupado2) == 1:
    colores_personalizados = ['#ff4e50']  # Longitud 1
else:
    colores_personalizados = ['#ff4e50', '#fc913a']  # Longitud 2

df_agrupado2['color'] = colores_personalizados


bar_chart2 = px.bar(df_agrupado2, 
                   x='Fuente CEDLA encuesta delivery 2022',
                   y='porcentaje',           
                   text='porcentaje',
                   color='color',
                   color_discrete_sequence=colores_personalizados,
                   template = 'plotly_white')
mensaje2 = f"El nivel de estudio que tienen un nivel mas alla de segundario es del  **{primera_fila2}%**"

st.plotly_chart(bar_chart2) #mostrar el grafico de barras en streamlit
st.markdown(mensaje2)
# Ingresos
st.subheader('Nivel de ingresos') 
edad3=df2['edad'].unique().tolist()
Nivel_Ingreso = df2['categoria'].unique().tolist()
Ciudad2 = df['ciudad'].unique().tolist()
calificacion_ingresor = st.multiselect('ingreso:',
                                       Nivel_Ingreso,
                                       default = Nivel_Ingreso)

edad_selector3 = st.slider("Edad persona encuestada segun:",
                          min_value = min(edad3), #el valor minimo va a ser el valor mas pequeño que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          max_value = max(edad3),#el valor maximo va a ser el valor mas grande que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          value = (min(edad3),max(edad3))) #que tome desde el minimo, hasta el maximo
calificacion_ciudad2 = st.multiselect('ciudad2:',
                                       Ciudad2,
                                       default = Ciudad2)
mask3 = (df2['edad'].between(*edad_selector3))& (df2['categoria'].isin(calificacion_ingresor))&(df['ciudad'].isin(calificacion_ciudad2))
numero_resultados3 = df[mask3].shape[0]
st.markdown(f'*Resultados Disponibles:{numero_resultados3}*')
df_agrupado3 = df2[mask3].groupby(by=['categoria']).count()[['edad']] #que me agrupe por CALIFICACION y me cuente por los datos de  EDAD PERSONA ENCUESTADA
df_agrupado3 =df_agrupado3.reset_index()
df_agrupado3 =df_agrupado3.rename(columns={'edad': 'Numero de repartidores'})
df_agrupado3 =df_agrupado3.rename(columns={'categoria': 'Fuente CEDLA encuesta delivery 2022'})
suma_edades3 = df_agrupado3['Numero de repartidores'].sum( )
df_agrupado3['porcentaje'] = ((df_agrupado3['Numero de repartidores'] / suma_edades3) * 100).round(0).astype(int)
primera_fila3 = df_agrupado3['porcentaje'].iloc[0].copy()

if len(df_agrupado3) == 3:
    colores_personalizados = ['#ff4e50', '#fc913a', '#f9d423']
if len(df_agrupado3)==2:
    colores_personalizados = ['#ff4e50', '#fc913a']
if len(df_agrupado3)==1:
    colores_personalizados = ['#ff4e50']

df_agrupado3['color'] = colores_personalizados

# Crea el gráfico de barras y asigna los colores personalizados
bar_chart3 = px.bar(df_agrupado3, 
                   x='Fuente CEDLA encuesta delivery 2022',
                   y='porcentaje',
                   text='porcentaje',
                   color='color',
                   color_discrete_sequence=colores_personalizados,  # Asigna los colores personalizados aquí
                   template='plotly_white')
mensaje3 = f"Minimo hace referencia a que el repartido gana hasta un salario minimo, medio hasta dos salarios minimos y alto gana mas de dos salarios minimos "

st.plotly_chart(bar_chart3) #mostrar el grafico de barras en streamlit
st.markdown(mensaje3)
#  razones para volverse repartidor
df['m'] = df['p20a'].apply(P)
st.subheader('Razones para volverse repartidor') 
edad4=df2['edad'].unique().tolist()
Razon= df['m'].unique().tolist()
Ciudad3 = df['ciudad'].unique().tolist()
calificacion_Razon = st.multiselect('Razones:',
                                       Razon,
                                       default = Razon)

edad_selector4 = st.slider("Edad persona encuestada por razones:",
                          min_value = min(edad4), #el valor minimo va a ser el valor mas pequeño que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          max_value = max(edad4),#el valor maximo va a ser el valor mas grande que encuentre dentro de la columna EDAD PERSONA ENCUESTADA
                          value = (min(edad4),max(edad4))) #que tome desde el minimo, hasta el maximo
calificacion_ciudad3 = st.multiselect('ciudad6:',
                                       Ciudad3,
                                       default = Ciudad3)
mask4 = (df2['edad'].between(*edad_selector3))& (df['m'].isin(calificacion_Razon))&(df['ciudad'].isin(calificacion_ciudad3))
numero_resultados4 = df[mask4].shape[0]
st.markdown(f'*Resultados Disponibles:{numero_resultados4}*')
df_agrupado4 = df[mask4].groupby(by=['m']).count()[['edad']] #que me agrupe por CALIFICACION y me cuente por los datos de  EDAD PERSONA ENCUESTADA
df_agrupado4 =df_agrupado4.reset_index()
suma_edades4 = df_agrupado4['edad'].sum( )
df_agrupado4['porcentaje'] = ((df_agrupado4['edad'] / suma_edades4) * 100).round(0).astype(int)
primera_fila4 = df_agrupado4['porcentaje'].iloc[0].copy()

if len(df_agrupado2) == 1:
    colores_personalizados = ['#ff4e50']  # Longitud 1
else:
    colores_personalizados = ['#ff4e50', '#fc913a']  # Longitud 2

colores_personalizados = ['Era la unica opcion', 'Mayor libertad de horario','Mejor ingreso','Otros']
# colores_personalizados = ['#ff4e50', '#fc913a', '#f9d423','#ede574']
df_agrupado4['color'] = colores_personalizados
df_agrupado4 =df_agrupado4.rename(columns={'m': 'Fuente CEDLA encuesta delivery 2022'})
primera_fila4 = df_agrupado4['porcentaje'].iloc[2].copy()
# Crea el gráfico de barras y asigna los colores personalizados
bar_chart4 = px.bar(df_agrupado4, 
                   x='Fuente CEDLA encuesta delivery 2022',
                   y='porcentaje',
                   text='porcentaje',
                   color='color',
                   color_discrete_map = {'Era la unica opcion': '#ff4e50', 'Mayor libertad de horario': '#fc913a','Mejor ingreso':'#f9d423',
                                         'Otros':'#ede574'},
                   # color_discrete_sequence=colores_personalizados,  # Asigna los colores personalizados aquí
                   template='plotly_white')
mensaje4 = f"La principal razon para que los trabajadores decidieran volverse de delivery es por mejores posibilidades de ingreso  es del **{primera_fila4}%**"
st.plotly_chart(bar_chart4) #mostrar el grafico de barras en streamlit
st.markdown(mensaje4)

if len(df_agrupado2) == 1:
    colores_personalizados = ['#ff4e50']  # Longitud 1
else:
    colores_personalizados = ['#ff4e50', '#fc913a']  # Longitud 2
