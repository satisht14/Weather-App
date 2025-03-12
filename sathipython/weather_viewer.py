import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("weather_data.csv")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Display basic statistics
print("\nDataset Overview:\n", df.head())
print("\nSummary Statistics:\n", df.describe())

# Plot temperature trends
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Temperature"], marker="o", linestyle="-", color="b", label="Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()
