# IMPORTING LIBRARIES
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

converters = {
    "Original": lambda x: float(x.replace(",", "."))
}
df = pd.read_csv("data/coding-environment-exercise.csv", index_col=0, encoding="utf-8", delimiter=";", converters=converters) 
df["Original"] = df["Original"].astype(float)
colors = sns.color_palette('pastel')[0:len(df.index.tolist())]
plt.pie(df["Original"].tolist(), labels = df.index.tolist(), colors = colors, autopct='%1.1f%%')
plt.title("Pringles Original Nutrition Percentage Pie Chart")
plt.savefig("result/plot-pringles.png")
plt.show()
print("building successfully")
