#!/usr/bin/env python
# coding: utf-8

# In[1]:

## Pandas packages
import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from unidecode import unidecode
import math
import joblib


## Visu
def angle_calcul(p1,p2,p3):
    u = (p2[0]-p1[0],p2[1]-p1[1])
    v = (p3[0]-p1[0],p3[1]-p1[1])
    rad = (u[0]*v[0]+u[1]*v[1])/(np.sqrt(u[0]**2+u[1]**2)*np.sqrt(v[0]**2+v[1]**2))
    return math.degrees(math.acos(rad))

def time_out_in(playerId,list):
    for i in range(len(list)):
        if (playerId == list[i]['playerOut'] or playerId == list[i]['playerIn']):
            return list[i]['minute']
    else:
        return np.nan

def remove_accents(x):
    return unidecode(str(x).encode('utf-8').decode('unicode escape'))

def plot_pitch(fig):
    try:
        for row_idx, row_figs in enumerate(fig._grid_ref):

            for col_idx, col_fig in enumerate(row_figs):
                #field
                
                fig.add_shape(type="rect",
                    xref="x", yref="y",
                    x0=-52.5, y0=-34, x1=52.5, y1=34,
                    line_color="white",
                    fillcolor='#3B782F',
                    opacity=0.3,
                    row=row_idx+1, col=col_idx+1
                    )
                
                #middle round
                fig.add_shape(type="circle",
                    xref="x", yref="y",
                    x0=-9.15, y0=-9.15, x1=9.15, y1=9.15,
                    line_color="white",
                    row=row_idx+1, col=col_idx+1
                    )
                #middle line
                fig.add_shape(type="line",
                    xref="x", yref="y",
                    x0=0, y0=-34, x1=0, y1=34,
                    line_color="white",
                    row=row_idx+1, col=col_idx+1
                    )
                #surface de réparation
                fig.add_shape(type="rect",
                    xref="x", yref="y",
                    x0=-52.5, y0=-34+13.85, x1=-52.5+16.5, y1=34-13.85,
                    line_color="white",
                    #fillcolor='#3B782F',
                    #opacity=0.2,
                    row=row_idx+1, col=col_idx+1
                    )
                fig.add_shape(type="rect",
                    xref="x", yref="y",
                    x0=52.5, y0=-34+13.85, x1=52.5-16.5, y1=34-13.85,
                    line_color="white",
                    #fillcolor='#3B782F',
                    #opacity=0.2,
                    row=row_idx+1, col=col_idx+1
                    )

                fig.add_shape(type="rect",
                    xref="x", yref="y",
                    x0=-52.5, y0=-34+24.85, x1=-52.5+5.5, y1=34-24.85,
                    line_color="white",
                    #fillcolor='#3B782F',
                    #opacity=0.2,
                    row=row_idx+1, col=col_idx+1
                    )
                fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=52.5, y0=-34+24.85, x1=52.5-5.5, y1=34-24.85,
                      line_color="white",
                      #fillcolor='#3B782F',
                      #opacity=0.2,
                      row=row_idx+1, col=col_idx+1
                      )
                #goals
                fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=52.5, y0=-34+30.35, x1=52.5+2.44, y1=34-30.35,
                      line_color="white",
                      #fillcolor='#3B782F',
                      #opacity=0.2,
                      row=row_idx+1, col=col_idx+1
                      )
                fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=-52.5-2.44, y0=-34+30.35, x1=-52.5, y1=34-30.35,
                      line_color="white",
                      #fillcolor='#3B782F',
                      #opacity=0.2,
                      row=row_idx+1, col=col_idx+1
                      )
                #penalty
                fig.add_shape(type="circle",
                        xref="x", yref="y",
                        x0=-52.5+11.1, y0=-0.1, x1=-52.5+10.9, y1=0.1,
                        fillcolor='white',
                        line_color='white',
                        row=row_idx+1, col=col_idx+1
                        )
                fig.add_shape(type="circle",
                        xref="x", yref="y",
                        x0=52.5-11.1, y0=-0.1, x1=52.5-10.9, y1=0.1,
                        fillcolor='white',
                        line_color='white',
                        row=row_idx+1, col=col_idx+1
                        )
                #corner points
                fig.add_shape(type="path",
                            path="M 51.5,34 Q 51.5,33 52.5,33",
                            line_color="white",
                             row=row_idx+1, col=col_idx+1)
                fig.add_shape(type="path",
                            path="M 51.5,-34 Q 51.5,-33 52.5,-33",
                            line_color="white",
                             row=row_idx+1, col=col_idx+1)
                fig.add_shape(type="path",
                            path="M -51.5,34 Q -51.5,33 -52.5,33",
                            line_color="white",
                             row=row_idx+1, col=col_idx+1)
                fig.add_shape(type="path",
                            path="M -51.5,-34 Q -51.5,-33 -52.5,-33",
                            line_color="white",
                             row=row_idx+1, col=col_idx+1)
                fig.add_shape(type="path",
                            path="M -36,-6.9 Q -32.35,0 -36,6.9",
                            line_color="white",
                             row=row_idx+1, col=col_idx+1)
                fig.add_shape(type="path",
                            path="M 36,-6.9 Q 32.35,0 36,6.9",
                            line_color="white",
                             row=row_idx+1, col=col_idx+1)
    except:
        #field
        fig.add_shape(type="rect",
            xref="x", yref="y",
            x0=-52.5, y0=-34, x1=52.5, y1=34,
            line_color="white",
            fillcolor='#3B782F',
            opacity=0.3,
            
            )
        #middle round
        fig.add_shape(type="circle",
            xref="x", yref="y",
            x0=-9.15, y0=-9.15, x1=9.15, y1=9.15,
            line_color="white",
                    
            )
        #middle line
        fig.add_shape(type="line",
            xref="x", yref="y",
            x0=0, y0=-34, x1=0, y1=34,
            line_color="white",
            
            )
        #surface de réparation
        fig.add_shape(type="rect",
            xref="x", yref="y",
            x0=-52.5, y0=-34+13.85, x1=-52.5+16.5, y1=34-13.85,
            line_color="white",
            #fillcolor='#3B782F',
            #opacity=0.2,
            
            )
        fig.add_shape(type="rect",
            xref="x", yref="y",
            x0=52.5, y0=-34+13.85, x1=52.5-16.5, y1=34-13.85,
            line_color="white",
            #fillcolor='#3B782F',
            #opacity=0.2,
            
            )

        fig.add_shape(type="rect",
            xref="x", yref="y",
            x0=-52.5, y0=-34+24.85, x1=-52.5+5.5, y1=34-24.85,
            line_color="white",
            #fillcolor='#3B782F',
            #opacity=0.2,
            
            )
        fig.add_shape(type="rect",
              xref="x", yref="y",
              x0=52.5, y0=-34+24.85, x1=52.5-5.5, y1=34-24.85,
              line_color="white",
              #fillcolor='#3B782F',
              #opacity=0.2,
              
              )
        #goals
        fig.add_shape(type="rect",
              xref="x", yref="y",
              x0=52.5, y0=-34+30.35, x1=52.5+2.44, y1=34-30.35,
              line_color="white",
              #fillcolor='#3B782F',
              #opacity=0.2,
              
              )
        fig.add_shape(type="rect",
              xref="x", yref="y",
              x0=-52.5-2.44, y0=-34+30.35, x1=-52.5, y1=34-30.35,
              line_color="white",
              #fillcolor='#3B782F',
              #opacity=0.2,
              
              )
        #penalty
        fig.add_shape(type="circle",
                xref="x", yref="y",
                x0=-52.5+11.1, y0=-0.1, x1=-52.5+10.9, y1=0.1,
                fillcolor='white',
                line_color='white',
                
                )
        fig.add_shape(type="circle",
                xref="x", yref="y",
                x0=52.5-11.1, y0=-0.1, x1=52.5-10.9, y1=0.1,
                fillcolor='white',
                line_color='white',
                
                )
        #corner points
        fig.add_shape(type="path",
                    path="M 51.5,34 Q 51.5,33 52.5,33",
                    line_color="white",
                      
                     )
        fig.add_shape(type="path",
                    path="M 51.5,-34 Q 51.5,-33 52.5,-33",
                    line_color="white",
                     
                     )
        fig.add_shape(type="path",
                    path="M -51.5,34 Q -51.5,33 -52.5,33",
                    line_color="white",
                     
                     )
        fig.add_shape(type="path",
                    path="M -51.5,-34 Q -51.5,-33 -52.5,-33",
                    line_color="white",
                     
                     )
        fig.add_shape(type="path",
                    path="M -36,-6.9 Q -32.35,0 -36,6.9",
                    line_color="white",
                     
                     )
        fig.add_shape(type="path",
                    path="M 36,-6.9 Q 32.35,0 36,6.9",
                    line_color="white",
                     
                     )

    fig.update_yaxes(matches=None, showticklabels=False)
    fig.update_xaxes(matches=None, showticklabels=False)
    try :
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    except:
        pass
    
    
    return fig
    

