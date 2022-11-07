import pandas as pd

df = pd.read_csv("../csv/cards.csv")

# update card_type column with yellow randomly to 15% of the rows
df.loc[df.sample(frac=0.15).index, "card_type"] = "yellow"
# update card_type column with red randomly to 7% of the rows
df.loc[df.sample(frac=0.07).index, "card_type"] = "red"

df.to_csv("../csv/cards.csv", index=False)
