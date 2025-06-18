import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#import the actual origional data
df = pd.read_excel(r"C:\Users\User\PycharmProjects\DeckCardProject\new_file.xlsx")

# Data inspection and cleaning
df.columns = df.columns.str.strip()  # Remove extra spaces in column names
df.rename(columns={'Mathes Played': 'Matches Played'}, inplace=True)  # Fix column typo, rewrite name
df.index = range(1, len(df) + 1)  # Ensure index starts at 1
df.fillna(0, inplace=True)  # Fill missing values

# Safeguard against division by zero when calculating 'Win Rate'
df['Win Rate'] = df['Wins'] / df['Matches Played'].replace(0, 1)

# Convert Win Rate to percentage and round it
df['Win Rate (%)'] = (df['Win Rate'] * 100).round(2)

# Display cleaned DataFrame
print(df.head(33))  # Show first 33 rows
print(df.describe(include='all'))  # Summary statistics

# Group by 'Deck Name' and aggregate data
deck_summary = df.groupby('Deck Name').agg({
    'Wins': 'sum',
    'lost': 'sum',
    'Matches Played': 'mean',
    'Win Rate': lambda x: x.mean() * 100  # Convert Win Rate to percentages, is important cause in line 18
}).reset_index()


# Round the 'Win Rate' in deck_summary
deck_summary['Win Rate'] = deck_summary['Win Rate'].round(2)

# Display the deck summary
print(deck_summary)

# matplotlib, seaborn

df.to_excel(r"C:\Users\User\PycharmProjects\DeckCardProject\cleaned_data.xlsx", index=False)

# Example of plotting with the updated method
plt.figure(figsize=(10, 6))
sns.barplot(x='Deck Name', y='Win Rate (%)', data=df, hue='Deck Name', palette='viridis', legend=False)
plt.title('Win Rate by Deck')
plt.xticks(rotation=90)  # Rotate x labels if they are long
plt.show()

# Create a scatter plot to see the relationship between Wins and Matches Played
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Matches Played', y='Wins', data=df, hue='Deck Name', palette='Set1')

# Add labels and title
plt.title('Wins vs Matches Played by Deck Name')
plt.xlabel('Matches Played')
plt.ylabel('Wins')

# Show the plot
plt.tight_layout()
plt.show()