def get_match_infos(matches,match_id,teams_id_name,teams_name_id,players,events,tags_id_name):
    match_test = matches[matches['wyId']==match_id]
    left_team = teams_id_name[int(list(match_test['teamsData'].iloc[0].keys())[0])]
    right_team = teams_id_name[int(list(match_test['teamsData'].iloc[0].keys())[1])]
    match_test['home_team'] = match_test['label'].apply(lambda x:x.split(',')[0].split('-')[0]).str.strip()
    match_test['home_team_score'] = match_test['label'].apply(lambda x:x.split(',')[1].split('-')[0])
    match_test['away_team'] = match_test['label'].apply(lambda x:x.split(',')[0].split('-')[1]).str.strip()
    titulars = [dico['playerId'] for dico in match_test['teamsData'].iloc[0][list(match_test['teamsData'].iloc[0].keys())[0]]['formation']['lineup'] + match_test['teamsData'].iloc[0][list(match_test['teamsData'].iloc[0].keys())[1]]['formation']['lineup']]
    substitutions = match_test['teamsData'].iloc[0][list(match_test['teamsData'].iloc[0].keys())[0]]['formation']['substitutions'] + match_test['teamsData'].iloc[0][list(match_test['teamsData'].iloc[0].keys())[1]]['formation']['substitutions']
    
    match_test['away_team_score']= match_test['label'].apply(lambda x:x.split(',')[1].split('-')[1])
    match_test['winner'] = match_test['winner'].apply(lambda team:teams_id_name[team])
    temp_players = pd.concat([pd.concat([pd.DataFrame(match_test['teamsData'].iloc[0][str(teams_name_id[team])]['formation']['lineup']),
           pd.DataFrame(match_test['teamsData'].iloc[0][str(teams_name_id[team])]['formation']['bench'])])\
                     for team in [left_team,right_team]]
         ).reset_index(drop=True)
    temp_players_bis = players.query(f"wyId=={temp_players['playerId'].unique().tolist()}")[['wyId','shortName','weight',
                                                                      'height',
                                                                      'role','foot',
                                                                     ]]
    temp_players_bis['shortName'] = temp_players_bis['shortName'].apply(remove_accents)
    players_stats = pd.merge(temp_players_bis,temp_players,left_on='wyId',right_on='playerId').drop('wyId',axis=1)
    players_stats['role'] = players_stats['role'].apply(lambda role:role['code3'])

    match_events = events[events['matchId']==match_id]
    df_events = match_events.drop(['id'],axis=1)
    df_events['tags_name'] = df_events['tags'].apply(lambda x:[tags_id_name[o['id']] for o in x])
    df_events['outcome'] = df_events['tags_name'].apply(lambda liste:'accurate' if 'accurate' in liste else 'not_accurate' if 'not accurate' in liste else np.nan)
    df_events.loc[df_events['outcome'].isnull(),'result'] = df_events.loc[df_events['outcome'].isnull(),'tags_name'].apply(lambda x:'Goal' if 'Goal' in x else 'opportunity' if 'opportunity' in x else '')
    df_events.loc[df_events['outcome'].notnull(),'result'] = df_events.loc[df_events['outcome'].notnull(),'tags_name'].apply(lambda x:'Goal' if 'Goal' in x else 'opportunity' if 'opportunity' in x else '')
    
    df_events.loc[df_events['result']=='Goal','tag'] = df_events.loc[df_events['result']=='Goal','tags_name'].apply(lambda x:str(x[1]).lower() if len(x)>1  else '')
    df_events.loc[df_events['result']=='opportunity','tag'] = df_events.loc[df_events['result']=='opportunity','tags_name'].apply(lambda x:str(x[0]).lower() if len(x)>0  else '')
    df_events.loc[(df_events['result']!='Goal')&(df_events['result']!='opportunity'),'tag'] = df_events.loc[(df_events['result']!='Goal')&(df_events['result']!='opportunity'),'tags_name'].apply(lambda x:x[0] if len(x)>0  else '')
    
    
    #df_events.loc[df_events['outcome'].notnull(),'tag'] = df_events.loc[df_events['outcome'].notnull(),'tags_name'].apply(lambda x:x[0] if len(x)>1 else '')
    
    df_events['team'] = df_events['teamId'].apply(lambda idx:teams_id_name[idx])

    match_stats =  pd.merge(df_events,players_stats,left_on='playerId',right_on='playerId')
    match_stats['winner'] = match_stats['team'].apply(lambda x: 1 if match_test['winner'].values[0]==x else 0)
    match_stats.loc[match_stats['tag']==match_stats['foot'],'good_foot'] = 'Yes'
    match_stats.loc[match_stats['tag']!=match_stats['foot'],'good_foot'] = 'No'
    ### Temps sur 90 minutes
    match_stats.loc[match_stats['matchPeriod']=='1H','time'] = match_stats.loc[match_stats['matchPeriod']=='1H','eventSec'].apply(lambda x: pd.Timestamp(round(x),unit="s").time())
    match_stats.loc[match_stats['matchPeriod']=='2H','time'] = match_stats.loc[match_stats['matchPeriod']=='2H','eventSec'].apply(lambda x: pd.Timestamp(45*60+round(x),unit="s").time())
    match_stats['positions'] = match_stats['positions'].apply(lambda liste : [dico for dico in liste if (list(dico.values())!=[0,0]) & (list(dico.values())!=[100,100]) ])

    ### Remettre de la bonne manière les coordonnées
    match_stats.loc[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='1H'),'x'] = \
    match_stats[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='1H')]['positions'].\
    apply(lambda x:(x[0]['x'])*105/100-52.5 if len(x)!=0 else np.nan)

    match_stats.loc[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='1H'),'y'] = \
    match_stats[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='1H')]['positions'].\
    apply(lambda x:(100-x[0]['y'])*68/100-34 if len(x)!=0 else np.nan)

    match_stats.loc[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='1H'),'x'] = \
    match_stats[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='1H')]['positions'].\
    apply(lambda x:(100-x[0]['x'])*105/100-52.5 if len(x)!=0 else np.nan)

    match_stats.loc[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='1H'),'y'] = \
    match_stats[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='1H')]['positions'].\
    apply(lambda x:(x[0]['y'])*68/100-34 if len(x)!=0 else np.nan)

    match_stats.loc[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='2H'),'x'] = \
    match_stats[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='2H')]['positions'].\
    apply(lambda x:(100-x[0]['x'])*105/100-52.5 if len(x)!=0 else np.nan)

    match_stats.loc[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='2H'),'y'] = \
    match_stats[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='2H')]['positions'].\
    apply(lambda x:(x[0]['y'])*68/100-34 if len(x)!=0 else np.nan)

    match_stats.loc[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='2H'),'x'] = \
    match_stats[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='2H')]['positions'].\
    apply(lambda x:(x[0]['x'])*105/100-52.5 if len(x)!=0 else np.nan)

    match_stats.loc[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='2H'),'y'] = \
    match_stats[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='2H')]['positions'].\
    apply(lambda x:(100-x[0]['y'])*68/100-34 if len(x)!=0 else np.nan)
    
    ###
    match_stats.loc[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='1H'),'x_to'] = \
    match_stats[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='1H')]['positions'].\
    apply(lambda x:(x[1]['x'])*105/100-52.5 if len(x)>1 else np.nan)

    match_stats.loc[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='1H'),'y_to'] = \
    match_stats[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='1H')]['positions'].\
    apply(lambda x:(100-x[1]['y'])*68/100-34 if len(x)>1 else np.nan)

    match_stats.loc[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='1H'),'x_to'] = \
    match_stats[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='1H')]['positions'].\
    apply(lambda x:(100-x[1]['x'])*105/100-52.5 if len(x)>1 else np.nan)

    match_stats.loc[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='1H'),'y_to'] = \
    match_stats[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='1H')]['positions'].\
    apply(lambda x:(x[1]['y'])*68/100-34 if len(x)>1 else np.nan)

    match_stats.loc[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='2H'),'x_to'] = \
    match_stats[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='2H')]['positions'].\
    apply(lambda x:(100-x[1]['x'])*105/100-52.5 if len(x)>1 else np.nan)

    match_stats.loc[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='2H'),'y_to'] = \
    match_stats[(match_stats['team']==left_team)&(match_stats['matchPeriod']=='2H')]['positions'].\
    apply(lambda x:(x[1]['y'])*68/100-34 if len(x)>1 else np.nan)

    match_stats.loc[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='2H'),'x_to'] = \
    match_stats[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='2H')]['positions'].\
    apply(lambda x:(x[1]['x'])*105/100-52.5 if len(x)>1 else np.nan)

    match_stats.loc[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='2H'),'y_to'] = \
    match_stats[(match_stats['team']==right_team)&(match_stats['matchPeriod']=='2H')]['positions'].\
    apply(lambda x:(100-x[1]['y'])*68/100-34 if len(x)>1 else np.nan)

    match_stats['x'] = match_stats['x'].round()
    match_stats['y'] = match_stats['y'].round()
    match_stats['x_to'] = match_stats['x_to'].round()
    match_stats['y_to'] = match_stats['y_to'].round()
    
    #### Délimiter attaque milieu défense
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team) & (match_stats['x']<=-22),"zone_from"] = 'defence'
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team) & (match_stats['x']>=22),"zone_from"] = 'attack'
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team) & (match_stats['x']<22) & (match_stats['x']>-22),"zone_from"] = 'middle'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team) & (match_stats['x']>=22),"zone_from"] = 'defence'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team) & (match_stats['x']<=-22),"zone_from"] = 'attack'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team) & (match_stats['x']>-22) & (match_stats['x']<22),"zone_from"] = 'middle'
    
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team) & (match_stats['x']>=22),"zone_from"] = 'defence'
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team) & (match_stats['x']<=-22),"zone_from"] = 'attack'
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team) & (match_stats['x']<22) & (match_stats['x']>-22),"zone_from"] = 'middle'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team) & (match_stats['x']<=-22),"zone_from"] = 'defence'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team) & (match_stats['x']>=22),"zone_from"] = 'attack'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team) & (match_stats['x']<22) & (match_stats['x']>-22),"zone_from"] = 'middle'
    
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team) & (match_stats['x_to']<=-22),"zone_to"] = 'defence'
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team) & (match_stats['x_to']>=22),"zone_to"] = 'attack'
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team) & (match_stats['x_to']<22) & (match_stats['x_to']>-22),"zone_to"] = 'middle'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team) & (match_stats['x_to']>=22),"zone_to"] = 'defence'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team) & (match_stats['x_to']<=-22),"zone_to"] = 'attack'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team) & (match_stats['x_to']>-22) & (match_stats['x_to']<22),"zone_to"] = 'middle'
    
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team) & (match_stats['x_to']>=22),"zone_to"] = 'defence'
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team) & (match_stats['x_to']<=-22),"zone_to"] = 'attack'
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team) & (match_stats['x_to']<22) & (match_stats['x_to']>-22),"zone_to"] = 'middle'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team) & (match_stats['x_to']<=-22),"zone_to"] = 'defence'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team) & (match_stats['x_to']>=22),"zone_to"] = 'attack'
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team) & (match_stats['x_to']<22) & (match_stats['x_to']>-22),"zone_to"] = 'middle'
    
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),"distance_to_goal_from"] =\
    np.sqrt((52.5-match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),"x"])**2 + (0-match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),"y"])**2)
    
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),"distance_to_goal_from"] =\
    np.sqrt((-52.5-match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),"x"])**2 + (0-match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),"y"])**2)
    
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),"distance_to_goal_from"] =\
    np.sqrt((-52.5-match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),"x"])**2 + (0-match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),"y"])**2)
    
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),"distance_to_goal_from"] =\
    np.sqrt((52.5-match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),"x"])**2 + (0-match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),"y"])**2)
   
    match_stats["distance_to_goal_from"] = match_stats["distance_to_goal_from"].round()
    
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),"distance_to_goal_to"] =\
    np.sqrt((52.5-match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),"x_to"])**2 + (0-match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),"y_to"])**2)

    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),"distance_to_goal_to"] =\
    np.sqrt((-52.5-match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),"x_to"])**2 + (0-match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),"y_to"])**2)

    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),"distance_to_goal_to"] =\
    np.sqrt((-52.5-match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),"x_to"])**2 + (0-match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),"y_to"])**2)

    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),"distance_to_goal_to"] =\
    np.sqrt((52.5-match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),"x_to"])**2 + (0-match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),"y_to"])**2)
    
    match_stats["distance_to_goal_to"] = match_stats["distance_to_goal_to"].round()
    
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),"angle_from"] =\
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),'positions'].\
    apply(lambda x:angle_calcul(((x[0]['x'])*105/100-52.5,(100-x[0]['y'])*68/100-34),(52.5,3.65),(52.5,-3.65)) if len(x)!=0 else np.nan)

    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),"angle_from"] =\
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),'positions'].\
    apply(lambda x:angle_calcul(((100-x[0]['x'])*105/100-52.5,(x[0]['y'])*68/100-34),(-52.5,3.65),(-52.5,-3.65)) if len(x)!=0 else np.nan)

    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),"angle_from"] =\
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),'positions'].\
    apply(lambda x:angle_calcul(((100-x[0]['x'])*105/100-52.5,(x[0]['y'])*68/100-34),(-52.5,3.65),(-52.5,-3.65)) if len(x)!=0 else np.nan)
    
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),"angle_from"] =\
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),'positions'].\
    apply(lambda x:angle_calcul(((x[0]['x'])*105/100-52.5,(100-x[0]['y'])*68/100-34),(52.5,3.65),(52.5,-3.65)) if len(x)!=0 else np.nan)
    
    match_stats["angle_from"] = match_stats["angle_from"].round()
    
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),"angle_to"] =\
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==left_team),'positions'].\
    apply(lambda x:angle_calcul(((x[1]['x'])*105/100-52.5,(100-x[1]['y'])*68/100-34),(52.5,3.65),(52.5,-3.65)) if len(x)>1 else np.nan)

    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),"angle_to"] =\
    match_stats.loc[(match_stats['matchPeriod']=='1H') & (match_stats['team']==right_team),'positions'].\
    apply(lambda x:angle_calcul(((100-x[1]['x'])*105/100-52.5,(x[1]['y'])*68/100-34),(-52.5,3.65),(-52.5,-3.65)) if len(x)>1 else np.nan)

    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),"angle_to"] =\
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==left_team),'positions'].\
    apply(lambda x:angle_calcul(((100-x[1]['x'])*105/100-52.5,(x[1]['y'])*68/100-34),(-52.5,3.65),(-52.5,-3.65)) if len(x)>1 else np.nan)
    
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),"angle_to"] =\
    match_stats.loc[(match_stats['matchPeriod']=='2H') & (match_stats['team']==right_team),'positions'].\
    apply(lambda x:angle_calcul(((x[1]['x'])*105/100-52.5,(100-x[1]['y'])*68/100-34),(52.5,3.65),(52.5,-3.65)) if len(x)>1 else np.nan)
    
    match_stats["angle_to"] = match_stats["angle_to"].round()
    match_stats['eventSec'] = match_stats['eventSec'].round()
    #match_stats['total_sec'] = match_stats['matchPeriod'].apply(lambda x:int(x[0])-1 if (x=='1H' or x=='2H') else 0)*45*60 + match_stats['eventSec']
    match_stats['titular'] = match_stats['playerId'].apply(lambda x: 'titular' if x in titulars else 'substitute')
    match_stats['color'] = match_stats['team'].apply(lambda x:'darkred' if x=='Liverpool' else 'slategrey')
    
    return match_test,match_stats.sort_values(by=['time']).reset_index(drop=True)
    
