#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:24:28 2024

@author: raquelprado
"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'soc_vul_PR.xlsx'
data = pd.read_excel(file_path)

# columns to keep
columns_to_keep = [
    'GEO_ID', 'STATE', 'COUNTY', 'TRACT', 'NAME', 
    'PRED0_E', 'POPUNI', 'PRED12_E', 'PRED3_E']
data = data[columns_to_keep]

# Convert COUNTY column to string to filter
data['COUNTY'] = data['COUNTY'].astype(str).str.zfill(3)

# Define the list of county codes for the poorest counties
county_codes = ['055', '001', '093', '015', '079']

# Filter the data for the five poorest counties
filtered_data = data[data['COUNTY'].isin(county_codes)]

# Aggregate the data for each risk factor across counties
total_population = filtered_data['POPUNI'].sum()
total_pred0 = filtered_data['PRED0_E'].sum()
total_pred12 = filtered_data['PRED12_E'].sum()
total_pred3 = filtered_data['PRED3_E'].sum()

# Calculate the percentages
percentage_pred0 = (total_pred0 / total_population) * 100
percentage_pred12 = (total_pred12 / total_population) * 100
percentage_pred3 = (total_pred3 / total_population) * 100


categories = ['No Risk Factors', '1-2 Risk Factors', '3+ Risk Factors']
percentages = [percentage_pred0, percentage_pred12, percentage_pred3]

# Bar graph of percentage of total population  by Risk Factor in the
# 5 poorest counties of Puerto Rico
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, percentages, color=['#add8e6', '#90ee90', '#ff8c00'])
plt.title('Percentage of Total Population by Risk Factors in Five Poorest Counties of Puerto Rico')
plt.xlabel('Risk Factor Categories')
plt.ylabel('Percentage of Total Population')

# Adding text labels to bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}%', va='bottom') 

# Save the figure
plt.savefig('Percentage_Risk_Factors_Poorest_Counties_PR.png')

plt.show()

#%%

# Bar graph of percentage of 
# Total population by risk factors

# Calculate the total population of Puerto Rico
total_population_PR = data['POPUNI'].sum()

# Aggregate the data for each risk factor across all of Puerto Rico
total_pred0 = data['PRED0_E'].sum()
total_pred12 = data['PRED12_E'].sum()
total_pred3 = data['PRED3_E'].sum()

# Calculate the percentages
percentage_pred0 = (total_pred0 / total_population_PR) * 100
percentage_pred12 = (total_pred12 / total_population_PR) * 100
percentage_pred3 = (total_pred3 / total_population_PR) * 100

# Prepare data for plotting
categories = ['No Risk Factors', '1-2 Risk Factors', '3+ Risk Factors']
percentages = [percentage_pred0, percentage_pred12, percentage_pred3]

# Bar graph of percentage of 
# Total population by risk factors
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, percentages, color=['#add8e6', '#90ee90', '#ff8c00'])
plt.title('Percentage of Total Population by Risk Factors Across Puerto Rico')
plt.xlabel('Risk Factor Categories')
plt.ylabel('Percentage of Total Population')

# Adding text labels to bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}%', va='bottom')

# Save the figure
plt.savefig('Percentage_Risk_Factors_All_Puerto_Rico.png')

plt.show()