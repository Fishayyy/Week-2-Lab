'''
Lab 2
'''

import pandas as pd

######### Part 1 ###########


'''
    1) Download the iris-data-1 from Canvas, use pandas.read_csv to load it.

'''
# YOUR CODE GOES HERE
iris1 = pd.read_csv('iris-data-1.csv', index_col=0)

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

'''
    4)  print out the frequency count of each class (setosa, versicolor, virginica)
    Hint: use pandas’ function value_counts 

'''
# YOUR CODE GOES HERE


'''
    5) Use pandas.DataFrame.drop_duplicates to drop duplications in "petal_length" feature (keep the last instance) and print out the resulted data
    print out the length of the resulted dataset
    print out the mean of each feature
    print out the frequency count of each label (=class)

'''
# YOUR CODE GOES HERE

######### Part 2 ###########
'''
    1)  Use pandas.DataFrame.plot() to plot all of the columns in a single graph. What is the X axis and Y axis on the rrsulted graph?

'''
# YOUR CODE GOES HERE



'''
    2)  plot the bar graph of your data
    Hint: pandas.DataFrame.plot.bar()
    
'''
# YOUR CODE GOES HERE

'''
    4)  plot the histogram graph for "petal_length" feature
    Hint: pandas.DataFrame.plot.histograms()
    
'''
# YOUR CODE GOES HERE


'''
    5)  Use the bar graph to show the frequency of each label (class)
'''
# YOUR CODE GOES HERE


######### Part 3 ###########

'''
    1) Download the iris-data-2 from Canvas, use pandas.read_csv to load it.

'''
# YOUR CODE GOES HERE

'''
    2) Use pandas.DataFrame.drop_duplicates to drop duplications in "ID" (keep the first instance) and save the resulted data frame in a new datafram (df). Print out the shape of df.

'''
# YOUR CODE GOES HERE


'''
    3)  plot the bar graph for df['color']
    Hint: pandas.DataFrame.plot.bar()
    
'''
# YOUR CODE GOES HERE


'''
    4)  How many missing values we have in 'color' column?
    Hint: pandas.DataFrame.dropna()
    
'''
# YOUR CODE GOES HERE



'''
    5)  Make the values in 'color' column to be consistant and remove the unkown values
    Hint: pandas.DataFrame.replace()
       
'''
# YOUR CODE GOES HERE


##########Part 4 ###########

'''
    0) Repeat Q1 ,and Q2 in part 3

'''
# YOUR CODE GOES HERE

'''
    1) Make the values in 'color' column consistant and replace missing values with 'pink' 
    Hint: pandas.DataFrame.fillna()
    
'''
# YOUR CODE GOES HERE
