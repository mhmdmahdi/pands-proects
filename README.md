# pands-project - Day 1 23Apr2022
    23Apr2022
    Create Github Repository for pands-project - Done
    Familiarise myself with task at hand - Done
    Create a roadmap for completion of Project by Friday 29thApr2022 - Done

    24Apr2022
    Develop an understanding of Fisher's Iris Data Set
    Write a summary about the Data Set below

    25Apr2022-26Apr2022
    Write program analysis.py to output summary of each variable to a single text file

    27Apr2022
    Save a histogram of each variable to png files
    # Develop understading of possibilities with code and understanding of the fundamentals of histograms.
    # Completed on 01May2022

    28Apr2022
    Output a scatter plot of each pair of vaiables
    # Write my own code to create a histogram for each variable and save a histogram of each variable to png files.
    # Write my own code for a scatter plot of each pair of variables.
    # To begin this on 02May2022
    # Completed on 03May2022 with sns.pairplot
    # Revisited and completed again for each individual plot by 07May2022

    29Apr2022
    Generated summary text file
    https://towardsdatascience.com/understand-text-summarization-and-create-your-own-summarizer-in-python-b26a9f09fc70
    # This has already been created so there will be spillover from previous days work. This final day can also be used to tidy up code and files due for submission.

# pands-project - Day 2 24Apr2022
    Four features measured from each of 3 samples. These features were length and width of sepals and petals.
    ref#1 https://en.wikipedia.org/wiki/Iris_flower_data_set

    The data set is a multivariate data set and can be imported directly into Python using sklearn.
    The data set consists of 3 Classes with 50 samples per data set totaling 150 samples.
    *Goal of assignment is to predict what type of Iris a flower is based off of the available data points (or given features).*
    ref#2 https://www.youtube.com/watch?v=rdaG53khzv0&list=PLMAyPTgGwv2DUV6DZib9eMetsTTX87JNr

    Analysis can be done using Numpy and Numpy Arrays or using a Pandas DataFrame.
    (Can also be done using Python lists but this is not as good)
    Python has built in tools which can analyse all the data and return basic descriptive statistics.
    This should be done for each iris type, then when a value is inputted the code generated should search through the available code and try to best predict where this inputted value should lie.
    ref#3 https://www.youtube.com/watch?v=6BagRiSY1ds&list=PLMAyPTgGwv2DUV6DZib9eMetsTTX87JNr&index=2

# pands-project - Day 3 25Apr2022
    Number of different references that can be used to import and analyse the Fishers Iris Data Set.
    1) This Youtube lecture series uses pandas and explains the problem very well
    https://www.youtube.com/watch?v=6BagRiSY1ds&list=PLMAyPTgGwv2DUV6DZib9eMetsTTX87JNr&index=2
    2) This Notebook reference uses a number of built in functions available in Python and outputs the results of the dataset. I don't think I'd learn much from this reference but it will be a good check to come back to once I've completed the assignment as the results are very comprehensive. Its just the method of getting the results which seems too simple.
    https://www.kaggle.com/code/jchen2186/machine-learning-with-iris-dataset/notebook
    3) The scikit learn website and notebook seems to be a good starting point and uses numpy which I'm familiar with from the plottask.py assignment. However this reference only plays with the first 2 features of the dataset so I will need to keep this in mind. Also the plots are not the required plots for this assignment. Still this reference is a good starting point.
    https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
    4) After checking many of the references I don't think I will get away with avoiding the use of Pandas. I may try to start by following some of the references mentioned previously and this next reference and gain a minimal understanding of Pandas but I may also have to play catch up and squeeze in some time to catch up on the last of the lecture series, which I was hoping I could do after submitting this assignment. This github repository is very easy to follow and I will use this as the backbone of my project.
    https://github.com/RitRa/Project2018-iris

    Had some trouble importing the dataset but eventually got it. This may have been due to trying to run the code using the wrong interpreter which also caused me trouble for the plottask.py assignment. Not exactly sure what caused the fix but eventually the code just worked. Initial error message I was receiving was a long error message that seemed to be coming from the source file <"in __getattr__     return self[key] KeyError: 'datasets'">

# pands-project - Day 4 26Apr2022
    Developed an understanding of the contents of the imported module by writing the 'print' code for the different variables.
    Outputted a summary of the variables using the 'print' command to a summary text file. Need to remove the comments of this summary from the main code as it is redundant duplicating this text.