def remove_accents(x):
    return unidecode(str(x).encode().decode('unicode_escape'))

@st.cache(persist=True,suppress_st_warning=True)
def get_data(league):

    if league == 'Premier League':
        matches = pd.read_csv('https://raw.githubusercontent.com/jmaignier/wyscout_data/data/liv_matches.csv',index_col=0)
        events = pd.read_csv('https://raw.githubusercontent.com/jmaignier/wyscout_data/data/liv_events.csv',index_col=0)
    
        
    tags = pd.read_csv('/https://raw.githubusercontent.com/jmaignier/wyscout_data/data/tags2name.csv')
    tags_id_name = tags[['Tag','Label']].set_index('Tag').to_dict()['Label']
    teams = pd.read_json('https://raw.githubusercontent.com/jmaignier/wyscout_data/data/teams.json')
    players=pd.read_json('https://raw.githubusercontent.com/jmaignier/wyscout_data/data/players.json')
    teams['area'] = teams['area'].apply(lambda dico:dico['name'])
    teams['name'] = teams['name'].apply(lambda name : remove_accents(name))
    teams_id_name = teams[['wyId','name']].set_index('wyId').to_dict()['name']
    teams_id_name.update({0:'Nul'})
    teams_name_id = teams[['wyId','name']].set_index('name').to_dict()['wyId']
    teams_name_id.update({'Nul':0})
    liv_matches = matches[matches['label'].str.contains('Liverpool')]
    #st.write(liv_matches['wyId'].unique())
    #st.write(events['matchId'].unique())
    liv_events = events.query(f"matchId=={liv_matches['wyId'].unique().tolist()}")
    
    return liv_matches,liv_events,tags_id_name,teams_id_name,teams_name_id,players


