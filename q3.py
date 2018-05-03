# Basic procedure to put the data in an apropriate data frame, using pandas:
import pandas as pd
# adapting the dataset to pandas:
dataset=pd.read_csv("Crimes_-_2001_to_present.csv")
# here we create a variable to identify
# the Types of crime -- ["Primary Type"]
# that appear on dataset (counting the frequency of appearence) -- .value_counts()
crime_frequency=dataset["Primary Type"].value_counts()
# here we create a variable to select, from the above identied values
# the crime that resulted in arrestment -- [dataset.Arrest==True]
# that appear on dataset (counting the frequency of appearence) -- .value_counts()
# the ["Primary Type"] is there to organize the counted values by type of crime
arrest_frequency=dataset[dataset.Arrest==True]["Primary Type"].value_counts()
# here we create a variable to calculate the proportion of
# crimes with arrestment arrest_frequency in the total, organized by type of crime
quotient=arrest_frequency/crime_frequency
#here we print the variable created above, but organizing in from the lower number to the higher
# and select just the last 4 - I decided to pick only the last 4 because they are equal, and the highest propotion (1 or 100%)
print(quotient.sort_values().tail(4))
