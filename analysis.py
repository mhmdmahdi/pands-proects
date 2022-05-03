import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# dataset imported using the reference https://www.codegrepper.com/code-examples/python/how+to+import+iris+dataset
# loads the iris data set using scikitlearns built in datasets
data = load_iris()

# print(list(data.target_names))
# ['setosa', 'versicolor', 'virginica',]
# print(list(data))
# ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']
# attempted to print this command to see what else what stored in the load_iris dataset
# print(list(data.target))
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(list(data.feature_names))
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# print(data.data)
# I attempted print(data) which returns all of the information stored in the imported module. The raw data is stored within a list in this file called 'data'. By using the print(data.data) function I was able to isolate just the raw data.
# Using all of the above information I could see that the 0's represent 'setosa', 1's represent versicolor and 2's represent 'virginica'.
# This also meant that the the first 50 rows in the raw data were associated with 'setosa'/ 0's, the second 50 rows associated with 'versicolor'/ 1's and the third 50 rows associated with 'virginica'/ 2's.
# The 1st column in the data was for sepal lenth, 2nd column for sepal width, 3rd column for petal length and 4th column for petal width.

fig, axes = plt.subplots(nrows=2, ncols=2)
colors = ['blue', 'red', 'green']
for i, ax in enumerate(axes.flat):
    for label, color in zip(range(len(data.target_names)), colors):
        ax.hist(data.data[data.target == label, i],
                label=data.target_names[label], color=color)
        ax.set_xlabel(data.feature_names[i])
        ax.legend(loc='upper right')
plt.show()
# This code was completely copied off from Stack Overflow and modified slightly to my iris data file name. https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib
# For me the goal of copying and pasting this code directly from Stack Overflow was to see if this program could generate the histograms (and other plots) directly from the imported dataset without using numpy or pandas. The answer is yes but I do not understand how. By breaking down through Pandas as done below I can see exactly what is going on. The above code is very complicated.

# had to install pandas using 'python -m pip install pandas'
df = pd.DataFrame(data["data"], columns=data["feature_names"])
# Creating a Pandas DataFrame from the data
df["target"] = data["target"]
# Adding 'target' data to dataframe under a new column called 'target'
df["target_name"] = df["target"].map(
    {0: "setosa", 1: "versicolor", 2: "virginica"})
# Adding 'target_name' data to dataframe under a new column and using the mapping function to pair this wth the defined target syntax.
print(df)

print(df.describe())
# returns some statistical information

hist1 = "sepal length (cm)"
df[hist1].hist()
plt.suptitle(hist1)
plt.show()

hist2 = "sepal width (cm)"
df[hist2].hist()
plt.suptitle(hist2)
plt.show()

hist3 = "petal length (cm)"
df[hist3].hist()
plt.suptitle(hist3)
plt.show()

hist4 = "petal width (cm)"
df[hist4].hist()
plt.suptitle(hist4)
plt.show()

hist5 = data.feature_names
df[hist5].hist()
plt.suptitle(hist5)
plt.show()
# If I have time after completing project I can come back and tidy up this code to iterate and print in 1 block of code as opposed to 4/5 different blocks of code

# sns.pairplot(df, hue="target")
# This line of code seems like a bit of a cheat code. It should output every pair of plots available from the dataset against each other. This will help me to discern which scatter plots are relevant then I can type out the line code for action #3 of the assignment as per the histogram code above.
# Had to install then import seaborn
# This line of code didn't actually work for me so I will plot each scatter plot individually.

iris = sns.load_dataset("iris")
iris.head()
print(iris)
# sns.scatterplot(data=tips, x="total_bill", y="tip")
# https: // seaborn.pydata.org/generated/seaborn.scatterplot.html  # seaborn.scatterplot