def quantile(x):
    return np.quantile(x,0.4)
    
def str_to_time(string):
    time = string.split('.')[0]
    hours = int(time.split(':')[0])//60
    minutes = int(time.split(':')[0])%60
    seconds = int(time.split(':')[1])
    return pd.Timestamp(hours*3600+minutes*60+seconds,unit="s").time()


def dist_running(df):
    positions = df[['x','y']].diff(1).apply(lambda x:x**2)
    return round(((positions['x']+positions['y']).apply(lambda x:np.sqrt(x)).sum())*1e-3,2)
#######################

def plot_events_scatter(match_info,match_events,teams_id_name,match_id,event_name, sub_event_name , tags,outcomes,player=None):
    left_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[0])]
    right_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[1])]
    event = match_events[match_events['eventName']==event_name]
    if 'ALL' not in sub_event_name:
        event = event.query(f"subEventName=={sub_event_name}")
    if 'ALL' not in tags:
        event = event.query(f"tag=={tags}")
    if player:
        event = event.query(f"shortName=={[player]}")
    if 'BOTH' not in outcomes:
        event = event.query(f"outcome=={outcomes}")
    
    fig = px.scatter(event,
                     x='x',y='y',
                     range_x=[[-55,55],[-55,55]],
                     range_y=[[-35,35],[-35,35]],
                     color='team',
                     symbol='subEventName',
                     facet_col='matchPeriod',
                     facet_row='team',
                     size='distance_to_goal_from',
                     #animation_frame=event["time"].astype('str'),
                     #animation_group="teamId",
                     #size_max=22,
                     custom_data=['subEventName', 'shortName', 'tag','time','distance_to_goal_from','angle_from','outcome'],
                     labels={'team':'team',
                             'subEventName':'sub event'
                            },
                     category_orders={'matchPeriod':['1H','2H'],
                                  'team':[left_team,right_team],
                                  #'eventSec':match_events['eventSec'].tolist(),
                                 },
                     template='plotly_dark',
                     height=500,
                     width=900,
                     title=f"<span style='text-decoration:underline'>(L) {left_team} - {right_team} (R)</span>"
                     )
    #fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2500
    fig.update_traces(hovertemplate=" %{customdata[0]} by %{customdata[1]} (%{customdata[2]} %{customdata[6]}) at %{customdata[3]} <br> %{customdata[4]}m  %{customdata[5]}° ",)
    fig.update_layout(title=dict(x=0.3),)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return plot_pitch(fig),event

