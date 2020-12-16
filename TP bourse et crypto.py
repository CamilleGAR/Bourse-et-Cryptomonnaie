# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:57:04 2020

@author: camil
"""


from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datetime
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.io as pio

#Permet d'afficher certaines courbes indisponibles sur spyder
pio.renderers.default='browser'


#Recuperation des dataframes
cac40 = wb.DataReader("^FCHI",start='2015-1-1',end='2019-12-31', data_source='yahoo')
bitcoin = wb.DataReader("BTC-EUR",start='2015-1-1',end='2019-12-30', data_source='yahoo') #Il faut mettre 2019-12-30 pour s'arreter au 31

#Creation de patch utilises comme legende
ouverture_patch = mpatches.Patch(color='teal', label='ouverture')
fermeture_patch = mpatches.Patch(color='darkorange', label='fermeture')
maxima_patch = mpatches.Patch(color='green', label='maxima')
minima_patch = mpatches.Patch(color='firebrick', label='minima')

log_cac_patch = mpatches.Patch(color='teal', label='rendement logarithmique du cac40')
ari_cac_patch = mpatches.Patch(color='darkorange', label='rendement arithmetique du cac40')
log_bit_patch = mpatches.Patch(color='green', label='rendement logarithmique du bitcoin')
ari_bit_patch = mpatches.Patch(color='firebrick', label='rendement arithmetique du bitcoin')

invest_j_patch = mpatches.Patch(color='mediumturquoise', label='investissement journalier sans clapet')
invest_m_patch = mpatches.Patch(color='gold', label='investissement mensuel sans clapet')
invest_a_patch = mpatches.Patch(color='firebrick', label='investissement annuel sans clapet')

invest_j_clapet_patch = mpatches.Patch(color='teal', label='investissement journalier avec clapet')
invest_m_clapet_patch = mpatches.Patch(color='darkorange', label='investissement mensuel avec clapet')
invest_a_clapet_patch = mpatches.Patch(color='maroon', label='investissement annuel avec clapet')


#Donnees cac40
dates_cac = list(map(lambda x: datetime.datetime.strptime(str(x),'%Y-%m-%d %H:%M:%S'), cac40.index))
ouverture_cac = cac40['Open'].values
fermeture_cac = cac40['Close'].values
maxima_cac = cac40['High'].values
minima_cac = cac40['Low'].values

#Courbes cac40
plt.plot(dates_cac, ouverture_cac, color = 'teal')
plt.plot(dates_cac, fermeture_cac, color = 'darkorange')
plt.plot(dates_cac, maxima_cac, color = 'green')
plt.plot(dates_cac, minima_cac, color = 'firebrick')

plt.legend(handles=[ouverture_patch, fermeture_patch, maxima_patch, minima_patch])
plt.title('Cac40')
plt.show()

#Courbes cac40 dernier mois de 2019
dates_cac_dmois = dates_cac[-20:]  #(on a que 20 valeurs)
plt.plot(dates_cac_dmois, ouverture_cac[-20:], color = 'teal')
plt.plot(dates_cac_dmois, fermeture_cac[-20:], color = 'darkorange')
plt.plot(dates_cac_dmois, maxima_cac[-20:], color = 'green')
plt.plot(dates_cac_dmois, minima_cac[-20:], color = 'firebrick')

plt.xticks([dates_cac_dmois[0], dates_cac_dmois[-1]],[dates_cac_dmois[0].strftime('%Y/%m/%d'), dates_cac_dmois[-1].strftime('%Y/%m/%d')])
plt.legend(handles=[ouverture_patch, fermeture_patch, maxima_patch, minima_patch])
plt.title('Cac40 dernier mois de 2019')
plt.show()

#Chandelier cac40
fig = go.Figure(data=[go.Candlestick(x=dates_cac,
                       open=ouverture_cac, high=maxima_cac,
                       low=minima_cac, close=fermeture_cac)])
fig.update_layout(title="Cac40", font=dict(size=30))
fig.show()


#Donnees bitcoin
dates_bit = list(map(lambda x: datetime.datetime.strptime(str(x),'%Y-%m-%d %H:%M:%S'), bitcoin.index))
ouverture_bit = bitcoin['Open'].values
fermeture_bit = bitcoin['Close'].values
maxima_bit = bitcoin['High'].values
minima_bit = bitcoin['Low'].values

#Courbes bitcoin
plt.plot(dates_bit, ouverture_bit, color = 'teal')
plt.plot(dates_bit, fermeture_bit, color = 'darkorange')
plt.plot(dates_bit, maxima_bit, color = 'green')
plt.plot(dates_bit, minima_bit, color = 'firebrick')

plt.legend(handles=[ouverture_patch, fermeture_patch, maxima_patch, minima_patch])
plt.title('Bitcoin')
plt.show()

#Courbes bitcoin dernier mois de 2019
dates_bit_dmois = dates_bit[-31:]
plt.plot(dates_bit_dmois, ouverture_cac[-31:], color = 'teal')
plt.plot(dates_bit_dmois, fermeture_cac[-31:], color = 'darkorange')
plt.plot(dates_bit_dmois, maxima_cac[-31:], color = 'green')
plt.plot(dates_bit_dmois, minima_cac[-31:], color = 'firebrick')

plt.xticks([dates_bit_dmois[0], dates_bit_dmois[-1]],[dates_bit_dmois[0].strftime('%Y/%m/%d'), dates_bit_dmois[-1].strftime('%Y/%m/%d')])
plt.legend(handles=[ouverture_patch, fermeture_patch, maxima_patch, minima_patch])
plt.title('Bitcoin dernier mois de 2019')
plt.show()

#Chandelier bitcoin
fig = go.Figure(data=[go.Candlestick(x=dates_bit,
                       open=ouverture_bit, high=maxima_bit,
                       low=minima_bit, close=fermeture_bit)])
fig.update_layout(title="Bitcoin", font=dict(size=30))
fig.show()


#Rendements journaliers
rend_log_j_cac, rend_ari_j_cac = list(), list()
for cours_actuel, cours_precedent in zip(ouverture_cac[1:], ouverture_cac[:-1]):
    rend_log_j_cac.append(np.log(cours_actuel/cours_precedent))
    rend_ari_j_cac.append((cours_actuel - cours_precedent)/cours_precedent)
    
rend_log_j_bit, rend_ari_j_bit = list(), list()
for cours_actuel, cours_precedent in zip(ouverture_bit[1:], ouverture_bit[:-1]):
    rend_log_j_bit.append(np.log(cours_actuel/cours_precedent))
    rend_ari_j_bit.append((cours_actuel - cours_precedent)/cours_precedent)
    
plt.plot(dates_cac[1:], rend_log_j_cac, color = 'teal')
plt.plot(dates_cac[1:], rend_ari_j_cac, color = 'darkorange')
plt.plot(dates_bit[1:], rend_log_j_bit, color = 'green')
plt.plot(dates_bit[1:], rend_ari_j_bit, color = 'firebrick')

plt.ylim(-0.25, 0.5)
plt.legend(handles=[log_cac_patch, ari_cac_patch, log_bit_patch, ari_bit_patch])
plt.title('rendements journaliers du bitcoin et du cac40')
plt.show()

#Rendements journaliers du dernier mois de 2019
plt.plot(dates_cac_dmois, rend_log_j_cac[-20:], color = 'teal')
plt.plot(dates_cac_dmois, rend_ari_j_cac[-20:], color = 'darkorange')
plt.plot(dates_bit_dmois, rend_log_j_bit[-31:], color = 'green')
plt.plot(dates_bit_dmois, rend_ari_j_bit[-31:], color = 'firebrick')

plt.ylim(-0.06, 0.175)
plt.xticks([dates_bit_dmois[0], dates_bit_dmois[-1]],[dates_bit_dmois[0].strftime('%Y/%m/%d'), dates_bit_dmois[-1].strftime('%Y/%m/%d')])
plt.legend(handles=[log_cac_patch, ari_cac_patch, log_bit_patch, ari_bit_patch])
plt.title('rendements journaliers sur le dernier mois de 2019')
plt.show()


#Rendements mensuels
values_debut_m_cac, values_fin_m_cac = [ouverture_cac[0]], list()
dates_months_cac = list()
for date1, date2, val1, val2 in zip(dates_cac[:-1], dates_cac[1:], ouverture_cac[:-1], ouverture_cac[1:]):
    if date1.month != date2.month :
        values_fin_m_cac.append(val1)
        values_debut_m_cac.append(val2)
        dates_months_cac.append(date1)
values_fin_m_cac.append(ouverture_bit[-1])
dates_months_cac.append(dates_cac[-1])
rend_log_m_cac = list(map(lambda d,f : np.log(f/d), values_debut_m_cac, values_fin_m_cac))
rend_ari_m_cac = list(map(lambda d,f : (f-d)/d, values_debut_m_cac, values_fin_m_cac))

values_debut_m_bit, values_fin_m_bit = [ouverture_bit[0]], list()
dates_months_bit = list()
for date1, date2, val1, val2 in zip(dates_bit[:-1], dates_bit[1:], ouverture_bit[:-1], ouverture_bit[1:]):
    if date1.month != date2.month :
        values_fin_m_bit.append(val1)
        values_debut_m_bit.append(val2)
        dates_months_bit.append(date1)
values_fin_m_bit.append(ouverture_bit[-1])
dates_months_bit.append(dates_bit[-1])
rend_log_m_bit = list(map(lambda d,f : np.log(f/d), values_debut_m_bit, values_fin_m_bit))
rend_ari_m_bit = list(map(lambda d,f : (f-d)/d, values_debut_m_bit, values_fin_m_bit))

plt.plot(dates_months_cac, rend_log_m_cac, color = 'teal')
plt.plot(dates_months_cac, rend_ari_m_cac, color = 'darkorange')
plt.plot(dates_months_bit, rend_log_m_bit, color = 'green')
plt.plot(dates_months_bit, rend_ari_m_bit, color = 'firebrick')

plt.ylim(-0.5, 1.5)
plt.legend(handles=[log_cac_patch, ari_cac_patch, log_bit_patch, ari_bit_patch])
plt.title('rendements mensuels du bitcoin et du cac40')
plt.show()

#Rendements mensuels de 2019
plt.plot(dates_months_cac[-12:], rend_log_m_cac[-12:], color = 'teal')
plt.plot(dates_months_cac[-12:], rend_ari_m_cac[-12:], color = 'darkorange')
plt.plot(dates_months_bit[-12:], rend_log_m_bit[-12:], color = 'green')
plt.plot(dates_months_bit[-12:], rend_ari_m_bit[-12:], color = 'firebrick')

plt.ylim(-0.2, 1)
plt.legend(handles=[log_cac_patch, ari_cac_patch, log_bit_patch, ari_bit_patch])
plt.title('rendements mensuels de 2019')
plt.show()


#Rendements annuels
values_debut_a_cac, values_fin_a_cac = [ouverture_cac[0]], list()
dates_years_cac = list()
dates_years_cac_datetime = list()
for date1, date2, val1, val2 in zip(dates_cac[:-1], dates_cac[1:], ouverture_cac[:-1], ouverture_cac[1:]):
    if date1.year != date2.year :
        values_fin_a_cac.append(val1)
        values_debut_a_cac.append(val2)
        dates_years_cac.append(str(date1.year))
        dates_years_cac_datetime.append(date1)
values_fin_a_cac.append(ouverture_bit[-1])
dates_years_cac.append(str(dates_cac[-1].year))
dates_years_cac_datetime.append(dates_cac[-1])
rend_log_a_cac = list(map(lambda d,f : np.log(f/d), values_debut_a_cac, values_fin_a_cac))
rend_ari_a_cac = list(map(lambda d,f : (f-d)/d, values_debut_a_cac, values_fin_a_cac))

values_debut_a_bit, values_fin_a_bit = [ouverture_bit[0]], list()
dates_years_bit = list()
dates_years_bit_datetime = list()
for date1, date2, val1, val2 in zip(dates_bit[:-1], dates_bit[1:], ouverture_bit[:-1], ouverture_bit[1:]):
    if date1.year != date2.year :
        values_fin_a_bit.append(val1)
        values_debut_a_bit.append(val2)
        dates_years_bit.append(str(date1.year))
        dates_years_bit_datetime.append(date1)
values_fin_a_bit.append(ouverture_bit[-1])
dates_years_bit.append(str(dates_bit[-1].year))
dates_years_bit_datetime.append(dates_bit[-1])
rend_log_a_bit = list(map(lambda d,f : np.log(f/d), values_debut_a_bit, values_fin_a_bit))
rend_ari_a_bit = list(map(lambda d,f : (f-d)/d, values_debut_a_bit, values_fin_a_bit))

plt.plot(dates_years_cac, rend_log_a_cac, color = 'teal')
plt.plot(dates_years_cac, rend_ari_a_cac, color = 'darkorange')
plt.plot(dates_years_bit, rend_log_a_bit, color = 'green')
plt.plot(dates_years_bit, rend_ari_a_bit, color = 'firebrick')

plt.ylim(-2, 17)
plt.legend(handles=[log_cac_patch, ari_cac_patch, log_bit_patch, ari_bit_patch])
plt.title('rendements annuels du bitcoin et du cac40')
plt.show()


#Postures d'investisseurs

#Decisions une fois par jour
def posture_j(ouverture, rendements, clapet = False):
    
    if clapet == True :
        clapet_max = ouverture[1]
        def condition(rend, rend_prec, value):
            return (rend >= rend_prec) and (rend >= 0) and (value < clapet_max)
    else :
        def condition(rend, rend_prec, value):
            return (rend >= rend_prec) and (rend >= 0)
        
    liquide_j = [10000]
    capital_j = [10000]
    actions_j = [0]
    for value, rend, rend_prec in zip(ouverture[2:], rendements[1:], rendements[:-1]):
        if condition(rend, rend_prec, value) :
            nb_achat = (liquide_j[-1]*0.2)//(value/100)
            liquide_j.append(liquide_j[-1] - nb_achat*(value/100))
            actions_j.append(actions_j[-1] + nb_achat)
            capital_j.append(liquide_j[-1] + actions_j[-1]*(value/100))
            
        else : 
            nb_ventes = (actions_j[-1]//2) +1
            liquide_j.append(liquide_j[-1] + nb_ventes *(value/100))
            actions_j.append(actions_j[-1] - nb_ventes)
            capital_j.append(liquide_j[-1] + actions_j[-1]*(value/100)) 
            
        if clapet == True and value > clapet_max :
            clapet_max = value
            
    return capital_j

#Decisions une fois par mois
def posture_a_m(values_fin, rendements, clapet = False):
    
    if clapet == True :
        clapet_max = values_fin[0]
        def condition(rend, rend_prec, value):
            return (rend >= rend_prec) and (rend >= 0) and (value < clapet_max)
    else :
        def condition(rend, rend_prec, value):
            return (rend >= rend_prec) and (rend >= 0)
        
    liquide = [10000]
    capital = [10000]
    actions = [0]
    for value, rend, rend_prec in zip(values_fin[1:], rendements[1:], rendements[:-1]):
        if condition(rend, rend_prec, value) :
            nb_achat = (liquide[-1]*0.2)//(value/100)
            liquide.append(liquide[-1] - nb_achat*(value/100))
            actions.append(actions[-1] + nb_achat)
            capital.append(liquide[-1] + actions[-1]*(value/100))
            
        else : 
            nb_ventes = (actions[-1]//2) +1
            liquide.append(liquide[-1] + nb_ventes *(value/100))
            actions.append(actions[-1] - nb_ventes)
            capital.append(liquide[-1] + actions[-1]*(value/100)) 
            
        if clapet == True and value > clapet_max :
            clapet_max = value
    return capital


        
#Investissements du Bitcoin, méthode sans clapet
p_j_bit = posture_j(ouverture_bit, rend_log_j_bit)
p_m_bit = posture_a_m(values_fin_m_bit, rend_log_m_bit)
p_a_bit = posture_a_m(values_fin_a_bit, rend_log_a_bit)
plt.plot(dates_bit[1:], p_j_bit, color = 'mediumturquoise')
plt.plot(dates_months_bit, p_m_bit, color = 'gold')
plt.plot(dates_years_bit_datetime, p_a_bit, color = 'firebrick')
plt.ylim(8000, 65000)
plt.legend(handles=[invest_j_patch, invest_m_patch, invest_a_patch])
plt.title('Evolution de notre capital avec investissement sur le Bitcoin')
plt.show()

#Investissements du Cac40, méthode sans clapet
p_j_cac = posture_j(ouverture_cac, rend_log_j_cac)
p_m_cac = posture_a_m(values_fin_m_cac, rend_log_m_cac)
p_a_cac = posture_a_m(values_fin_a_cac, rend_log_a_cac)
plt.plot(dates_cac[1:], p_j_cac, color = 'mediumturquoise')
plt.plot(dates_months_cac, p_m_cac, color = 'gold')
plt.plot(dates_years_cac_datetime, p_a_cac, color = 'firebrick')
plt.ylim(9500, 12500)
plt.legend(handles=[invest_j_patch, invest_m_patch, invest_a_patch])
plt.title('Evolution de notre capital avec investissement sur le Cac40')
plt.show()

#Investissements du Bitcoin, méthode avec clapet
p_j_clapet_bit = posture_j(ouverture_bit, rend_log_j_bit, clapet = True)
p_m_clapet_bit = posture_a_m(values_fin_m_bit, rend_log_m_bit, clapet = True)
p_a_clapet_bit = posture_a_m(values_fin_a_bit, rend_log_a_bit, clapet = True)
plt.plot(dates_bit[1:], p_j_clapet_bit, color = 'teal')
plt.plot(dates_months_bit, p_m_clapet_bit, color = 'darkorange')
plt.plot(dates_years_bit_datetime, p_a_clapet_bit, color = 'maroon')
plt.ylim(8000, 27000)
plt.legend(handles=[invest_j_clapet_patch, invest_m_clapet_patch, invest_a_clapet_patch])
plt.title('Evolution de notre capital avec investissement sur le Bitcoin')
plt.show()

#Investissements du Cac40, méthode avec clapet
p_j_clapet_cac = posture_j(ouverture_cac, rend_log_j_cac, clapet = True)
p_m_clapet_cac = posture_a_m(values_fin_m_cac, rend_log_m_cac, clapet = True)
p_a_clapet_cac = posture_a_m(values_fin_a_cac, rend_log_a_cac, clapet = True)
plt.plot(dates_cac[1:], p_j_clapet_cac, color = 'teal')
plt.plot(dates_months_cac, p_m_clapet_cac, color = 'darkorange')
plt.plot(dates_years_cac_datetime, p_a_clapet_cac, color = 'maroon')
plt.ylim(9500, 12500)
plt.legend(handles=[invest_j_clapet_patch, invest_m_clapet_patch, invest_a_clapet_patch])
plt.title('Evolution de notre capital avec investissement sur le Cac40')
plt.show()

#Comparaisons des deux méthode avec le Bitcoin
plt.plot(dates_bit[1:], p_j_bit, color = 'mediumturquoise')
plt.plot(dates_months_bit, p_m_bit, color = 'gold')
plt.plot(dates_bit[1:], p_j_clapet_bit, color = 'teal')
plt.ylim(8000, 70000)
plt.plot(dates_months_bit, p_m_clapet_bit, color = 'darkorange')
plt.legend(handles=[invest_j_patch, invest_m_patch, invest_j_clapet_patch, invest_m_clapet_patch])
plt.title('Comparaisons des deux méthode avec le Bitcoin')
plt.show()

#Comparaisons des deux méthode avec le Cac40
plt.plot(dates_cac[1:], p_j_cac, color = 'mediumturquoise')
plt.plot(dates_months_cac, p_m_cac, color = 'gold')
plt.plot(dates_cac[1:], p_j_clapet_cac, color = 'teal')
plt.plot(dates_months_cac, p_m_clapet_cac, color = 'darkorange')
plt.ylim(9500, 12500)
plt.legend(handles=[invest_j_patch, invest_m_patch, invest_j_clapet_patch, invest_m_clapet_patch])
plt.title('Comparaisons des deux méthode avec le Cac40')
plt.show()
