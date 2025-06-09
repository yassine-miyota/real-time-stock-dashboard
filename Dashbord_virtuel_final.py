#!/usr/bin/env python
# coding: utf-8

# # VIRTUAL DATABASE CONNECTION

# In[823]:


import pandas as pd
import random
import string
import time
import copy
import uuid
# Global variable to store the accumulated dataset
global_df = pd.DataFrame()

def theoric_dataset ():
    global global_df  # To modify the global DataFrame
    # Générer 100 lignes (articles)
    num_rows = random.randint(50, 100)
    unites = ['ERGAM/GESTION', '1BSMAT/GESTION' , '2BSMAT/GESTION' , '6BSMAT/GESTION', '7BSMAT/GESTION',
             '2ESMAT', '3ESMAT', '4ESMAT', 'ETAM', 'ECGSM/GESTION']

    # Générer des données aléatoires
    nomenclature = [f'NOM-{random.randint(1, 30)}' for _ in range(num_rows)]  # Nomenclature aléatoire (ex: NOM-001, NOM-002,...)
    designation = [f'Article-{random.randint(1, 20)}' for _ in range(num_rows)]  # Désignation (ex: Article-001, Article-002,...)
    quantite_distribuee = [random.randint(1, 500) for _ in range(num_rows)]  # Quantité aléatoire entre 10 et 1000
    prix_unitaire = [random.uniform(100, 1000) for _ in range(num_rows)]  # Prix unitaire aléatoire entre 10 et 1000
    decompte = [random.uniform(100, 1000) for _ in range(num_rows)]  # Prix unitaire aléatoire entre 10 et 1000
    unite_beneficiaire = [random.choice(unites) for _ in range(num_rows)]  # Unités bénéficiaires U1 à U10
    reference_bon_commande = [random.randint(10100, 10140) for _ in range(num_rows)]  # Référence aléatoire

    # Créer le DataFrame
    data = {
        'Nomenclature': nomenclature,
        'Désignation': designation,
        'QUANT_ALLOUEE_NET': quantite_distribuee,
        'DECOMPTE': decompte,
        'CMN': prix_unitaire,
        'UNITE_CLIENT': unite_beneficiaire,
        'N_BM1': reference_bon_commande
    }

    new_df = pd.DataFrame(data)
    # Append to the global DataFrame
    global_df = pd.concat([global_df, new_df], ignore_index=True)

    return global_df


# In[825]:


df = theoric_dataset ()
# df.shape [0]


# In[826]:


from datetime import datetime, timedelta

def nbr_heurs_travail():
    
    # Définir les heures de travail
    heures_jour_semainier = {
        0: 6,  # Lundi
        1: 6,  # Mardi
        2: 6,  # Mercredi
        3: 6,  # Jeudi
        4: 6,  # Vendredi
        5: 4,  # Samedi
        6: 0   # Dimanche (pas de travail)
    }
    
    # Date de début de l'année
    debut_annee = datetime(2024, 1, 1)
    
    # Date du jour
    aujourd_hui = datetime.now()
    
    # Calculer la différence entre les dates
    nb_jours = (aujourd_hui - debut_annee).days + 1  # +1 pour inclure aujourd'hui
    
    # Parcourir chaque jour de l'année et compter les heures de travail
    heures_travail_total = 0
    for i in range(nb_jours):
        jour = debut_annee + timedelta(days=i)
        jour_semaine = jour.weekday()  # Renvoie un nombre de 0 (lundi) à 6 (dimanche)
        heures_travail_total += heures_jour_semainier[jour_semaine]

# Afficher le résultat
    #return f"Nombre total d'heures de travail jusqu'à aujourd'hui : {heures_travail_total} heures"
    return heures_travail_total*60


# In[827]:


#nbr_heurs_travail()


# #DATASET FROM DATABASE

# In[832]:


def kpi_from_dataset (dataset):
    df = dataset
    indices = {'kpi1': 0 , 'kpi2': 0, 'kpi3': 0, 'kpi4': 0, 'kpi5': 0 , 'kpi6': 0, 'kpi7': 0, 'kpi8': 0, 'kpi9': 0, 
               'kpi10': 0, 'kpi11': 0,'kpi12': 0, 'kpi13': 0.0, 'kpi14': 0,'kpi15': 0, 'kpi16': 0, 'kpi17': 0, 'kpi18': 0}
    # Somme des valeurs pour chaque barre
    kpi1 = round(df[df['UNITE_CLIENT']=='ERGAM/GESTION']['QUANT_ALLOUEE_NET'].sum())
    kpi2 = round (df[df['UNITE_CLIENT']=='1BSMAT/GESTION']['QUANT_ALLOUEE_NET'].sum())
    kpi3 = round (df[df['UNITE_CLIENT']=='2BSMAT/GESTION']['QUANT_ALLOUEE_NET'].sum())
    kpi4 = round (df[df['UNITE_CLIENT']=='6BSMAT/GESTION']['QUANT_ALLOUEE_NET'].sum())
    kpi5 = round (df[df['UNITE_CLIENT']=='7BSMAT/GESTION']['QUANT_ALLOUEE_NET'].sum())
    kpi6 = round (df[df['UNITE_CLIENT']=='2ESMAT']['QUANT_ALLOUEE_NET'].sum())
    kpi7 = round (df[df['UNITE_CLIENT']=='3ESMAT']['QUANT_ALLOUEE_NET'].sum())
    kpi8 = round (df[df['UNITE_CLIENT']=='ETAM']['QUANT_ALLOUEE_NET'].sum())
    kpi9 = round (df[df['UNITE_CLIENT']=='4ESMAT']['QUANT_ALLOUEE_NET'].sum())
    kpi10 = round (df[df['UNITE_CLIENT']=='ECGSM/GESTION']['QUANT_ALLOUEE_NET'].sum())
    # calcul de cumul
    indices['kpi1']=kpi1
    indices['kpi2']=kpi2
    indices['kpi3']=kpi3
    indices['kpi4']=kpi4
    indices['kpi5']=kpi5
    indices['kpi6']=kpi6
    indices['kpi7']=kpi7
    indices['kpi8']=kpi8
    indices['kpi9']=kpi9
    indices['kpi10']=kpi10
    
    # Calculer le total des sorties
    indices['kpi11'] = round (indices['kpi1']+indices['kpi2']+indices['kpi3']+indices['kpi4']+indices['kpi5']+
                              indices['kpi6']+indices['kpi7']+indices['kpi8']+indices['kpi9']+indices['kpi10'])
    indices['kpi12'] = df.shape[0]
    indices['kpi13'] = round (df['DECOMPTE'].sum()/1000000,2)
   
    
    #Les indices du graphe circulaire
    indices['kpi14']=indices['kpi1']
    indices['kpi15']=indices['kpi2']+indices['kpi4']+indices['kpi5']
    indices['kpi16']=indices['kpi3']
    indices['kpi17']=indices['kpi6']+indices['kpi7']+indices['kpi8']+indices['kpi9']+indices['kpi10']

    indices['kpi18']= df.shape [0]
    
    return indices


# # LAYOUT

# In[834]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import random
import pandas as pd
import time

# Initialisation de l'application Dash
app = dash.Dash(__name__, external_stylesheets=[
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
])

# Configuration pour éviter la mise en cache (important pour les données en temps réel)
@app.server.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# In[835]:


