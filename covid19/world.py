import pandas as pd

df = pd.read_csv("owid-covid-data.csv")

print(df.columns)

df_ir= df.loc[df["location"]=="Iran"]

print(df_ir["total_deaths"].sum())
