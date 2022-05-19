
# Agréger le data de tous les participants dans un cvs ou un excel unique 

import pandas as pd
import researchpy as rp
import scipy.stats as stats
import matplotlib.pyplot as plot

df = pd.read_csv('Data_SRT.csv')
print(df.head())

# Calculer moyenne RT congruents et RT incongruents 
# Je veux faire deux sous data frames, un pour congruent et un pour incongruent 

## Datafram congruent:
congruent_right = df[(df.Block == 'block_right_hand') & (df.Trial == 'right')]
congruent_left = df[(df.Block == 'block_left_hand') & (df.Trial == 'left')]

congruent_trials = pd.concat([congruent_right,congruent_left], ignore_index=True)


print(congruent_trials["RT"].mean())

## Datafram incongruent:
incongruent_right = df[(df.Block == 'block_right_hand') & (df.Trial == 'left')]
incongruent_left = df[(df.Block == 'block_left_hand') & (df.Trial == 'right')]

incongruent_trials = pd.concat([incongruent_right,incongruent_left], ignore_index=True)

print(incongruent_trials["RT"].mean())