app.layout = html.Div(className="app-layout", children=[
    html.Button("☰ Menu", id="toggle-menu", className="menu-button", n_clicks=0),

    html.Div([
        html.H4("📥 Inbound :", className="section-header"),
        html.Button("Inbound Dashboard", id="btn-inputs", className="input-button", n_clicks=0),

        html.H4("📤 Distribution :", className="section-header", style={"marginTop": "15px"}),
        html.Button("Distribution Dashboard", id="btn-outputs", className="input-button", n_clicks=0),

        html.H4("🎯 Threshold targets :", className="section-header", style={"marginTop": "15px"}),
        html.Button("Dynamic Target", id="btn-average", className="input-button", n_clicks=0),
        html.Button("Dynamic Minimum", id="btn-min", className="input-button", n_clicks=0)
    ], id="sidebar", style={
        "width": "250px",
        "height": "100vh",
        "padding": "20px",
        "background": "#f0f8f5",
        "borderLeft": "1px solid #ddd",
        "position": "fixed",
        "top": "0",
        "right": "0",
        "zIndex": 9999,
        "transition": "transform 0.3s ease-in-out",
        "transform": "translateX(100%)"
    }),

    html.Div(id="overlay", n_clicks=0, style={
        "position": "fixed",
        "top": "0",
        "left": "0",
        "width": "100vw",
        "height": "100vh",
        "backgroundColor": "rgba(0, 0, 0, 0.3)",
        "zIndex": 9998,
        "display": "none"
    }),

    html.Div(className="container-fluid", children=[
        # Ligne 1 : Logos et Titre
        html.Div(className="row align-items-center", children=[
            html.Div(className="col-2", children=[
                html.Img(src='/assets/logo5.jpeg', className="image-logo")
            ]),
            html.Div(className="col-8 text-center", children=[
                html.H1("REAL-TIME WAREHOUSE FLOW MONITOR", className="title-h1")
            ]),
            html.Div(className="col-2 text-end", children=[
                html.Img(src='/assets/logo5.jpeg', className="image-logo")
            ])
        ]),

        # Ligne 2 : Date/Heure        
        html.Div(className="row mt-2 justify-content-center", children=[
            html.Div(className="col-8", children=[
                dcc.Input(
                    id='current-time',
                    type='text',
                    readOnly=True,
                    className="form-control title-h2",
                    style={"textAlign": "center", "fontSize": "24px" }
                )
            ])
        ]),


        # Ligne 3 : KPIs
        html.Div(className="row text-center", children=[
            html.Div(className="col-4 col-lg-2", children=[
                html.Div(id='total-graph2', className="kpi"),
                html.Button('Total Distributed Items', className="kpi-button")
            ]),
            html.Div(className="col-4 col-lg-2", children=[
                html.Div(id='total-graph4', className="kpi"),
                html.Button('Total Inbound Items', className="kpi-button")
            ]),
            html.Div(className="col-4 col-lg-2", children=[
                html.Div(id='total-graph1', className="kpi"),
                html.Button('Number of Processed Orders', className="kpi-button")
            ]),
            html.Div(className="col-4 col-lg-2", children=[
                html.Div(id='total-graph', className="kpi"),
                html.Button('Average Processing Time', className="kpi-button")
            ]),
            html.Div(className="col-4 col-lg-2", children=[
                html.Div(id='total-graph3', className="kpi"),
                html.Button('Total Distribution Value', className="kpi-button")
            ]),
            html.Div(className="col-4 col-lg-2", children=[
                html.Div(id='total-graph6', className="kpi"),
                html.Button('Total Inbound Value', className="kpi-button")
            ])
        ]),

        # Ligne 4 : Graphiques
        html.Div(className="row mt-3", children=[
            html.Div(className="col-12 col-lg-8", children=[
                html.Div(className="bar-graph", children=[
                    html.Div(style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '3px'}, children=[
                        dcc.DatePickerSingle(
                            id='date-picker',
                            display_format='DD-MM-YYYY',
                            placeholder='Start Date',
                            with_portal=True,
                            className="agenda_styl"
                        ),
                        html.H3(id='bar-title', className="bar_title")
                    ]),
                    dcc.Graph(id='live-graph-bar', animate=True)
                ])
            ]),
            html.Div(className="col-12 col-lg-4", children=[
                html.Div(className="pie-graph", children=[
                    html.H3(id='pie-title', className="bar_title"),
                    dcc.Graph(id='live-pie-chart')
                ])
            ])
        ]),

        dcc.Store(id='graph-state', data='inputs'),
        dcc.Store(id='seuil-state', data='inputs'),
        dcc.Interval(id='graph-update', interval=5000, n_intervals=0),
        dcc.Interval(id='reset-check', interval=1000, n_intervals=0),
    ])
])


# # Sidebar Animation

# In[840]:


from dash.dependencies import Input, Output, State

@app.callback(
    [Output("sidebar", "style"),
     Output("overlay", "style")],
    [Input("toggle-menu", "n_clicks"),
     Input("overlay", "n_clicks")],
    State("sidebar", "style"),
    prevent_initial_call=True
)
def toggle_sidebar(toggle_clicks, overlay_clicks, sidebar_style):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger_id == "toggle-menu":
        if sidebar_style["transform"] == "translateX(0%)":
            return (
                {**sidebar_style, "transform": "translateX(100%)"},
                {"display": "none"}
            )
        else:
            return (
                {**sidebar_style, "transform": "translateX(0%)"},
                {
                    "position": "fixed",
                    "top": "0",
                    "left": "0",
                    "width": "100vw",
                    "height": "100vh",
                    "backgroundColor": "rgba(0, 0, 0, 0.4)",
                    "zIndex": 9998,
                    "display": "block"
                }
            )

    elif trigger_id == "overlay":
        return (
            {**sidebar_style, "transform": "translateX(100%)"},
            {"display": "none"}
        )

    raise dash.exceptions.PreventUpdate


