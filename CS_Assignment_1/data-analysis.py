import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = "ants-with-pheromones-behavior-space-data.xlsx"  # Replace with your actual file path
sheet_name = "Sheet1"  # Assuming data is in "Sheet1"

try:
    # Read data, handle potential non-numeric values
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    data = data[pd.to_numeric(data["ticks"], errors='coerce') != 0]  # Filter rows with non-zero (numeric) ticks
    data = data.apply(pd.to_numeric, errors='coerce')  # Convert all columns to numeric (handle errors)
except Exception as e:
    print(f"Error loading or cleaning data: {e}")
    exit()

# sheet_name = "Cleaned_Data"
# writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
# data.to_excel(writer, sheet_name=sheet_name, index=False)
# writer.save()
data.to_csv("cleaned_data.csv", index=False)

min_ticks = data["ticks"].min()
max_ticks = data["ticks"].max()

# Define a list of parameter names excluding 'ticks'
parameter_names = ["max-step-size", "evaporation-rate", "population", "max-turn-angle", "diffusion-rate"]

# HEATMAP
heatmap_data = data
plt.figure(figsize=(12, 8))
heatmap = plt.pcolor(heatmap_data, vmin=min_ticks, vmax=max_ticks)
plt.colorbar(heatmap)
plt.xlabel("Parameters")
plt.ylabel("Combinations")
plt.title(f"Heatmap of Ticks (Min: {min_ticks}, Max: {max_ticks})")
plt.show()

# PAIR-PLOT
sns.pairplot(data, diag_kind="kde")
plt.show()
