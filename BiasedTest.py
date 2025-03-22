import pandas as pd
from scipy.stats import (chi2_contingency)

df = pd.read_excel(r"C:\Users\User\PycharmProjects\DeckCardProject\new_file.xlsx")
df.columns = df.columns.str.strip()# Create a contingency table for wins/losses per deck
print(df.columns)

contingency_table = df.groupby('Deck Name')[['Wins', 'lost']].sum()

# Run the Chi-Square test
chi2, p, _, _ = chi2_contingency(contingency_table)

print(f"Chi-Square Value: {chi2}")
print(f"P-Value: {p}")

if p < 0.05:
    print("Win rates are significantly different (not random, potential bias).")
else:
    print("No significant difference in win rates (fair distribution).")
