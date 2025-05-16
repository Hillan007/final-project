# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

try:
    # Load and validate the COVID-19 data
    df = pd.read_csv('country_wise_latest.csv')
    required_columns = ['Country/Region', 'Deaths', 'Confirmed']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Define countries to analyze
    countries = ['United States', 'India', 'Brazil']

    # Filter the data - create a proper copy
    df_filtered = df[df['Country/Region'].isin(countries)].copy()
    if df_filtered.empty:
        raise ValueError("No data found for specified countries")

    # Calculate death rate using loc
    df_filtered.loc[:, 'death_rate'] = (df_filtered['Deaths'] / df_filtered['Confirmed']) * 100

    # Plot death rates with error checking
    plt.figure(figsize=(10, 5))
    for country in countries:
        subset = df_filtered[df_filtered['Country/Region'] == country]
        if not subset.empty:
            plt.bar(country, subset['death_rate'].iloc[0], label=country)
        else:
            print(f"Warning: No data found for {country}")

    plt.xlabel('Countries')
    plt.ylabel('Death Rate (%)')
    plt.title('COVID-19 Death Rate by Country')
    plt.legend()
    plt.show()

except FileNotFoundError:
    print("Error: Cannot find 'country_wise_latest.csv'. Please ensure the file exists in the correct location.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
