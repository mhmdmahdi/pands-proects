import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# dataset imported using the reference https://www.codegrepper.com/code-examples/python/how+to+import+iris+dataset

data = load_iris()

print(list(data.target_names))
# ['setosa', 'versicolor', 'virginica',]
print(list(data))
# ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']
# attempted to print this command to see what else what stored in the load_iris dataset
print(list(data.target))
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(list(data.feature_names))
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print(data.data)
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
# This code was completely ripped off from Stack Overflow and modified slightly to my iris data file name. https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib
# I need to come back to this and come up with my own code that I actually understand
# For me the goal of copying and pasting this code directly from Stack Overflow was to see if this program could generate the histograms (and other plots) directly from the imported dataset without using numpy or pandas. The answer is yes...
