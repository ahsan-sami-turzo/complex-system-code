import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = "ants-with-pheromones-behavior-space-data.xlsx"
data = pd.read_excel(file_path, sheet_name="Sheet1")

# Filter rows with non-zero ticks (cast ticks to numeric before filtering)
try:
    data = data[pd.to_numeric(data["ticks"], errors='coerce') != 0]  # Handle potential conversion errors
except:
    print("Error: There might be non-numeric values in the 'ticks' column. Please check your data.")
    exit()

# Convert all columns to numeric (handle potential errors)
try:
    data = data.apply(pd.to_numeric, errors='coerce')  # Handle potential conversion errors
except:
    print("Error: There might be non-numeric values in some columns. Please check your data and handle appropriately.")
    exit()

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

# FACETGRID
categorical_columns = ["max-step-size", "evaporation-rate", "population", "max-turn-angle"]
for col in categorical_columns:
  data[col] = data[col].astype("category")
# Define a list of parameter names excluding 'ticks'
parameter_names = categorical_columns
# Create FacetGrid
g = sns.FacetGrid(data, col=parameter_names)
# Create scatter plots for each parameter vs ticks
g.map(sns.scatterplot, "ticks", x=parameter_names)
# Adjust layout and title
g.fig.suptitle("Effect of Parameters on Ticks (Conditional on Other Parameters)")
plt.tight_layout()
plt.show()
