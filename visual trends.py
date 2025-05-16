import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    # Load the data
    df = pd.read_csv('country_wise_latest.csv')

    # Set plot style
    sns.set_style("whitegrid")

    # Define countries to analyze
    countries = ['United States', 'India', 'Brazil']

    # Filter data
    df_filtered = df[df['Country/Region'].isin(countries)].copy()
    if df_filtered.empty:
        raise ValueError("No data found for specified countries")

    # Plot total cases
    plt.figure(figsize=(10, 5))
    for country in countries:
        subset = df_filtered[df_filtered['Country/Region'] == country]
        if not subset.empty:
            plt.plot(subset.index, subset['Confirmed'], label=country)
        else:
            print(f"Warning: No data found for {country}")

    plt.xlabel("Time")
    plt.ylabel("Total Cases")
    plt.title("COVID-19 Total Cases by Country")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: Cannot find the CSV file. Please check if it exists in the current directory.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
