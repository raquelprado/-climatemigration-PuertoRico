## Abstract 
This project provides an analysis of climate-driven migration in Puerto Rico, focusing on the the estimates of migration driven by climate disasters, the identification of flood zone areas, and the assessment of social vulnerability factors. 

## Data
The data utilized in this analysis comes from multiple sources. The [Internal Displacement Monitoring Centre](https://www.internal-displacement.org/database/displacement-data/) provides comprehensive data on internal displacements globally due to conflicts or weather-related events. Additionally, the [Community Resilience Estimates (CRE)](https://www.census.gov/data/experimental-data-products/cre-pr.html) from Puerto Rico offer insights into social vulnerability and the region's susceptibility to natural disasters by analyzing risk factors. Lastly, I also incorporate population change data for Puerto Rico from 2020 to 2023, sourced from the [US Census Bureau](https://www.census.gov/data/tables/time-series/demo/popest/2020s-state-total.html), which provides annual and cumulative estimates of the resident population.

My research focused on evaluating the number of internal displacements caused by weather-related hazards in Puerto Rico over the period from 2017 to 2022. Subsequently, I examined the percentage change in Puerto Rico's population from 2020 to 2023, noting that this calculation did not specifically account for climate-related migration. This analysis aimed to provide a comprehensive view of recent population trends in Puerto Rico.

Additionally, I analyzed the social vulnerability in Puerto Rico using data from the US Census Bureau’s Community Resilience Estimates. This analysis is based on a metric designed to gauge a community's ability to endure and recover from disasters such as hurricanes or other hazardous events. Social vulnerability was assessed using 10 indicators provided by the US Census Bureau:

- Poverty status
- Disability status
- Number of caregivers in the households
- Unit-level crowding
- Vehicle access
- Broadband internet
- Employment
- Education
- Age
- Health insurance



## Running Scripts 

pr_displacement.py(insert link) processes and visualizes data on internal displacements due to weather-related hazards in Puerto Rico from 2017 to 2022. It starts by reading and cleaning the displacement data, ensuring it is specific to Puerto Rico and focused on weather-related disasters. The script then aggregates total displacements for all years and also by individual years. To illustrate these findings, it generates two types of plots: a line graph and a bar graph. 

per_change_pop_pr.py(insert link) analyzes and visualizes the population change in Puerto Rico between 2020 and 2023. The script calculates the percentage change in population starting from 2020 as the base year, with subsequent years (2021, 2022, and 2023) compared against this baseline to determine the annual population growth or decline. These percentage changes are then visually represented in two distinct ways. First, a line graph is created to display the percentage changes over the years, providing a clear visual trend of population shifts.Second, the script generates a bar graph that details the same percentage changes year by year. This bar graph uses different colors for each year to visually distinguish between them and includes annotations on each bar that denote the exact percentage change, ensuring the data is immediately understandable. 

RiskFactor_perc_PR.py(insert link) analyzes and visualizes risk factors related to social vulnerability in Puerto Rico, specifically focusing on the five poorest counties. Using data from the soc_vul_PR.xlsx(insert link), which includes Community Resilience Estimates by the US Census Bureau, the script selects relevant columns, filters data for the specified counties, and calculates the proportion of the population within various risk categories. It then generates a bar graph that illustrates the percentage of the population in these counties with zero, one to two, and three or more risk factors, clearly highlighting the elevated vulnerability in these regions. A second bar graph extends the analysis to all population in Puerto Rico, providing a territory-wide perspective on social vulnerability. This comparative approach allows for a direct visualization of how these impoverished counties compare against the broader demographic landscape, emphasizing areas that may require focused intervention to mitigate the impacts of natural disasters. 

Puerto_Rico_Maps_GIS_Package.ppk(insert link) contains a series of maps created using ArcGIS, which integrate data from the Community Resilience Estimates along with essential shapefiles for Puerto Rico. Initially, three separate maps were developed to depict the distribution of three distinct risk factor categories across Puerto Rico: zero risk factors, one to two risk factors, and three or more risk factors. These visualizations help in understanding the spatial distribution of social vulnerability across the territory. Subsequently, a more focused map was produced, specifically highlighting areas with three or more risk factors alongside the five poorest counties in Puerto Rico. This map also incorporates a flood zone layer to provide insights into potential flood-prone routes within these regions. This detailed mapping approach aids in assessing the heightened risk and potential impact of flooding on the most vulnerable communities, supporting better planning and risk management strategies.


## Analysis and Results

The initial analysis delved into internal displacement data in Puerto Rico, focusing specifically on displacements caused by weather-related events. The analysis, represented through line and bar graphs, highlights the trends and annual comparisons of displacements. Notably, the data shows a significant spike in displacements in 2017, which is attributed to the devastating impact of Hurricane Maria. This peak in displacements is expected given the severity of the storm. However, it's concerning that the data also indicates a gradual increase in displacements over the subsequent years. This trend suggests a persistent vulnerability to weather-related events, underscoring the need for ongoing attention to resilience and preparedness measures in the region.

![Image of internal displacements bar graph and line graph]


Secondly, I expanded my analysis beyond internal displacements to also consider the outflow migration from Puerto Rico. Utilizing data from the US Census Bureau, I analyzed the trends in migration between 2020 and 2023. Although these figures aren't specifically linked to weather-related events or natural disasters, the analysis revealed a noticeable decrease in the total population, which is intensifying significantly over this period. Factors such as the pursuit of higher education, better job opportunities, and improved quality of life likely contribute to this trend, yet the data points to a considerable population decline within just a three-year span. 

![image of the percent change in population, line and bar graph]

Subsequently, using the Community Resilience Estimates for Puerto Rico, I generated maps to illustrate the social vulnerability across various counties on the island. These maps clearly delineated areas categorized by different levels of risk factors—0, 1-2, and 3 or more—highlighting which communities are more likely to be resilient or vulnerable to natural hazards and disasters. This visualization helps identify regions where social vulnerability may impact the ability to respond to and recover from such events.

![image of map of puerto rico with 3 risk factors]


The final map produced focused on illustrating regions in Puerto Rico with three or more risk factors, specifically emphasizing the five poorest counties. Additionally, this map incorporated flood zone layers to identify areas susceptible to flooding and to determine the overlap between these zones and regions with high vulnerability indicators. The expectation was that the poorest counties, characterized by significant risk factors, would also coincide with high flood risk areas, suggesting a compounded vulnerability to natural disasters.

However, the mapping analysis revealed a counterintuitive pattern: the majority of flood-prone areas were actually in more affluent counties, notably near San Juan, the capital and a wealthier urban center. This suggests that while the poorest counties are indeed vulnerable to disasters due to socio-economic factors, the geographic distribution of flood risks primarily affects more affluent regions. The findings indicate that mobility in response to flood risks is often a privilege of those with higher incomes and better resources, highlighting a disparity in vulnerability and resilience across different socioeconomic groups in Puerto Rico. This nuanced understanding helps refine emergency preparedness and urban planning strategies to address the specific needs of both economically disadvantaged and affluent communities.

![image of map puerto rico with flood zone]



Following the mapping analysis, I delved deeper into the distribution of risk factors across Puerto Rico to gain a clearer understanding of the regional disparities in vulnerability. The analysis revealed that a mere 14.74% of the total population is without any risk factors, suggesting a relatively low level of baseline resilience. Conversely, 39.19% of the population has 1-2 risk factors, and a significant 46.07% are burdened with 3 or more risk factors, underscoring a widespread vulnerability to natural disasters and hazards throughout the island.

![image of risk factors across puerto rico]


The situation is particularly acute in the five poorest counties, where it was anticipated that a higher percentage of the population would exhibit 3 or more risk factors and a correspondingly lower percentage would have no risk factors. Indeed, the findings confirm this hypothesis, indicating that these areas are at an increased risk of suffering disproportionately during natural disasters due to their compounded socio-economic challenges.


![image of risk factors across 5 poorest counties]


## Final Considerations

With climate change exacerbating the frequency and intensity of natural disasters like hurricanes and causing sea level rise, enhancing infrastructure, improving access to resources, and implementing robust disaster preparedness programs become even more critical. Moreover, migration should be considered as a viable adaptation strategy, particularly for communities on islands like Puerto Rico, which are highly susceptible to these environmental threats.
These findings underscore the urgent need for targeted interventions and policy adjustments to bolster resilience in Puerto Rico's most vulnerable regions. Special attention should also be directed towards socio-economically disadvantaged areas that might not traditionally align with recognized geographical risk zones, such as flood plains.
 Ensuring that resilience-building efforts are inclusive and comprehensive is essential. Such measures will help these communities adapt more effectively to the adverse effects of climate change, securing a safer and more resilient future for all residents.