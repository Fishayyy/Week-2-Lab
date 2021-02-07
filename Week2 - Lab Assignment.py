'''
Lab 2
'''

import pandas as pd
import matplotlib.pyplot as plt

######### Part 1 ###########


'''
    1) Download the iris-data-1 from Canvas, use pandas.read_csv to load it.

'''
# YOUR CODE GOES HERE
iris1 = pd.read_csv('iris-data-1.csv')

'''
    2) after loading the data:
       print out the index, columns, and values information
       print out the length of the dataset 
       print out the last 50 data points
       print out the labels (species)
       print out the petal_length for the last sample
'''
# YOUR CODE GOES HERE
print(iris1.index, iris1.columns, iris1.values)
print(len(iris1))
print(iris1.values[-50:])
print(iris1.species.unique())
print(iris1["petal_length"])

'''
    3) print out the mean and std of each feature (sepal_length, sepal_width, petal_length, petal_width)
    print out the mean of petal_length for first 100 samples
    print out the maximum and minimum values for each feature

'''
# YOUR CODE GOES HERE
print(iris1.mean())
print(iris1.std())

print(iris1["petal_length"][:100].mean())

print(iris1.max())
print(iris1.min())

'''
    4)  print out the frequency count of each class (setosa, versicolor, virginica)
    Hint: use pandas’ function value_counts 

'''
# YOUR CODE GOES HERE
print(iris1["species"].value_counts())

'''
    5) Use pandas.DataFrame.drop_duplicates to drop duplications in "petal_length" feature (keep the last instance) and print out the resulted data
    print out the length of the resulted dataset
    print out the mean of each feature
    print out the frequency count of each label (=class)

'''
# YOUR CODE GOES HERE
petalDupesDropped = iris1.drop_duplicates(subset='petal_length', keep='last')
print(petalDupesDropped)
print(len(petalDupesDropped))
print(petalDupesDropped.mean())
print(petalDupesDropped.species.value_counts())

######### Part 2 ###########
'''
    1)  Use pandas.DataFrame.plot() to plot all of the columns in a single graph. What is the X axis and Y axis on the rrsulted graph?

'''
# YOUR CODE GOES HERE
iris1.plot()
plt.show()

'''
    2)  plot the bar graph of your data
    Hint: pandas.DataFrame.plot.bar()
    
'''
# YOUR CODE GOES HERE
iris1.plot.bar()
plt.show()

'''
    4)  plot the histogram graph for "petal_length" feature
    Hint: pandas.DataFrame.plot.histograms()
    
'''
# YOUR CODE GOES HERE
iris1.plot.hist()
plt.show()

'''
    5)  Use the bar graph to show the frequency of each label (class)
'''
# YOUR CODE GOES HERE
iris1.species.value_counts().plot.bar()
plt.show()

######### Part 3 ###########

'''
    1) Download the iris-data-2 from Canvas, use pandas.read_csv to load it.

'''
# YOUR CODE GOES HERE
iris2 = pd.read_csv("iris-data-2.csv")

'''
    2) Use pandas.DataFrame.drop_duplicates to drop duplications in "ID" (keep the first instance) and save the resulted data frame in a new datafram (df). Print out the shape of df.

'''
# YOUR CODE GOES HERE
df = iris2.drop_duplicates(subset='ID', keep='first')
print(df.shape)

'''
    3)  plot the bar graph for df['color']
    Hint: pandas.DataFrame.plot.bar()
    
'''
# YOUR CODE GOES HERE
df['color'].value_counts().plot.bar()
plt.show()

'''
    4)  How many missing values we have in 'color' column?
    Hint: pandas.DataFrame.dropna()
    
'''
# YOUR CODE GOES HERE
dfDropped = df['color'].dropna()
print(len(df) - len(dfDropped))

'''
    5)  Make the values in 'color' column to be consistant and remove the unkown values
    Hint: pandas.DataFrame.replace()
       
'''
# YOUR CODE GOES HERE
df3 = df[df.color.notnull()]
df3['color'].str.lower()
df3 = df3[df3.color.isin(['red', 'purple', 'blue', 'pink'])]
print(df3)


##########Part 4 ###########

'''
    0) Repeat Q1 ,and Q2 in part 3

'''
# YOUR CODE GOES HERE
iris2 = pd.read_csv("iris-data-2.csv")
df = iris2.drop_duplicates(subset=['ID'], keep='first', inplace=False)

'''
    1) Make the values in 'color' column consistant and replace missing values with 'pink' 
    Hint: pandas.DataFrame.fillna()
    
'''
# YOUR CODE GOES HERE
df['color'].fillna('pink')
df['color'].str.lower()
print(df)