############
def plot_events_density(match_info,match_events,teams_id_name,match_id,event_name, sub_event_name , tags,outcomes,player=None):
    left_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[0])]
    right_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[1])]
    event = match_events[match_events['eventName']==event_name]
    if 'ALL' not in sub_event_name:
        event = event.query(f"subEventName=={sub_event_name}")
    if 'ALL' not in tags:
        event = event.query(f"tag=={tags}")
    if player:
        event = event.query(f"shortName=={[player]}")
    if 'BOTH' not in outcomes:
        event = event.query(f"outcome=={outcomes}")
        
    fig = px.density_contour(event,
                     x='x',y='y',
                     range_x=[[-55,55],[-55,55]],
                     range_y=[[-35,35],[-35,35]],
                     marginal_x='histogram',
                     #color='teamId',
                     #symbol='subEventName',
                     facet_col='matchPeriod',
                     facet_row='team',
                     #size='eventSec',
                     #size_max=22,
                     #custom_data=['subEventName', 'shortName', 'tags','time'],
                     
                     category_orders={'matchPeriod':['1H','2H'],
                                  'team':[left_team,right_team]
                                 },
                     template='plotly_dark',
                     height=800,
                     width=1100,
                     title=f"<span style='text-decoration:underline'>(L) {left_team} - {right_team} (R)</span>"
                     )
    fig.update_traces(contours_coloring="fill", contours_showlabels = False,showscale=False,colorscale='Inferno')
    fig.update_layout(title=dict(x=0.3),plot_bgcolor='black')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return plot_pitch(fig),event
    
def plot_animated_scatter(match_info,match_events,teams_id_name,match_id,event_name, sub_event_name , tags,start_time,end_time):
    left_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[0])]
    right_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[1])]
    event = match_events.loc[(match_events['time']>=start_time) & (match_events['time']<=end_time)]
    if 'ALL' not in sub_event_name:
        event = event.query(f"subEventName=={sub_event_name}")
    if 'ALL' not in tags:
        event = event.query(f"tag=={tags}")
    
    fig = px.scatter(event,
                     x='x',y='y',
                     range_x=[[-55,55],[-55,55]],
                     range_y=[[-35,35],[-35,35]],
                     #color='teamId',
                     #symbol='subEventName',
                     #facet_col='matchPeriod',
                     #facet_row='teamId',
                     #size='distance_to_goal_from',
                     animation_frame=event["time"].astype('str'),
                     animation_group="team",
                     custom_data=['subEventName', 'shortName', 'tag','time','distance_to_goal_from','angle_from'],
                     
                     category_orders={'matchPeriod':['1H','2H'],
                                  'team':[left_team,right_team],
                                  'time':event['time'].tolist(),
                                 },
                     template='plotly_dark',
                     height=800,
                     width=1100,
                     title=f"<span style='text-decoration:underline'>(L) {left_team} - {right_team} (R)</span>"
                     )
    
    fig.update_traces(hovertemplate=" %{customdata[0]} by %{customdata[1]} (%{customdata[2]}) at %{customdata[3]} <br> %{customdata[4]}m  %{customdata[5]}° ",
                      texttemplate = "%{customdata[0]} ((%{customdata[2]}))  by %{customdata[1]}")
    fig.update_layout(title=dict(x=0.3),)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    
    for k in range(len(fig.frames)):
        fig.frames[k]['layout'].update(title=dict(text=f"{k} {event.iloc[k]['eventName']} ({event.iloc[k]['tag']}) by {event.iloc[k]['shortName']} ",y=0.5,x=0.5))
    for button in fig.layout.updatemenus[0].buttons:
        button['args'][1]['frame']['redraw'] = True
        button['args'][1]["frame"]["duration"] = 2000
    
    return plot_pitch(fig)
    

################

def plot_destinations(fig,match_info,match_events,event,teams_id_name):
    left_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[0])]
    right_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[1])]
    sub = [[('1H',right_team,('x1','y1')),('2H',right_team,('x2','y2'))],[('1H',left_team,('x3','y3')),('2H',left_team,('x4','y4'))]]
    
    for row_idx, row_figs in enumerate(fig._grid_ref):
        for col_idx, col_fig in enumerate(row_figs):
            
            temp =  event.query(f"(matchPeriod=={[sub[row_idx][col_idx][0]]}) & (team=={[sub[row_idx][col_idx][1]]})")
            
            dests = match_events.loc[temp.index+1].fillna(value='?')
            
            fig.add_trace(go.Scatter(x=dests['x'],
                                      y=dests['y'],
                                      text=dests['shortName'],
                                      mode='markers',
                                      showlegend=False,
                                      customdata=dests[['subEventName','tag','shortName','time']],
                                      hovertemplate="%{customdata[0]} (%{customdata[1]}) by %{customdata[2]} at %{customdata[3]}",
                                      marker=dict(size=12,
                                                  color='deeppink',
                                                  symbol='hexagram',
                                                  line=dict(width=2),
                                                  ),
                                      ),
                                      row = row_idx+1,
                                     col = col_idx+1)
            for x0,x1,y0,y1 in zip(temp['x'],dests['x'],temp['y'],dests['y']):
                fig.add_shape(type="path",
                path=f"M {x0},{y0} Q {(x0+x1)/2},{(y0+y1)/2+3} {x1},{y1}",
                line_color="white",
                xref=sub[row_idx][col_idx][2][0],
                yref=sub[row_idx][col_idx][2][1],
                )
    return fig
    
def funct(x,team,match_events):
    if match_events.loc[match_events['shortName']==x,'team'].values[0] == team:
        return x
    else:
        return np.nan
    

st.set_page_config(layout="wide",page_title="Matches analysis")
st.markdown("""<head>
    <title> Style CSS </title>
    <style type="text/css">
    #div {color:maroon}
    div.Widget.row-widget.stRadio div{border-radius:5px;border-color:darkgreen}
    div.Widget.row-widget.stSelectbox div{border-radius:5px;border-color:darkgreen}
    div.Widget.row-widget.stTextInput div{border-radius:5px;background-color:rgba(0,205,0.5,0.1);border-color:darkgreen}
    div.Widget.row-widget.stMultiSelect div{border-radius:5px;background-color:lavenderblush;border-color:darkblue}
    
    </style>
    
</head>
  """,unsafe_allow_html=True)


