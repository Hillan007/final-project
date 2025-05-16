# Import required libraries
import pandas as pd

# Load the data
try:
    # Read the CSV file
    df = pd.read_csv('country_wise_latest.csv')
    
    # Select specific countries
    countries = ["Kenya", "USA", "India"]
    df_filtered = df[df["Country/Region"].isin(countries)]
    
    # Convert 'date' column to datetime format if it exists
    if 'date' in df_filtered.columns:
        df_filtered["date"] = pd.to_datetime(df_filtered["date"])
    
    # Fill missing values using interpolation
    df_filtered.fillna(method="ffill", inplace=True)
    
    # Save cleaned data
    df_filtered.to_csv('cleaned_data.csv', index=False)
    print("Data cleaning completed successfully!")

except FileNotFoundError:
    print("Error: Cannot find the CSV file. Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
