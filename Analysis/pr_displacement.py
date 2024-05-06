#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:12:26 2024

@author: raquelprado
"""

import pandas as pd
import matplotlib.pyplot as plt

# This script manipulates data related to internal displacement in Puerto Rico by:
# Filtering data by weather related hazard events
# Plotting line graph showing displacements per year
# Plotting Bar graph

# Read the Excel file
df = pd.read_excel("IDMC_GIDD_Disasters_Internal_Displacement_Data.xlsx")

# Rename the columns
df.rename(columns={'ISO3': 'Puerto Rico', 'country/ territory': 'Puerto Rico'}, inplace=True)

# Filter the data for only weather-related disasters
weather_related_df = df[df['Hazard Category'] == 'weather related']

# Calculate the total internal displacements for all years for weather-related disasters
total_displacements_all_years = weather_related_df["Disaster Internal Displacements"].sum()

# Calculate the total internal displacements by year for weather-related disasters
total_displacements_by_year = weather_related_df.groupby("Year")["Disaster Internal Displacements"].sum().reset_index()
total_displacements_by_year.columns = ["Year", "Total Displacements by Year"]
df = df.merge(total_displacements_by_year, on="Year", how="left")

# Add a column
df["Total Displacements (All Years)"] = total_displacements_all_years

# Calculate total displacements per year
total_displacements_by_year = df.groupby("Year")["Disaster Internal Displacements"].sum().reset_index()

# Line plot
plt.figure(figsize=(10, 6))
plt.plot(total_displacements_by_year["Year"], total_displacements_by_year["Disaster Internal Displacements"], marker='o')
plt.title('Total Displacements caused by Weather related events by Year in Puerto Rico')
plt.xlabel('Year')
plt.ylabel('Total Displacements in Puerto Rico')
plt.grid(True)
plt.xticks(total_displacements_by_year["Year"], rotation=45)
plt.tight_layout()
plt.savefig('total_displacements_by_year_line.png')

# Bar graph
plt.figure(figsize=(12, 8))
plt.bar(total_displacements_by_year["Year"], total_displacements_by_year["Disaster Internal Displacements"])
plt.title('Total Internal Displacements caused by Weather related events by Year in Puerto Rico')
plt.xlabel('Year')
plt.ylabel('Total Internal Displacements')
plt.grid(True)
plt.xticks(total_displacements_by_year["Year"], rotation=45)
plt.tight_layout()
plt.savefig('total_displacements_by_year_bar.png')

# Adjust the plot layout
plt.tight_layout()

# Show the plot
plt.show()