####### MAIN
def main():
    st.title("Liverpool matches analysis (season 2017/2018)")
    
    MENU = st.sidebar.radio("MENU",['Introduction','Events Data',])
    
    if MENU == 'Introduction':
        st.title(MENU)
        
        st.markdown("""
        As a huge fan of Liverpool FC since many years now, and as a recent french graduate student in Data Science, I would love to share the best of both.
        To be able to gather the two most things i'm currently fond of as a whole is an incredible opportunity for me.
        <br><br> Also quite a funny coincidence that Liverpool FC is one of the <b>first European Club</b> so much involved in the manipulation of data.
        Today Data Science in sports analytics is step by step taking so much space in the process. The idea is obviously not so much to denature the magic unpredictability of soccer, but as in a lot of fields, there as some patterns that can be analyzed and from which we can learn to better perform the next time. It clearly and will never be a true science, but there are definitely some incredible things that can be done gathering these two fields.
        <br><br> Data Science can be used in soccer to make <b>performance analysis</b>, getting a new point of view of a match rather than reviewing videos, but also in <b>scouting</b>, analyzing some players through a whole season with aggregate data and <b>key performance indicator</b> that could rise from that. It even can be used to monitor players' <b>physic condition</b> in order to prevent muscular injuries.
        """,unsafe_allow_html=True)
        
    elif MENU == 'Events Data':
        st.markdown("""<br> <p style='border: 2px solid black; padding: 5px;'> The most data used today is called <i>Event Data</i>, a dataset where all actions are registered with which player does it, the timestamp the action is done, the location and the outcome. We'll be able to plot events on the pitch, to see density heatmaps, pitch control, possession frames, and animation around goals time to analyze the sequence.
        <br>I've used the open dataset provided by <a href='https://wyscout.com' target='_blank'> Wyscout </a> (see also the article published by <a href='https://www.nature.com/articles/s41597-019-0247-7' target='_blank'> Nature</a>)
        and you can easily find all the references and the presentation of the datasets on the Github public account of <a href='https://github.com/Friends-of-Tracking-Data-FoTD/mapping-match-events-in-Python' target='_blank'> Friends of Tracking </a>.
         <br>The data sets are released under the CC BY 4.0 License and are publicly available on figshare:
        <br>Pappalardo, Luca; Massucco, Emanuele (2019): <a href=' https://doi.org/10.6084/m9.figshare.c.4415000.v5' target='_blank'>Soccer match event dataset. figshare. Collection.</a>  </p> <br>
    """,unsafe_allow_html=True)
        
        league = st.sidebar.selectbox("Choose competition",['Premier League'])
        matches,events,tags,teams_id_name,teams_name_id,players = get_data(league)
        
        match_id = st.sidebar.selectbox("Select a match",[''] + matches.sort_values(by='gameweek')['wyId'].unique().tolist(),format_func=lambda x:matches.set_index('wyId').loc[x]['label'] if x is not '' else '')
        if match_id :
            match_info,match_events = get_match_infos(matches,match_id,teams_id_name,teams_name_id,players,events,tags)
        
            choice = st.sidebar.radio("What to see ?",['Event location','Team performance'])
            st.sidebar.markdown("---")

            teams,_,match_type,_,display = st.beta_columns([1,0.1,1,0.1,1])
            left_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[0])]
            right_team = teams_id_name[int(list(match_info['teamsData'].iloc[0].keys())[1])]
            opponent = matches.set_index('wyId').loc[match_id]['label'].split(',')[0].replace(' - ','').replace('Liverpool','')
    
            teams.text_input("Match",value=f"{matches.set_index('wyId').loc[match_id]['label']}")
            match_type.text_input("Date",value=f"{matches.set_index('wyId').loc[match_id]['date']}")
            display.text_input("Team sides at the start",value=f"{left_team} - {right_team}")
            st.markdown("---")
        
            if choice == 'Event location':
                with st.beta_expander(f"Event Location"):
                    params,sep,figure,exp = st.beta_columns([150,50,700,100])
                    sep.markdown("<p style='border-left:1px solid black;display: inline-block;height: 500px;margin: 0 20px;'> </p>",unsafe_allow_html=True)
                    
                    event_name = params.selectbox("Select an event",match_events['eventName'].unique())
                    sub_event_name = params.multiselect("Select a sub event",
                                                            match_events[match_events['eventName']==event_name]['subEventName'].unique().tolist()+['ALL'],
                                                            default=['ALL'])
                    tags = params.multiselect("Tags",
                                                      match_events.query(f"(eventName=={[event_name]})")['tag'].unique().tolist()+['ALL'],
                                                      default=['ALL'])
                    outcomes = params.multiselect("Outcome",
                                                        match_events.query(f"(eventName=={[event_name]})")['outcome'].unique().tolist()+['BOTH'],
                                                    default=['BOTH'])
                    plot = figure.empty()
                    
                    fig,event = plot_events_scatter(match_info,match_events,teams_id_name,match_id,event_name=event_name,sub_event_name=sub_event_name,tags=tags,outcomes=outcomes)
                    plot.plotly_chart(fig)
                    
                    
                    if params.button("Show destinations"):
                        fig_dest = plot_destinations(fig,match_info,match_events,event,teams_id_name)
                        plot.plotly_chart(fig_dest)
                #with st.beta_expander(f'Show {event_name} density'):
                    #density,event = plot_events_density(match_info,match_events,teams_id_name,match_id,event_name=event_name,sub_event_name=sub_event_name,tags=tags_id)
                    #st.plotly_chart(density)
                
                #st.write(match_events.query("(eventName=='Pass')")['tags'].value_counts())
                #st.write(match_events.loc[match_events.query("(eventName=='Pass')&(tags=='interception')").index+1])
                #st.write(match_events.query("(eventName=='Pass')&(subEventName!='Cross')")['tags'].value_counts())
                
                group = match_events.query("eventName!='Goalkeeper leaving line'").groupby(['team','matchPeriod','role','titular','shortName',]).agg(x_mean=('x','mean'),
                                                                                                                          y_mean=('y','mean'),
                                                                                                                          pass_nbre=('eventName','count')
                                                                                                                        ).reset_index()
                
                pos = px.scatter(group,
                                x='x_mean',
                                y='y_mean',
                                #color='matchPeriod',
                                color='team',
                                symbol='titular',
                                labels={'team':'Team'},
                                category_orders={'team':[left_team,right_team]},
                                symbol_map={'titular':'circle',
                                             'substitute':'hexagram'
                                
                                 },
                                size='pass_nbre',
                                #text='shortName',
                                custom_data=['shortName','role','pass_nbre'],
                                facet_col='matchPeriod',
                                facet_row='team',
                                template='plotly_dark',
                                width=800,
                                
                                )
                pos.update_traces(hovertemplate="%{customdata[0]} (%{customdata[1]}) : %{customdata[2]} total passes")
                pos.update_layout(title=dict(text="<span style='text-decoration:underline'>Passes network (for passes>1)</span>",x=0.5))
                indexes = match_events.query("(eventName=='Pass')&(outcome=='accurate')").index
                
                match_events.loc[list(indexes),'receiver'] = match_events.loc[list(indexes+1),'shortName'].values
                match_events.loc[match_events['team']==left_team,'receiver'] = match_events.loc[match_events['team']==left_team,'receiver'].apply(lambda x:funct(x,left_team,match_events) if pd.notnull(x) else np.nan)
                match_events.loc[match_events['team']==right_team,'receiver'] = match_events.loc[match_events['team']==right_team,'receiver'].apply(lambda x:funct(x,right_team,match_events) if pd.notnull(x) else np.nan)
                
                test = match_events.loc[match_events['receiver'].notnull()][['eventName','tag','shortName','receiver','team','matchPeriod']]
                utile = test.groupby(['matchPeriod','shortName','receiver']).size().reset_index(name='pass_nbre_between')
                last = utile.merge(group[['matchPeriod','team','shortName','x_mean','y_mean']],on=['matchPeriod','shortName']).merge(group[['matchPeriod','shortName','x_mean','y_mean']],
                    left_on=['matchPeriod','receiver'],
                    right_on=['matchPeriod','shortName'],
                    suffixes=['_launcher','_receiver'])
                    
                #st.write(group)
                #st.write(last)
                sub = [[('1H',right_team,('x1','y1')),('2H',right_team,('x2','y2'))],[('1H',left_team,('x3','y3')),('2H',left_team,('x4','y4'))]]
                for row_idx, row_figs in enumerate(pos._grid_ref):
                    for col_idx, col_fig in enumerate(row_figs):
                        temp =  last.query(f"(matchPeriod=={[sub[row_idx][col_idx][0]]}) & (team=={[sub[row_idx][col_idx][1]]})&(pass_nbre_between>1)")
                        for o in range(temp.shape[0]):
                            
                            pos.add_trace(go.Scatter(x=temp.iloc[o][['x_mean_launcher','x_mean_receiver']],
                                                      y=temp.iloc[o][['y_mean_launcher','y_mean_receiver']],
                                                      mode='lines',
                                                      showlegend=False,
                                                      customdata = temp.iloc[o][['team']],
                                                      line=dict(width=temp.iloc[o]['pass_nbre_between']/2,color='deeppink'),
                                                      ),
                                                      row = row_idx+1,
                                                      col = col_idx+1)
                            
                
                passes = px.bar(group.groupby(['matchPeriod','role','team'])['pass_nbre'].sum().reset_index().sort_values(by='pass_nbre',ascending=False),
                                x='role',
                                y='pass_nbre',
                                facet_col='matchPeriod',
                                #facet_col='team',
                                #facet_col_wrap=1,
                                text='pass_nbre',
                                color='team',
                                barmode='group',
                                labels={'team':'Team','role':''},
                                color_discrete_map={left_team:'darkblue',
                                                    right_team:'darkgrey'
                                
                                                    },
                                template='seaborn',
                                width=600,
                                title=f"{left_team} - {right_team} <br> total number of passes",
                                #color_continuous_scale=px.colors.sequential.RdBu,
                                #template='plotly_dark',
                )
                passes.update_xaxes(showgrid=False,)
                passes.update_yaxes(showticklabels=False,showgrid=False,visible=False)
                passes.update_layout(legend=dict(xanchor='right',yanchor='top'))
                passes.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
                
                
                
                
                
                #st.write(match_events.playerId.unique())
                with st.beta_expander("Passes network"):
                    pos.update_xaxes(visible=False)
                    pos.update_yaxes(visible=False)
                    pos.update_layout(legend=dict(orientation='h'))
                    col_1,col_2 = st.beta_columns([800,600])
                    col_3,col_4 = st.beta_columns(2)
                    col_1.plotly_chart(plot_pitch(pos))
            
                    col_2.plotly_chart(passes)
                
                with st.beta_expander("Density heatmaps"):
                    button_1,_,button_2,__= st.beta_columns([10,0.5,10,15])
                    _.markdown("<p style='border-left:1px solid black;display: inline-block;height: 40px;margin:0 0px;'> </p>",unsafe_allow_html=True)
                    figure,sep,params = st.beta_columns([650,50,350])
                    pass_button = button_1.button("Add Pass directions")
                    shot_button = button_2.button("Add Shot location")
                    sep.markdown("<p style='border-left:1px solid black;display: inline-block;height: 600px;margin:0 20px;'> </p>",unsafe_allow_html=True)
                    player = params.selectbox("Select a player",match_events.sort_values(by=['team','shortName'])['shortName'].unique())
                    #seq = params.selectbox("Select a sequence",match_events.query(f"shortName=={[player]}")['eventName'].unique())
                    match_events['color'] = match_events['outcome'].apply(lambda x:'red' if x=='not_accurate' else 'darkblue')
                    match_events['symbol'] = match_events['tag'].apply(lambda x:'diamond' if x=='Goal' else 'circle')
                    
                    temp = match_events.query(f"(shortName=={[player]})&(eventName=='Pass')")
                    stats_df_temp = match_events.query(f"(shortName=={[player]})").\
                    groupby(['matchPeriod','eventName','subEventName','outcome']).size().sort_values(ascending=False).reset_index(name='count')
                    stats_df = stats_df_temp[['matchPeriod','eventName','subEventName']].drop_duplicates().sort_values(by='matchPeriod')
                    
                    for period in stats_df['matchPeriod'].unique():
                        for event in stats_df['eventName'].unique():
                            for sub_event in stats_df['subEventName'].unique():
                                stats_df.loc[(stats_df['matchPeriod']==period)&(stats_df['eventName']==event)&(stats_df['subEventName']==sub_event),'total'] = stats_df_temp.loc[(stats_df_temp['matchPeriod']==period)&(stats_df_temp['eventName']==event)&(stats_df_temp['subEventName']==sub_event),'count'].sum()
                                stats_df.loc[(stats_df['matchPeriod']==period)&(stats_df['eventName']==event)&(stats_df['subEventName']==sub_event),'accuracy'] = np.round((stats_df_temp.loc[(stats_df_temp['matchPeriod']==period)&(stats_df_temp['eventName']==event)&(stats_df_temp['subEventName']==sub_event)&(stats_df_temp['outcome']=='accurate'),'count']/stats_df.loc[(stats_df['matchPeriod']==period)&(stats_df['eventName']==event)&(stats_df['subEventName']==sub_event),'total'])*100,2)
                                
                    
                    stat = px.sunburst(stats_df.fillna(0),
                                  path=['matchPeriod','eventName','subEventName'],
                                  values='total',
                                  color='accuracy',
                                  labels={'accuracy':'accuracy(%)'},
                                  color_continuous_scale='rdylgn'
                                )
                    stat.update_layout(margin=dict(l=0))
                    stat.update_traces(textinfo='label+value')
                   
                    params.plotly_chart(stat)
                    
                    fig = px.density_contour(match_events.query(f"(shortName=={[player]})"),
                                             x='x',
                                             range_x=[-55,55],
                                             y='y',
                                             #range_y=[-35,35],
                                             histfunc='avg',
                                             facet_col='matchPeriod',
                                             width=800,
                                             #color_continuous_scale='Reds',
                                             nbinsx=10,
                                             nbinsy=10,
                                             template='plotly_dark'
                                             #marginal_x='histogram',
                                             )
                    fig.update_traces(colorscale='Greens',reversescale=True,showscale=False,contours = dict(
                    showlines=False,
                    showlabels = False,
                    coloring='fill',
                    ))
                    fig.update_layout(title=dict(text=f"{player} ({temp[temp['shortName']==player]['role'].unique()[0]})",x=0.5),plot_bgcolor=px.colors.sequential.Greens[-1],coloraxis_showscale=False)
                    fig.update_yaxes(showgrid=False,visible=False)
                    fig.update_xaxes(showgrid=False,visible=False)
                    
                    if pass_button :
                        fig.update_layout(title=dict(text=f"{player} ({temp[temp['shortName']==player]['role'].unique()[0]}) Passes directions",x=0.5),plot_bgcolor=px.colors.sequential.Greens[-1],coloraxis_showscale=False)
                        _.markdown("<p style='border-left:1px solid black;display: inline-block;height: 150px;margin:0 0px;'> </p>",unsafe_allow_html=True)
                        button_1.markdown("""<div style='float:left;width:50%;'>
                           <font color='red'>Red arrows</font> are for <b>not accurate</b> passes <br><font color='blue'> Blue</font> arrows are for  <b>accurate</b> passes <br>
                        </div>
                        """,unsafe_allow_html=True)
                        
                        
                        sub = [[('1H',right_team,('x1','y1')),('2H',right_team,('x2','y2'))],[('1H',left_team,('x3','y3')),('2H',left_team,('x4','y4'))]]
                        
                        for row_idx, row_figs in enumerate(fig._grid_ref):
                            
                            for col_idx, col_fig in enumerate(row_figs):
                                
                                temp_bis = temp.query(f"(matchPeriod=={[sub[row_idx][col_idx][0]]})")
                                fig.add_trace(go.Scatter(x=temp_bis['x_to'],
                                     y=temp_bis['y_to'],
                                     text=temp_bis['subEventName'],
                                     mode='markers',
                                     showlegend=False,
                                     hovertemplate="%{text}",
                                     marker=dict(size=5,
                                                 color=temp_bis['color'],
                                                 ),
                                     ),
                                     row = row_idx+1,
                                     col = col_idx+1)
                                     
                                for x0,x1,y0,y1,color in zip(temp_bis['x'],temp_bis['x_to'],temp_bis['y'],temp_bis['y_to'],temp_bis['color']):
                                    fig.add_annotation(
                                        x=x1,ax=x0,y=y1,ay=y0,
                                        arrowcolor=color,
                                        showarrow=True,
                                        arrowhead=2,
                                        arrowwidth=2,
                                        xref=sub[row_idx][col_idx][2][0],
                                        axref=sub[row_idx][col_idx][2][0],
                                        yref=sub[row_idx][col_idx][2][1],
                                        ayref=sub[row_idx][col_idx][2][1],
                                        )
                                        
                    elif shot_button:
                        fig.update_layout(title=dict(text=f"{player} ({temp[temp['shortName']==player]['role'].unique()[0]}) Shot location",x=0.5),plot_bgcolor=px.colors.sequential.Greens[-1],coloraxis_showscale=False)
                        _.markdown("<p style='border-left:1px solid black;display: inline-block;height: 150px;margin:0 0px;'> </p>",unsafe_allow_html=True)
                        button_2.markdown("""
                          <font color='blue'> Blue</font> are for accurate shots <br> <font color='red'>Red</font> are for non accurate shots <br> Diamonds are for goals scored
                        """,unsafe_allow_html=True)
                        sub = [[('1H',right_team,('x1','y1')),('2H',right_team,('x2','y2'))],[('1H',left_team,('x3','y3')),('2H',left_team,('x4','y4'))]]
                        
                        for row_idx, row_figs in enumerate(fig._grid_ref):
                            
                            for col_idx, col_fig in enumerate(row_figs):
                                
                                temp_bis = match_events.query(f"(matchPeriod=={[sub[row_idx][col_idx][0]]})&(shortName=={[player]})&(subEventName==['Shot'])")
                                
                                fig.add_trace(go.Scatter(x=temp_bis['x'],
                                     y=temp_bis['y'],
                                     text=temp_bis['subEventName'],
                                     mode='markers',
                                     customdata=temp_bis[['outcome','distance_to_goal_from','angle_from','tag']],
                                     showlegend=False,
                                     hovertemplate="%{text} %{customdata[0]} (%{customdata[3]}) <br> distance : %{customdata[1]} <br> angle : %{customdata[2]}",
                                     marker=dict(size=10,
                                                 color=temp_bis['color'],
                                                 symbol=temp_bis['symbol'],
                                                 #line=dict(width=2),
                                                 ),
                                     ),
                                     row = row_idx+1,
                                     col = col_idx+1)
                            
                    figure.plotly_chart(plot_pitch(fig))
                
                with st.beta_expander("XG"):
                                          
                    filename = 'https://github.com/jmaignier/wyscout_data/blob/main/xg_model.sav?raw=true'
                    loaded_model = joblib.load(filename)
                    match_events.loc[(match_events['eventName']=='Shot')&(match_events['tag']=='Goal'),'Goal'] = 'Yes'
                    match_events['Goal'] = match_events['Goal'].fillna('No')
                    match_events.loc[(match_events['eventName']=='Shot'),'XG'] = np.round(loaded_model.predict_proba(match_events.loc[match_events['eventName']=='Shot',['distance_to_goal_from','angle_from']])[:,1],2)
                    match_events.loc[(match_events['eventName']=='Pass')&(match_events['distance_to_goal_to'].notnull()),'XG'] = np.round(loaded_model.predict_proba(match_events.loc[(match_events['eventName']=='Pass')&(match_events['distance_to_goal_to'].notnull()),['distance_to_goal_to','angle_to']])[:,1],2)
                   
                    #st.write(match_events.query("eventName=='Shot'"))
                    shots = px.scatter(match_events.query("eventName=='Shot'"),
                                       x='x',
                                       y='y',
                                       size='XG',
                                       facet_col='matchPeriod',
                                       facet_row='team',
                                       color='team',
                                       color_discrete_map={'Liverpool':'red',
                                                           opponent:'lightblue'
                                       },
                                       symbol='result',
                                       symbol_map={'Goal':'hexagram',
                                                   'opportunity':'circle',
                                                   '':'x'},
                                       hover_name='shortName',
                                       custom_data=['shortName','result','tag','good_foot','XG'],
                                       category_orders={'team':[left_team,right_team]},
                                       template='plotly_dark'
                                       )
                    shots.update_traces(hovertemplate="by %{customdata[0]} <br> %{customdata[1]} <br> body part : %{customdata[2]} <br> Right foot : %{customdata[3]} <br> xG : %{customdata[4]}")
                    st.plotly_chart(plot_pitch(shots))
                    
                
            
        #st.markdown("Rendre l'application beaucoup plus compréhensible en expliquant le premier volet <br> le deuxième plutôt clair <br> le troisième assez complexe et apporte peu d'information <br> le dernier à améliorer en rajoutant pied fort ou pied faible <br> Mettre l'accent sur les XG et les XA et les chances créées",unsafe_allow_html=True)
        
        
        
        
if __name__ == "__main__":
    main()
