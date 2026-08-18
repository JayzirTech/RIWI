import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.system('cls')

df = pd.read_csv('moral_machine_responses.csv')

df.replace(np.nan, 'no especificado', inplace=True)

# Tasa de mortalidad por tipo de escenario (%)
muertos_por_escenario = (1 - df.groupby('scenario_type')['saved'].mean()) * 100

print(f'{muertos_por_escenario}\n')

print(f'{df.info()}')
