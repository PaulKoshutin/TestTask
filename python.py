import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data.xlsx")
df["receiving_date"] = pd.to_datetime(df["receiving_date"], format="%d.%m.%Y", errors="coerce")
one = df[df.receiving_date.dt.month == 7].loc[df.status != "ПРОСРОЧЕНО"]["sum"].sum(numeric_only=True)
print(one)

two = df.groupby(df['receiving_date'].dt.date)["sum"].sum().plot.line(x='receiving_date', y='sum')
plt.show()