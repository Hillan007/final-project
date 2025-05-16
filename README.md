# COVID-19 Data Analysis Project

## Overview
This project analyzes COVID-19 data across different countries using Python, focusing on visualizing trends and comparing statistics between major nations including the United States, India, and Brazil.

## Features
- Data cleaning and validation
- Visualization of COVID-19 cases trends
- Death rate analysis
- Vaccination progress tracking
- Country-wise comparisons

## Requirements
- Python 3.x
- Required packages:
```bash
pip install pandas matplotlib seaborn
```

## Project Structure
```
week8/
│
├── analyze_deaths.py      # Death rate analysis
├── clean.py              # Data cleaning script
├── vaccination.py        # Vaccination data analysis
├── visual_trends.py      # Trend visualization
└── country_wise_latest.csv    # Dataset
```

## Data Source
The analysis uses the `country_wise_latest.csv` dataset, which includes:
- Country/Region information
- Confirmed cases
- Death counts
- Other COVID-19 related metrics

## Scripts Description

### visual_trends.py
- Creates line plots showing COVID-19 case trends
- Compares data across United States, India, and Brazil
- Includes error handling and data validation

### analyze_deaths.py
- Calculates and visualizes death rates
- Provides country-wise death rate comparisons
- Includes data validation and error handling

### clean.py
- Handles missing values
- Filters relevant countries
- Saves cleaned data for analysis

## How to Run
1. Clone the repository
2. Install required packages:
```bash
pip install pandas matplotlib seaborn
```
3. Run the scripts:
```bash
python visual_trends.py
python analyze_deaths.py
python clean.py
```

## Error Handling
- File not found errors
- Data validation
- Empty dataset handling
- Missing value management

## Visualization Features
- Grid-style plots using Seaborn
- Rotated x-axis labels for better readability
- Clear legends and titles
- Proper figure sizing and layout

## Future Improvements
- Add more countries for comparison
- Include time series analysis
- Add interactive visualizations
- Implement automated data updates

## Author
Victor Hillan Muthomi