# # Event Button Sidebar Click

# In[843]:


@app.callback(
    Output('graph-state', 'data'),
    [Input('btn-inputs', 'n_clicks'),
     Input('btn-outputs', 'n_clicks')
    ]
)
def update_graph_state(n_inputs, n_outputs):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_id == 'btn-inputs':
        return 'inputs'
    elif triggered_id == 'btn-outputs':
        return 'outputs'
    else:
        return dash.no_update


# In[845]:


@app.callback(
    Output('seuil-state', 'data'),
    [Input('btn-average', 'n_clicks'),
     Input('btn-min', 'n_clicks')
    ]
)
def update_graph_state(n_average, n_min):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    

    if triggered_id == 'btn-average':
        return 'average'
    elif triggered_id == 'btn-min':
        return 'min'
    else:
        return dash.no_update


# # DATE AND TIME

# In[848]:


# Callback pour mettre à jour le titre secondaire avec l'heure et la date en temps réel
@app.callback(
    # Output('current-time', 'children'),
    Output('current-time', 'value'),
    Input('reset-check', 'n_intervals')
)
def update_time(n_intervals):
    # Récupérer l'heure et la date actuelles
    current_time = time.strftime('%d-%m-%Y -- %H:%M:%S')
    return f"Current Date and Time : {current_time}"


# # BAR GRAPH

# In[851]:


import plotly.graph_objects as go
import math
import copy