# pands-project - Day 5 27Apr2022
    As mentioned previously there are 4 variables (petal and sepal length and width) in the iris data set from each of 3 samples (Setosa, Versicolor and Virginica). This results in 150 lines of data.
    After beginning on todays work I realised that I need to put more time into the histograms. Today I have understood that what I am trying to do can be achieved in python. Now the goal for tomorrow will be the execution of this delivery. By copying code from Stack Overflow I know that the imported data I am using can be used to plot histograms. Reference: https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib
    Now what I need to do tomorrow is create my own code to build the histograms as I want them in a way that I undertand. Good understanding of histogram fundamentals was taken from the below reference: https://www.investopedia.com/terms/h/histogram.asp#:~:text=A%20histogram%20is%20a%20graphical,into%20logical%20ranges%20or%20bins.
    I have now readjusted the goals for the next couple of days.
    Other references used today:
    https://www.kaggle.com/code/jchen2186/machine-learning-with-iris-dataset/notebook
    https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
    https://github.com/RitRa/Project2018-iris
    https://www.kaggle.com/code/abhishekkrg/python-iris-data-visualization-and-explanation/notebook
    https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/
    https://www.codegrepper.com/code-examples/python/how+to+import+iris+dataset

# pands-project - Day 6 28Apr2022
    Extension on project granted until 08May2022.
    I will take today off and get back to work tomorrow.

# pands-project - Day 7 29Apr2022
    No work done on this project today

# pands-project - Day 8 30Apr2022
    No work done on this project today

# pands-project - Day 9 01May2022
    For today I'll just go through the video series and see if there's anything that will help with the code I am going to write over the next week now.
    https://www.youtube.com/watch?v=6BagRiSY1ds&list=PLMAyPTgGwv2DUV6DZib9eMetsTTX87JNr&index=2
        Need to import numpy as np, pandas as pd and seaborn as sns
        sns.set() - updates the plotting styles to use the seaborn plotting styles
    According to the lecture series referenced above pandas Dataframe makes things simpler than Numpy. For this reason I will use Pandas dataframe.
    Histogram of each variable plotted and saved.
        * If I have time after completing project I can come back and tidy up this code to iterate and print in 1 block of code as opposed to 4/5 different blocks of code
        * I should also come back and explain the data that each histogram is presenting
        * Pointing out the differences between python and excel could be of benefit in this regard and the benefits of choosing one over the other.

# pands-project - Day 10 02May2022
    No work done on this project today

# pands-project - Day 11 03May2022
   Attempted to complete the scatter plots for this assignment. Goal of today was to try find out which scatter plot pairs would be relevant.
   Achievement for today was loading the dataset into seaborn and figuring out which plots would are required.
   What I next want to do is create a scatter plot for the following:
    •sepal length vs petal width
    •sepal length vs petal length
    •sepal length vs sepal width
    •sepal width vs petal width
    •sepal width vs petal length
    •sepal width vs sepal length
    •petal length vs sepal width
    •petal length vs sepal length
    •petal length vs petal width
    •petal width vs sepal width
    •petal width vs sepal length
    •petal width vs petal length

# pands-project - Day 12 04May2022
    No work done on this project today

# pands-project - Day 13 05May2022
    No work done on this project today

# pands-project - Day 14 06May2022
    No work done on this project today

# pands-project - Day 15 07May2022
    Scatter plots created for each individual plot listed for Day 11 above and saved as png files.
    At this point the ask of the assignment is technically complete.
    Only task 4 remains which is:
        Perform any other analysis you think is appropriate.

    If I'm interested in the relationship between the features and what I'm trying to predict (as I've outlined as a task under Day 2):
        *Goal of assignment is to predict what type of Iris a flower is based off of the available data points (or given features).*
    then I need to write a model for machine learning. The question the model will answer is:
        • Based on the given set of datapoints, what is the species of iris?
        • Also what is the probability that the model above is correct when compared to the know target data
        • Final question to answer can be a prediction: Based on measurements (x,x,x,x) for (sl, sw, pl and pw) what is the species of iris
ref 1: https://www.youtube.com/watch?v=f3kSEebz8QA&list=PLMAyPTgGwv2DUV6DZib9eMetsTTX87JNr&index=4
ref 2: https://www.kaggle.com/code/jchen2186/machine-learning-with-iris-dataset/notebook
ref 3: https://github.com/RitRa/Project2018-iris

