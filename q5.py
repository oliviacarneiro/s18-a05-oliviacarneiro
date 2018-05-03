# Basic procedure to put the data in an apropriate data frame, using pandas:
import pandas as pd
# adapting the dataset to pandas:
dataset=pd.read_csv("Crimes_-_2001_to_present.csv")
# here we do the same thing we did before, but instead of selecting cases with arrestment, we select cases with HOMICIDE
# and instead of sorting it by the most frequent type of crime, we do it by Area
frequency=dataset[dataset['Primary Type']=='HOMICIDE']["Community Area"].value_counts().head(1)
print(frequency)
