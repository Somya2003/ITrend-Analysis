# %% [markdown]
# #  IPhone Sales Analysis
# 

# %%
import pandas as pd
import numpy as np
import matplotlib
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# %%
data= pd.read_csv("apple_products.csv")

# %%
data

# %%
print(type(data))

# %%
print(data.isnull().sum())

# %%
print(data.describe())

# %% [markdown]
# # iphone Sales Analysis in india
# 

# %%
highest_rated=data.sort_values(by=["Star Rating"],ascending=False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])

# %% [markdown]
# # lets have a look at the number of rating of the higest i phone on flipkart

# %%
iphones=highest_rated["Product Name"].value_counts()
labels=iphones.index
counts=highest_rated["Number Of Ratings"]
figure=px.bar(highest_rated, x=labels, y=counts, title="Number of rating highest rated i phone")
figure.show()

# %%
iphones

# %%
iphones=highest_rated["Product Name"].value_counts()
labels=iphones.index
counts=highest_rated["Number Of Reviews"]
figure=px.bar(highest_rated, x=labels, y=counts, title="Number of reviews of highest rated i phone")
figure.show()

# %%
figure=px.scatter(data_frame=data, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols", title ="Ralationship between sale price and number of ratings")
figure.show()

# %%
figure=px.scatter(data_frame=data, x="Number Of Ratings", y="Discount Percentage", size="Sale Price", trendline="ols", title="Relationship between discount percentage and Number of Ratings")
figure.show()

# %%


# %%


# %%



