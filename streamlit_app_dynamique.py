import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import pandas as pd
import plotly.express as px
import pandas as pd
import folium
from streamlit_folium import folium_static
import pydeck as pdk


DATA_FILENAME_vehicules=r'c:\\Users\\mouhs\\Desktop\\projet_data_school\\gdp-dashboard\\data\\vehicules.csv'
DATA_FILENAME_usagers=r'c:\\Users\\mouhs\\Desktop\\projet_data_school\\gdp-dashboard\\data\\usagers.csv'
DATA_FILENAME_lieux=r'c:\\Users\\mouhs\\Desktop\\projet_data_school\\gdp-dashboard\\data\\lieux.csv'
DATA_FILENAME_caracteristiques=r'c:\\Users\\mouhs\\Desktop\\projet_data_school\\gdp-dashboard\\data\\carcteristiques.csv'

df_vehicules = pd.read_csv(DATA_FILENAME_vehicules, sep=';', dtype=str)
df_usagers = pd.read_csv(DATA_FILENAME_usagers , sep=';' , dtype=str)
df_lieux = pd.read_csv(DATA_FILENAME_lieux ,    sep=';' , dtype=str)   
df_caracteristiques = pd.read_csv(DATA_FILENAME_caracteristiques ,    sep=';' , dtype=str)


mapping_atm = {
    -1: 'Non renseigné',
    1: 'Normale',
    2: 'Pluie légère',
    3: 'Pluie forte',
    4: 'Neige - grêle',
    5: 'Brouillard - fumée',
    6: 'Vent fort - tempête',
    7: 'Temps éblouissant',
    8: 'Temps couvert',
    9: 'Autre'
}

# Créer le nouveau champ 'trajet_lib' en utilisant le dictionnaire de mappage
df_caracteristiques['atm_lib'] = df_caracteristiques['atm'].astype(int).map(mapping_atm)


mapping_lum = {
    1: 'Plein jour',
    2: 'Crépuscule ou aube',
    3: 'Nuit sans éclairage public',
    4: 'Nuit avec éclairage public non allumé',
    5: 'Nuit avec éclairage public allumé'
}
df_caracteristiques['lum_lib'] = df_caracteristiques['lum'].astype(int).map(mapping_lum)


mapping_agg = {
    1: 'Hors agglomération ',
    2: 'En agglomération '
}
df_caracteristiques['agg_lib'] = df_caracteristiques['agg'].astype(int).map(mapping_agg)



mapping_grav = {
    -1: 'Non renseigné',
    1: 'Indemne',
    2: 'Tué',
    3: 'Blessé hospitalisé',
    4: 'Blessé léger'
}


# Créer le nouveau champ 'trajet_lib'  en utilisant le dictionnaire de mappage
df_usagers['grav_lib'] = df_usagers['grav'].astype(int).map(mapping_grav)

mapping_col = {
    -1: 'Non renseigné',
    1: 'Deux véhicules - frontale',
    2: 'Deux véhicules – par l’arrière',
    3: 'Deux véhicules – par le coté',
    4: 'Trois véhicules et plus – en chaîne',
    5: 'Trois véhicules et plus - collisions multiples',
    6: 'Autre collision',
    7: 'Sans collision'
}

df_caracteristiques['col_lib'] = df_caracteristiques['col'].astype(int).map(mapping_col)




mapping_catr = {
    1: 'Autoroute',
    2: 'Route nationale',
    3: 'Route Départementale',
    4: 'Voie Communales',
    5: 'Hors réseau public',
    6: 'Parc de stationnement ouvert à la circulation publique',
    7: 'Routes de métropole urbaine',
    9: 'autre'
}
df_lieux['catr_lib'] = df_lieux['catr'].astype(int).map(mapping_catr)




# creation du df jointure entre caracteristique et lieux  pour la deuxieme partie : 

df_caracteristiques_s= df_caracteristiques[['Accident_Id' ,'dep', 'atm_lib' , 'lum_lib'  , 'agg_lib' , 'col_lib' , 'adr' ,'lat', 'long'  ]]
df_lieux_s= df_lieux[['Num_Acc' , 'catr_lib']]
df_caracteristiques_s = df_caracteristiques_s.rename(columns={'Accident_Id': 'Num_Acc'})

df_accident = pd.merge(df_caracteristiques_s, df_lieux_s, on='Num_Acc', how='left')


# -----------------------------------------------------------------------------

# Conversion des colonnes lat et long en float
df_accident['lat'] = df_accident['lat'].str.replace(',', '.').astype(float)
df_accident['long'] = df_accident['long'].str.replace(',', '.').astype(float)

