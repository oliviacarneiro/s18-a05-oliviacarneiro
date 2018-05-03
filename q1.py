# Basic procedure to put the data in an apropriate data frame, using pandas:
import pandas as pd
# adapting the dataset to pandas:
dataset=pd.read_csv("Crimes_-_2001_to_present.csv")
#creating a new variable to count the lines, as each line is a crime, we are actually counting the number of lines:
#the .shape function gives us the number of lines and columns
crimes=dataset.shape
# to print the asked proportion, as we only need the number of lines, we put crimes[0] - meaning that we are only using the first argument
# then, we devide the number of crimes by the population of Chicago
# Chicago population = 2704958
# then, we multiply it by a thousand
print((crimes[0]/2704958)*1000)
