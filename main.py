# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Project C114
# %% [markdown]
# ## Getting Data

# %%
import pandas
import numpy
import plotly.express as px

data_frame = pandas.read_csv("https://raw.githubusercontent.com/whitehatjr/datasets/master/main.csv")
toefl_score = data_frame["TOEFL Score"].to_list()
admitting_chance = data_frame["Chance of Admit "].to_list()

# %% [markdown]
# ## Figure of Data

# %%
chart = px.scatter(x=toefl_score, y=admitting_chance, labels=dict(y="Chance of Admitting", x="TOEFL Score"), title="Chance of Admitting based on TOEFL Score")
chart.show()

# %% [markdown]
# ## Linear Regression

# %%
m, c = numpy.polyfit(toefl_score, admitting_chance, 1)

y = []

for x in toefl_score:
    value = m * x + c
    y.append(value)

figure = px.scatter(x=toefl_score, y=admitting_chance, labels=dict(y="Chance of Admitting", x="TOEFL Score"), title="Chance of Admitting based on TOEFL Score")

figure.update_layout(shapes=[dict(type="line", x0=min(toefl_score), x1=max(toefl_score), y0=min(y), y1=max(y))])

figure.show()

# %% [markdown]
# ## Prediction

# %%
score = int(input("Enter TOEFL Score: "))
predicted_coa = m*score+c

print(f"Chance of someone admitting with a TOEFL score of {score} is {predicted_coa}")


