#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:24:11 2024

@author: raquelprado
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'US_Cumulative_pop_change_2020_2023.csv'  
data = pd.read_csv(file_path)

# Extracting data for Puerto Rico
puerto_rico_data = data[data['Geographic Area'].str.contains("Puerto Rico", na=False)]

# Calculate the percentage change from the year 2020
base_population = puerto_rico_data['2020 Population Estimate'].values[0]
years = ['2021', '2022', '2023']
percentage_changes = [(puerto_rico_data[f'{year} Population Estimate'].values[0] / base_population - 1) * 100 for year in years]

# Add 2020 to the start of the list with a 0% change
years.insert(0, '2020')
percentage_changes.insert(0, 0)  # No change in the base year

# Create line graph
plt.figure(figsize=(10, 5))
plt.plot(years, percentage_changes, marker='o', linestyle='-', color='b')
plt.title('Percentage Change in Population of Puerto Rico (2020-2023)')
plt.xlabel('Year')
plt.ylabel('Percentage Change')
plt.grid(True)
plt.savefig('line_graph_Change_Puerto_Rico.png')
plt.show()

# create a bar graph showing the percent change

colors = ['grey','#add8e6', '#ffb6c1', '#dda0dd'] 
years = ['2020', '2021', '2022', '2023']
plt.figure(figsize=(10, 6)) 
bars = plt.bar(years, percentage_changes, color=colors)

# Adding percent change on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom' if yval < 0 else 'top', ha='center')

plt.title('Annual Percentage Change in Population of Puerto Rico (2020-2023)')
plt.xlabel('Year')
plt.ylabel('Percentage Change')
plt.ylim(min(percentage_changes) - 5, max(percentage_changes) + 5)
plt.axhline(0, color='gray', linewidth=0.8)  
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Population_Change_Puerto_Rico.png')