# Configuration de la page Streamlit
st.sidebar.header('Filtres')
liste_lav_dep = sorted(df_accident['dep'].unique().tolist()   )
liste_lav_dep.insert(0, 'Tous')

dep = st.sidebar.selectbox('département', liste_lav_dep)

atm_lib = st.sidebar.selectbox('Condition atmosphérique', ['Tous', 'Normale', 'Temps couvert', 'Pluie légère', 'Autre', 'Pluie forte',
       'Brouillard - fumée', 'Temps éblouissant', 'Vent fort - tempête',
       'Neige - grêle', 'Non renseigné'])
lum_lib = st.sidebar.selectbox('Condition de luminosité', ['Tous', 'Plein jour', 'Nuit avec éclairage public allumé',
       'Nuit sans éclairage public', 'Crépuscule ou aube',
       'Nuit avec éclairage public non allumé'])
agg_lib = st.sidebar.selectbox('Agglomération', ['Tous', 'En agglomération ', 'Hors agglomération '])
col_lib = st.sidebar.selectbox('Type de collision', ['Tous', 'Deux véhicules – par le coté', 'Deux véhicules – par l’arrière',
       'Autre collision', 'Deux véhicules - frontale', 'Non renseigné',
       'Trois véhicules et plus – en chaîne', 'Sans collision',
       'Trois véhicules et plus - collisions multiples'])
catr_lib = st.sidebar.selectbox('Type de route', ['Tous', 'Voie Communales', 'Route Départementale', 'Autoroute',
       'Route nationale', 'Hors réseau public',
       'Routes de métropole urbaine', 'autre',
       'Parc de stationnement ouvert à la circulation publique'])

# Filtrage des données
df_accident_filtre = df_accident[
    ((df_accident['dep'] == dep) | (dep == 'Tous')) &
    ((df_accident['atm_lib'] == atm_lib) | (atm_lib == 'Tous')) &
    ((df_accident['lum_lib'] == lum_lib) | (lum_lib == 'Tous')) &
    ((df_accident['agg_lib'] == agg_lib) | (agg_lib == 'Tous')) &
    ((df_accident['col_lib'] == col_lib) | (col_lib == 'Tous')) &
    ((df_accident['catr_lib'] == catr_lib) | (catr_lib == 'Tous'))
]
if df_accident_filtre.empty:
    st.warning('Aucun accident correspondant aux filtres')  
else : 
    # stat descriptive
# stat descriptive

    Nombre_accident = df_accident_filtre['Num_Acc'].unique().shape[0]

    vehicules_filtered = df_vehicules[df_vehicules['Num_Acc'].isin(df_accident_filtre['Num_Acc'])]
    nombre_vehicule_implique = vehicules_filtered['id_vehicule'].nunique()

    usagers_filtered = df_usagers[df_usagers['Num_Acc'].isin(df_accident_filtre['Num_Acc'])]
    nombre_usager_implique = usagers_filtered['id_usager'].nunique()
    # Le nombre de décès.

    nombre_usager_decede_filtre= df_usagers[(df_usagers['Num_Acc'].isin(df_accident_filtre['Num_Acc'])) & (df_usagers['grav'] == '2') ]
    nombre_usager_decede = nombre_usager_decede_filtre['id_usager'].nunique()

    # taux de letalité
    taux_letalite = (nombre_usager_decede /  Nombre_accident) *100 
    taux_letalite_format = "{:.2f}%".format(taux_letalite)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label='Nombre d\'accidents',
            value=f'{Nombre_accident}')

    with col2:
        st.metric(
            label='Nombre de véhicules impliqués',
            value=f'{nombre_vehicule_implique}')

    with col3:
        st.metric(
            label='Nombre d\'usagers impliqués',
            value=f'{nombre_usager_implique}')

    with col4:
        st.metric(
            label='Nombre de décès',
            value=f'{nombre_usager_decede}')

    with col5:
        st.metric(
            label='Taux de létalité',
            value=f'{taux_letalite_format}')


 # Préparer les données pour Mapbox
    data = df_accident_filtre[['lat', 'long']]
    data.columns = ['lat', 'lon']


    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v11',
        initial_view_state=pdk.ViewState(
            latitude=df_accident_filtre['lat'].mean(),
            longitude=df_accident_filtre['long'].mean(),
            zoom=6,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=data,
                get_position='[lon, lat]',
                get_color   ='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
        tooltip={"text": "Latitude: {lat}\nLongitude: {lon}"}
    ))
  