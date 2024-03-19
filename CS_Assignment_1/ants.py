import pandas as pd
from scipy.stats import pearsonr

data = pd.read_excel('Assignment_1_Task_3.xlsx', sheet_name='Sheet2')

correlation1, _ = pearsonr(data['experiment-result'], data['evaporation-rate'])
correlation2, _ = pearsonr(data['experiment-result'], data['diffusion-rate'])

print(f'Correlation between experiment result and evaporation rate: {correlation1}')
print(f'Correlation between experiment result and diffusion rate: {correlation2}')
