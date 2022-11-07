import pandas as pd

df = pd.read_csv("../csv/cards.csv")

# update 

df.to_csv("../csv/cards.csv", index=False)
