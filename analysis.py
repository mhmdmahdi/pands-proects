import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# dataset imported using the reference https://www.codegrepper.com/code-examples/python/how+to+import+iris+dataset
# loads the iris data set using scikitlearns built in datasets
data = load_iris()
pd.set_option('display.max_rows', None)

fig, axes = plt.subplots(nrows=2, ncols=2)
colors = ['blue', 'red', 'green']
for i, ax in enumerate(axes.flat):
    for label, color in zip(range(len(data.target_names)), colors):
        ax.hist(data.data[data.target == label, i],
                label=data.target_names[label], color=color)
        ax.set_xlabel(data.feature_names[i])
        ax.legend(loc='upper right')
plt.show()
# This code was completely copied off from Stack Overflow and modified slightly to suit my iris data file name. https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib
# For me the goal of copying and pasting this code directly from Stack Overflow was to see if this program could generate the histograms (and other plots) directly from the imported dataset without using numpy or pandas. The answer is yes. But by breaking down through Pandas as done below I can see exactly what is going on. The above code is very complicated and hard to understand.

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

# hist1 = "sepal length (cm)"
# df[hist1].hist()
# plt.suptitle(hist1)
# plt.show()

# hist2 = "sepal width (cm)"
# df[hist2].hist()
# plt.suptitle(hist2)
# plt.show()

# hist3 = "petal length (cm)"
# df[hist3].hist()
# plt.suptitle(hist3)
# plt.show()

# hist4 = "petal width (cm)"
# df[hist4].hist()
# plt.suptitle(hist4)
# plt.show()

# hist5 = data.feature_names
# df[hist5].hist()
# plt.suptitle(hist5)
# plt.show()

# The above histograms were created using the matplotlib hist function. However they don't give me much value added information so I will not spend much time on them to seperate out the species types into different colours. These different colours for the different species can be seen in the histogram produced from the lines of code in lines 11-19. Should I need the histograms can be re-created using seaborn to add colours to the charts.

sns.pairplot(df, hue="target")
plt.show()
# This line of code seems like a bit of a cheat code. It should output every pair of plots available from the dataset against each other. This will help me to discern which scatter plots are relevant then I can type out the line code for action #3 of the assignment as per the histogram code above.
# hue="target" adds colour to the plots to help differentiate as it calls in the relationship between x and y for different subsets of the data

iris = sns.load_dataset("iris")
iris.head()

# sns.scatterplot(data=iris, x="sepal_length", y="petal_width", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="sepal_length", y="petal_length", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="sepal_width", y="petal_width", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="sepal_width", y="petal_length", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="sepal_width", y="sepal_length", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="petal_length", y="sepal_width", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="petal_length", y="sepal_length", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="petal_length", y="petal_width", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="petal_width", y="sepal_width", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="petal_width", y="sepal_length", hue="species")
# plt.show()

# sns.scatterplot(data=iris, x="petal_width", y="petal_length", hue="species")
# plt.show()
# https: // seaborn.pydata.org/generated/seaborn.scatterplot.html  # seaborn.scatterplot

# I have left the scatterplots commented out after execution and saving to save having to close the plots each time the code is ran. I will also leave this in to show my work but the sns.pairplot suffice for my personal requirements so I will leave it in.

conditions = [
    (df['petal length (cm)'] <= 2.1),
    (df['petal length (cm)'] <= 4.95) & (df['petal width (cm)'] <= 1.65),
    (df['petal length (cm)'] >= 4.94) & (df['petal length (cm)'] <= 5.15) & (
        df['petal width (cm)'] >= 1.55) & (df['petal width (cm)'] <= 1.71),
    (df['petal width (cm)'] >= 1.6) & (df['petal length (cm)'] >= 5.2),
    (df['petal width (cm)'] >= 1.52) | (df['petal length (cm)'] >= 1.51)
]
# Created a list of conditions with specified criteria

values = [0, 1, 1, 2, 2]
# Defined the list of values to use if the Conditions above were met

df['predicted_name'] = np.select(conditions, values)
print(df)
# added a column to the pandas dataframe called predicted_names and assigned the values defined above to this new column
# https://datagy.io/pandas-conditional-column/
