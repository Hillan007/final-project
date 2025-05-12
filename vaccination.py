plt.figure(figsize=(10, 5))
for country in countries:
    subset = df_filtered[df_filtered["location"] == country]
    plt.plot(subset["date"], subset["total_vaccinations"], label=country)

plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.title("COVID-19 Vaccinations Over Time")
plt.legend()
plt.show()