# ➤ Callback principal pour la mise à jour automatique des graphiques
@app.callback(
    [
        Output('live-graph-bar', 'figure'),
        Output('live-pie-chart', 'figure'),
        Output('total-graph1', 'children'),
        Output('total-graph2', 'children'),
        Output('total-graph3', 'children'),
        Output('total-graph4', 'children'),
        Output('total-graph', 'children'),
        Output('total-graph6', 'children'),
        Output('pie-title', 'children'),
        Output('bar-title', 'children')
    ],
    [
        Input('graph-update', 'n_intervals'),
        Input('graph-state', 'data'),
        Input('seuil-state', 'data')
    ]
)
def update_graph1(n_intervals, graph_state, seuil_state):
    # --- Étape 1 : Récupération des KPI depuis un dataset théorique (peut être remplacé par un dataset réel)
    kpi = kpi_from_dataset(theoric_dataset())
    
    # --- Étape 2 : Préparation des données pour le graphique circulaire
    valeurs1 = [kpi['kpi14'], kpi['kpi15'], kpi['kpi16'], kpi['kpi17']]
    valeurs2 = [kpi['kpi15'], kpi['kpi14'] + kpi['kpi16'], kpi['kpi17'], kpi['kpi16']]

    # Calcul du temps moyen par opération
    kpi_tmps_moyen = round(math.sqrt(nbr_heurs_travail() / kpi['kpi18']), 1)

    # --- Étape 3 : Définition des axes pour les graphes à barres
    y_min, y_max = 0, max(
        kpi['kpi1'], kpi['kpi2'], kpi['kpi3'], kpi['kpi4'], kpi['kpi5'],
        kpi['kpi6'], kpi['kpi7'], kpi['kpi8'], kpi['kpi9'], kpi['kpi10']
    ) + 15000  # Marge ajoutée pour l'affichage

    magasins = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10']
    warehouses = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10']
    values11 = [kpi[f'kpi{i}'] for i in range(1, 11)]
    values12 = [kpi[f'kpi{i}'] for i in [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]]

    # --- Étape 4 : Détermination du seuil en fonction du mode (average ou min)
    seuil_labels = {
        "average": ("Seuil Ciblé", 1, "green"),
        "min": ("Seuil Minimum", 1.1, "red")
    }
    names_test, coef, color_seuil = seuil_labels.get(seuil_state, seuil_labels["average"])

    # Calcul des seuils
    kpi_target11 = round(sum(values11) / (coef * len(values11)), 2)
    kpi_target12 = round(sum(values12) / (coef * len(values12)), 2)

    # Attribution des couleurs conditionnelles
    colors11 = ['red' if val < kpi_target11 else '#43f380' for val in values11]
    colors12 = ['red' if val < kpi_target12 else '#bfa804' for val in values12]

    # --- Étape 5 : Création du 1er graphique à barres (Entrées par Magasin)
    figure11 = go.Figure()
    figure11.add_trace(go.Bar(
        x=magasins, y=values11, text=values11, textposition='outside',
        marker=dict(color=colors11),
        name='Qté entrée',
        textfont=dict(size=14, color='#000', family='Arial Black')
    ))
    figure11.add_trace(go.Scatter(
        x=magasins, y=[kpi_target11] * len(magasins),
        mode='lines', name=names_test,
        line=dict(color=color_seuil, width=2, dash='dash')
    ))
    figure11.update_layout(
        margin=dict(l=25, r=8, t=50, b=30),
        xaxis_title='Warehouses', yaxis_title='Number of Items',
        showlegend=False,
        yaxis=dict(range=[y_min, y_max], fixedrange=False),
        xaxis=dict(fixedrange=False)
    )

    # --- Étape 6 : Création du 2e graphique à barres (Sorties par Warehouse)
    figure12 = go.Figure()
    figure12.add_trace(go.Bar(
        x=warehouses, y=values12, text=values12, textposition='outside',
        marker=dict(color=colors12),
        name='Qté distribuée',
        textfont=dict(size=14, color='#000', family='Arial Black')
    ))
    figure12.add_trace(go.Scatter(
        x=warehouses, y=[kpi_target12] * len(warehouses),
        mode='lines', name=names_test,
        line=dict(color=color_seuil, width=2, dash='dash')
    ))
    figure12.update_layout(
        margin=dict(l=25, r=8, t=50, b=30),
        xaxis_title='Warehouses', yaxis_title='Number of Items',
        showlegend=False,
        yaxis=dict(range=[y_min, y_max], fixedrange=False),
        xaxis=dict(fixedrange=False)
    )

    # --- Étape 7 : Préparation du graphique circulaire (Pie) selon l'état
    if graph_state == "inputs":
        titre1, titre2 = "Inbound per Wharehouse 📥", "Inbound per Supplier 📥"
        figure1 = copy.deepcopy(figure11)
        labels, valeurs = ['S1', 'S2', 'S3', 'S4'], valeurs1
        color_pie = ['#202245', '#9b81ab', '#325f5f', '#0de8a6']
    else:
        titre1, titre2 = "Distribution per Warehouse 📤", "Distribution per Zone 📤"
        figure1 = copy.deepcopy(figure12)
        labels, valeurs = ['Z1', 'Z2', 'Z3', 'Z4'], valeurs2
        color_pie = ['#a1e139', '#dce439', '#656a03', '#f9c741']

    # --- Étape 8 : Création du graphique circulaire (Pie Chart)
    figure2 = go.Figure(
        data=[go.Pie(
            labels=labels,
            values=valeurs,
            hole=0.3,
            textinfo='label+percent',
            hoverinfo='label+value+percent',
            textfont=dict(size=14, family='Arial Black'),
            marker=dict(colors=color_pie, line=dict(color='#ecf9f9', width=2))
        )]
    )
    figure2.update_layout(
        title_x=0.5,
        showlegend=False,
        margin=dict(t=40, b=30, l=20, r=20)
    )

    # --- Étape 9 : Retour des valeurs au tableau de bord
    return (
        figure1, figure2,
        f"{kpi['kpi12']}", f"{kpi['kpi11']}",
        f"{kpi['kpi13']} MDH", f"{kpi['kpi15']}",
        f"{kpi_tmps_moyen} min",
        f"{kpi['kpi13']/2} MDH",
        f"{titre2}", f"{titre1}"
    )


# # RUN

# In[856]:


#Step 7: Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8041)


# In[858]:


# cd C:\Users\yassi\Desktop\install jupyter\dash\Dash_final-2


# In[ ]:


# pour avoir fichier.py


# In[860]:


# jupyter nbconvert --to script Dashbord_Distribution_final_8.ipynb


# In[862]:


#pour le tester
# python Dashbord_Distribution_final_7.py


# In[ ]:


#lancer le ganarateur de l'application (sur dist)


# In[866]:


#pyinstaller --onefile --hidden-import dash --hidden-import flask --hidden-import werkzeug Dashbord_Distribution_final_7.py


# In[864]:


# pyinstaller --onefile --add-data "assets;assets" --hidden-import dash --hidden-import flask --hidden-import werkzeug Dashbord_Distribution_final_12.py


# In[ ]:




