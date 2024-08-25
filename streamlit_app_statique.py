import streamlit as st
import pandas as pd
import plotly.express as px


#DATA_FILENAME_vehicules=r'data\\vehicules.csv'
#DATA_FILENAME_usagers=r'data\\usagers.csv'
#DATA_FILENAME_lieux=r'data\\lieux.csv'
#DATA_FILENAME_caracteristiques=r'data\\carcteristiques.csv'

DATA_FILENAME_vehicules=r'data/vehicules.csv'
DATA_FILENAME_usagers=r'data/usagers.csv'
DATA_FILENAME_lieux=r'data/lieux.csv'
DATA_FILENAME_caracteristiques=r'data/carcteristiques.csv'

df_vehicules = pd.read_csv(DATA_FILENAME_vehicules, sep=';', dtype=str)
df_usagers = pd.read_csv(DATA_FILENAME_usagers , sep=';' , dtype=str)
df_lieux = pd.read_csv(DATA_FILENAME_lieux ,    sep=';' , dtype=str)   
df_caracteristiques = pd.read_csv(DATA_FILENAME_caracteristiques ,    sep=';' , dtype=str)

mapping_trajet = {
    -1: 'Non renseigné',
    0: 'Non renseigné',
    1: 'Domicile – travail',
    2: 'Domicile – école',
    3: 'Courses – achats',
    4: 'Utilisation professionnelle',
    5: 'Promenade – loisirs',
    9: 'Autre'
}


# Créer le nouveau champ 'trajet_lib' en utilisant le dictionnaire de mappage
df_usagers['trajet_lib'] = df_usagers['trajet'].astype(int).map(mapping_trajet)

mapping_sexe = {
    1: 'Masculin',
    2: 'Féminin'
}
# Créer le nouveau champ 'trajet_lib' en utilisant le dictionnaire de mappage
df_usagers['sexe_lib'] = df_usagers['sexe'].astype(int).map(mapping_sexe)
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

mapping_catv = {
    "00": "Indéterminable",
    "01": "Bicyclette",
    "02": "Cyclomoteur <50cm3",
    "03": "Voiturette (Quadricycle à moteur carrossé) (anciennement 'voiturette ou tricycle à moteur')",
    "04": "Référence inutilisée depuis 2006 (scooter immatriculé)",
    "05": "Référence inutilisée depuis 2006 (motocyclette)",
    "06": "Référence inutilisée depuis 2006 (side-car)",
    "07": "VL seul",
    "08": "Référence inutilisée depuis 2006 (VL + caravane)",
    "09": "Référence inutilisée depuis 2006 (VL + remorque)",
    "10": "VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC <= 3,5T)",
    "11": "Référence inutilisée depuis 2006 (VU (10) + caravane)",
    "12": "Référence inutilisée depuis 2006 (VU (10) + remorque)",
    "13": "PL seul 3,5T <PTCA <= 7,5T",
    "14": "PL seul > 7,5T",
    "15": "PL > 3,5T + remorque",
    "16": "Tracteur routier seul",
    "17": "Tracteur routier + semi-remorque",
    "18": "Référence inutilisée depuis 2006 (transport en commun)",
    "19": "Référence inutilisée depuis 2006 (tramway)",
    "20": "Engin spécial",
    "21": "Tracteur agricole",
    "30": "Scooter < 50 cm3",
    "31": "Motocyclette > 50 cm3 et <= 125 cm3",
    "32": "Scooter > 50 cm3 et <= 125 cm3",
    "33": "Motocyclette > 125 cm3",
    "34": "Scooter > 125 cm3",
    "35": "Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)",
    "36": "Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)",
    "37": "Autobus",
    "38": "Autocar",
    "39": "Train",
    "40": "Tramway",
    "41": "3RM <= 50 cm3",
    "42": "3RM > 50 cm3 <= 125 cm3",
    "43": "3RM > 125 cm3",
    "50": "EDP à moteur",
    "60": "EDP sans moteur",
    "80": "VAE",
    "99": "Autre véhicule"
}

df_vehicules['catv_lib'] = df_vehicules['catv'].map(mapping_catv)



mapping_obsm = {
    "-1": "Non renseigné",
    "0": "Aucun",
    "1": "Piéton",
    "2": "Véhicule",
    "4": "Véhicule sur rail",
    "5": "Animal domestique",
    "6": "Animal sauvage",
    "9": "Autre"
}

df_vehicules['obsm_lib'] = df_vehicules['obsm'].map(mapping_obsm)


mapping_mois = {
    "01": "01 - Janvier",
    "02": "02 - Février",
    "03": "03 - Mars",
    "04": "04 - Avril",
    "05": "05 - Mai",
    "06": "06 - Juin",
    "07": "07 - Juillet",
    "08": "08 - Août",
    "09": "09 - Septembre",
    "10": "10 - Octobre",
    "11": "11 - Novembre",
    "12": "12 - Décembre"
}
df_caracteristiques['mois_lib'] = df_caracteristiques['mois'].map(mapping_mois)

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


# accident_par_mois
accident_par_mois_agg = df_caracteristiques['mois_lib'].value_counts().sort_index().reset_index()
accident_par_mois_agg.columns = ['mois_lib', 'count']
accident_par_mois_agg.set_index('mois_lib', inplace=True)


