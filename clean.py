# Select specific countries
countries = ["Kenya", "USA", "India"]
df_filtered = df[df["location"].isin(countries)]

# Convert 'date' column to datetime format
df_filtered["date"] = pd.to_datetime(df_filtered["date"])

# Fill missing values using interpolation
df_filtered.fillna(method="ffill", inplace=True)