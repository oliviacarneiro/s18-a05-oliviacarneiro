# Basic procedure to put the data in an apropriate data frame, using pandas:
import pandas as pd
# adapting the dataset to pandas:
dataset=pd.read_csv("Crimes_-_2001_to_present.csv")
# here we creat a loop to:
# first identify the cases with weapon
# then, classify it, by yes or no
def involved_weapon(text):
    weapon=['ARM', 'GUN', 'KNIFE', 'WEAPON', 'STICK']
    h='no'
    for w in weapon:
        if w in text:
            h='yes'

    if "NO WEAPON" in text:
        h='no'

    return h
#here we count the frequency that yes and no has appeared
x=dataset['Description'].apply(involved_weapon).value_counts()
# we will use again this variable, that shows the total number of crimes
crimes=dataset.shape
# and finally we create a variable dividing the number of yes by the total
y=x['yes']/crimes[0]
# print the value in number format
print(float(y))
