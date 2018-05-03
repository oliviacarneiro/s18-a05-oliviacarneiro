# Basic procedure to put the data in an apropriate data frame, using pandas:
import pandas as pd
# adapting the dataset to pandas:
dataset=pd.read_csv("Crimes_-_2001_to_present.csv")
# here we create a variable to identify
# the Types of crime -- ["Primary Type"]
# that appear on dataset (counting the frequency of appearence) -- .value_counts()
# the only difference from the previous question, is that we are creating a serie, and naming this column as "a"
crime_frequency=pd.Series(dataset["Primary Type"].value_counts(),name='a')
# here we create a variable to select, from the above identied values
# the crime that resulted in arrestment -- [dataset.Arrest==True]
# that appear on dataset (counting the frequency of appearence) -- .value_counts()
# the ["Primary Type"] is there to organize the counted values by type of crime
# the only difference from the previous question, is that we are creating a serie, and naming this column as "b"
arrest_frequency=pd.Series(dataset[dataset.Arrest==True]["Primary Type"].value_counts(),name='b')
# here we create a variable to calculate the proportion of
# crimes with arrestment arrest_frequency in the total, organized by type of crime
# the only difference from the previous question, is that we are creating a serie, and naming this column as "c"
quotient=pd.Series(arrest_frequency/crime_frequency,name='c')
#now we make a table with the created columns, and sort it by the propotion (column "c")
newdataset=pd.concat([crime_frequency,arrest_frequency,quotient],axis=1).sort_values(by="c")
#now we print the cases with more then a thousand occurences and thake the highest one
print(newdataset[newdataset.a>=1000].tail(1))
