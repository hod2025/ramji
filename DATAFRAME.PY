import pandas as pd
df = pd.read_csv("user_data.csv")
df.head(3)
df.tail(3)
age=df["Age"]
# print(age)
print(df.loc[1])
df.info()