# usager par gravité d'accident
usager_par_gravite_accident= df_usagers[['grav_lib']].astype('str').value_counts().sort_index().reset_index()
usager_par_gravite_accident.columns = ['grav_lib', 'count']
usager_par_gravite_accident.set_index('grav_lib', inplace=True)

# categorie de vehicule impliqué
nombre_accident_par_categorie_vehicule= df_vehicules[['catv_lib']].value_counts().sort_index().reset_index()
nombre_accident_par_categorie_vehicule.columns = ['catv_lib', 'count']
nombre_accident_par_categorie_vehicule.set_index('catv_lib', inplace=True)




# accident par jour
accident_par_date = pd.DataFrame()
accident_par_date['date']  = df_caracteristiques['jour'] + '/' + df_caracteristiques['mois'] +'/' + df_caracteristiques['an']
accident_par_date['date'] = pd.to_datetime(accident_par_date['date']  , dayfirst=True)
accident_par_date_agg = accident_par_date[['date']].value_counts().sort_index().reset_index()
accident_par_date_agg.columns = ['date', 'count']
accident_par_date_agg.set_index('date', inplace=True)




#La répartition des accidents par type de trajet.
accident_par_type_trajet= df_usagers['trajet_lib'].astype('str').value_counts().sort_index().reset_index()
accident_par_type_trajet.columns = ['trajet_lib', 'count']
accident_par_type_trajet.set_index('trajet_lib', inplace=True)


#La répartition des usagers par sexe
accident_par_sexe= df_usagers['sexe_lib'].astype('str').value_counts().sort_index().reset_index()
accident_par_sexe.columns = ['sexe_lib', 'count']
accident_par_sexe.set_index('sexe_lib', inplace=True)


#Le nombre d'accidents par condition atmosphérique
accident_par_cond_atm =  df_caracteristiques['atm_lib'].astype('str').value_counts().sort_index().reset_index()
accident_par_cond_atm.columns = ['atm_lib', 'count']
accident_par_cond_atm.set_index('atm_lib', inplace=True)


# La répartition des obstacles mobiles heurtés (véhicule, piéton, animal, etc).
nombre_accident_par_obsm = df_vehicules[['obsm_lib']].value_counts().sort_index().reset_index()
nombre_accident_par_obsm.columns = ['obsm_lib', 'count']
nombre_accident_par_obsm.set_index('obsm_lib', inplace=True)


# creation du df jointure entre caracteristique et lieux  pour la deuxieme partie : 

df_caracteristiques_s= df_caracteristiques[['Accident_Id' ,'atm_lib' , 'lum_lib'  , 'agg_lib' , 'col_lib' , 'adr' ,'lat', 'long'  ]]
df_lieux_s= df_lieux[['Num_Acc' , 'catr_lib']]
df_caracteristiques_s = df_caracteristiques_s.rename(columns={'Accident_Id': 'Num_Acc'})

df_accident = pd.merge(df_caracteristiques_s, df_lieux_s, on='Num_Acc', how='left')



# stat descriptive

Nombre_accident = df_caracteristiques['Accident_Id'].unique().shape[0]
#Le nombre de véhicules impliqués.
Nombre_vehicule_implique = df_vehicules['id_vehicule'].unique().shape[0]

# Le nombre d'usagers impliqués.
nombre_usager_implique  = df_usagers['id_usager'].unique().shape[0]

# Le nombre de décès.
nombre_usager_decede= df_usagers[df_usagers['grav'] == '2']['id_usager'].unique().shape[0]

# taux de letalité
taux_letalite = (nombre_usager_decede /  Nombre_accident) *100 
taux_letalite_format = "{:.2f}%".format(taux_letalite)
st.title(f'Statistiques accidents en France ')

st.header(f'Quelques chiffres ... ', divider='gray')
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label='Nombre d\'accidents',
        value=f'{Nombre_accident}')

with col2:
    st.metric(
        label='Nombre de véhicules impliqués',
        value=f'{Nombre_vehicule_implique}')

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


st.header(f'Quelques Graphiques ... ', divider='red')
''
st.header('Nombre d\'accidents par mois ')
st.bar_chart(accident_par_mois_agg , x_label='Mois', y_label='Nombre d\'accidents')
''
st.header('Nombre d\'accidents par gravité')
st.bar_chart(usager_par_gravite_accident ,  x_label='Gravité', y_label='Nombre d\'usagers')
''
st.header('Nombre d\'accidents par categorie vehicule')
st.bar_chart(nombre_accident_par_categorie_vehicule ,    x_label='Categorie', y_label='Nombre d\'accidents')

''
st.header('Nombre d\'accidents par date')
st.bar_chart(accident_par_date_agg ,    x_label='Date', y_label='Nombre d\'accidents')
''

fig = px.pie(accident_par_sexe, values='count', names='sexe', title='La répartition des usagers par sexe.')
st.plotly_chart(fig, theme=None)

''
st.header('Nombre d\'accidents par type trajet')

st.bar_chart(accident_par_type_trajet ,    x_label='Type de trajet', y_label='Nombre d\'accidents')


''
st.header('Nombre d\'accidents par conditino atmospherique')
st.bar_chart(accident_par_cond_atm ,    x_label='Conditions atmosphériques', y_label='Nombre d\'accidents')

''
st.header('Nombre d\'accidents sur obstacles mobiles')

st.bar_chart(nombre_accident_par_obsm ,    x_label='Obstacles', y_label='Nombre d\'accidents')

''
