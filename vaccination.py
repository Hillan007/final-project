import pandas as pd
import matplotlib.pyplot as plt

try:
    # Load vaccination data
    df = pd.read_csv('country_wise_latest.csv')
    
    # Define countries to analyze
    countries = ['United States', 'India', 'Brazil']
    
    # Filter data and validate
    df_filtered = df[df['Country/Region'].isin(countries)].copy()
    if df_filtered.empty:
        raise ValueError("No data found for specified countries")
        
    # Create the plot
    plt.figure(figsize=(10, 5))
    for country in countries:
        subset = df_filtered[df_filtered['Country/Region'] == country]
        if not subset.empty:
            plt.plot(subset.index, subset['Confirmed'], label=country)
        else:
            print(f"Warning: No data found for {country}")

    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.title("COVID-19 Cases by Country")
    plt.legend()
    plt.show()

except FileNotFoundError:
    print("Error: Cannot find the CSV file. Please check if it exists in the current directory.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
