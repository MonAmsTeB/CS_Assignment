import pandas as pd
import matplotlib.pyplot as plt

# Load data — semicolon-delimited, comma as decimal separator
df = pd.read_csv("istherecorrelation.csv", sep=";", decimal=",")
df.columns = ["Year", "WO", "BeerConsumption"]

# Correlation coefficient between the two series
corr = df["WO"].corr(df["BeerConsumption"])

fig, ax1 = plt.subplots(figsize=(8, 5))

color1 = "#1f77b4"
ax1.set_xlabel("Year")
ax1.set_ylabel("WO [x1000]", color=color1)
ax1.plot(df["Year"], df["WO"], color=color1, marker="o", label="WO [x1000]")
ax1.tick_params(axis="y", labelcolor=color1)

ax2 = ax1.twinx()
color2 = "#d62728"
ax2.set_ylabel("NL Beer consumption [x1000 hectoliter]", color=color2)
ax2.plot(df["Year"], df["BeerConsumption"], color=color2, marker="s", label="Beer consumption")
ax2.tick_params(axis="y", labelcolor=color2)

plt.title(f"WO vs. NL Beer Consumption, 2006–2018 (r = {corr:.3f})")
fig.tight_layout()

plt.savefig("correlation_plot.png", dpi=300)
plt.show()

print(f"Pearson correlation coefficient: {corr:.4f}")