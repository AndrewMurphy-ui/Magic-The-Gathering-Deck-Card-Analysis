import openpyxl
import pandas as pd

df = pd.read_excel(r"C:\Users\User\Documents\MTG project\data\Tournamentdata.xlsx")
df.to_excel(r"C:\Users\User\PycharmProjects\DeckCardProject\new_file.xlsx", index=False)
df = pd.read_excel(r"C:\Users\User\PycharmProjects\DeckCardProject\new_file.xlsx")