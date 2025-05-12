df_filtered["death_rate"] = df_filtered["total_deaths"] / df_filtered["total_cases"]

# Plot death rates
plt.figure(figsize=(10, 5))
for country in countries:
    subset = df_filtered[df_filtered["location"] == country]
    plt.plot(subset["date"], subset["death_rate"], label=country)

plt.xlabel("Date")
plt.ylabel("Death Rate")
plt.title("COVID-19 Death Rate Over Time")
plt.legend()
plt.show()