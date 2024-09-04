import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data.xlsx")

one = df[df[df['status'] == 'Июль 2021'].index[0]:df[df['status'] == 'Август 2021'].index[0]].loc[df.status != "ПРОСРОЧЕНО"]["sum"].sum(numeric_only=True)
print(one, "\n")

indexes = df[(df['status'] != 'ПРОСРОЧЕНО') & (df['status'] != 'ВНУТРЕННИЙ') & (df['status'] != 'ОПЛАЧЕНО') & (df['status'] != 'В РАБОТЕ') & (df['status'] != 'НА ПОДПИСАНИИ')].index.tolist()
indexes.append(df.index[-1])
months = df[(df['status'] != 'ПРОСРОЧЕНО') & (df['status'] != 'ВНУТРЕННИЙ') & (df['status'] != 'ОПЛАЧЕНО') & (df['status'] != 'В РАБОТЕ') & (df['status'] != 'НА ПОДПИСАНИИ')].status.tolist()
sums = []
for i in range(len(indexes) - 1):
    sums.append(df[indexes[i]:indexes[i + 1]]["sum"].sum())
two = plt.plot(months, sums)
plt.show()

three = df[df[df['status'] == 'Сентябрь 2021'].index[0]:df[df['status'] == 'Октябрь 2021'].index[0]].groupby('sale')["sum"].sum().idxmax()
print(three, "\n")

four = df[df[df['status'] == 'Октябрь 2021'].index[0]:df.index[-1]].groupby('new/current')['client_id'].count()
print(four, "\n")

df["receiving_date"] = pd.to_datetime(df["receiving_date"], format="%d.%m.%Y", errors="coerce")
five = df.loc[:df[df['status'] == 'Июнь 2021'].index[0]].loc[df.receiving_date.dt.month == 6].loc[df.document == "оригинал"]['client_id'].count()
print(five, "\n")

def calc(x):
    if x >= 10000:
        return x * 0.05
    else:
        return x * 0.03

toCalculate = df.loc[:df[df['status'] == 'Июль 2021'].index[0]].loc[(df.receiving_date.dt.month >= 7) & (df.receiving_date.dt.day > 1)]
bonus1 = toCalculate.loc[toCalculate['new/current'] == "новая"].loc[toCalculate.status == "ОПЛАЧЕНО"].loc[df.document == "оригинал"].groupby('sale')["sum"].sum().apply(lambda x: x * 0.07)
bonus2 = toCalculate.loc[toCalculate['new/current'] == "текущая"].loc[toCalculate.status != "ПРОСРОЧЕНО"].loc[df.document == "оригинал"].groupby('sale')["sum"].sum().apply(calc)

bonus = bonus1.add(bonus2, fill_value=0)

print(bonus1, "\n")
print(bonus2, "\n")
print(bonus, "\n")