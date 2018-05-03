# Basic procedure to put the data in an apropriate data frame, using pandas:
import pandas as pd
# adapting the dataset to pandas:
dataset=pd.read_csv("Crimes_-_2001_to_present.csv")
# here we create a variable to select the top 3 -- .head(3)
# of the Type of crime -- ["Primary Type"]
# most repeated in the dataset (counting the frequency of appearence) -- .value_counts()
frequency=dataset["Primary Type"].value_counts().head(3)
print(frequency)
# here we create a variable to select the last 3 -- .tail(3)
# of the Type of crime -- ["Primary Type"]
# most repeated in the dataset (counting the frequency of appearence) -- .value_counts()
frequency=dataset["Primary Type"].value_counts().tail(3)
print(frequency)
