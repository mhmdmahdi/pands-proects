# pands-project
    Create Github Repository for pands-project - Done
    Develop an understanding of Fisher's Iris Data Set
    Write a summary about the Data Set
    Write program analysis.py to output summary of each variable to a single text file
    Save a histogram of each variable to png files
    Output a scatter plot of each pair of vaiables
    Generated summary text file
    https://towardsdatascience.com/understand-text-summarization-and-create-your-own-summarizer-in-python-b26a9f09fc70
    # This has already been created so there will be spillover from previous days work. This final day can also be used to tidy up code and files due for submission.

# Data set summary
    Four features measured from each of 3 samples. These features were length and width of sepals and petals.
    The data set is a multivariate data set and can be imported directly into Python using sklearn.
    The data set consists of 3 Classes with 50 samples per data set totaling 150 samples.
    *Goal of assignment is to predict what type of Iris a flower is based off of the available data points (or given features).*
    Analysis can be done using Numpy and Numpy Arrays or using a Pandas DataFrame.

# Plots
    Scatter plots created for each individual plot listed and saved as png files.
    At this point the ask of the assignment is technically complete. Only task 4 remains which is:
        - Perform any other analysis you think is appropriate.
        - I'm interested in the relationship between the features and what I'm trying to predict (as I've outlined as a task under Day 2):
        *Goal of assignment is to predict what type of Iris a flower is based off of the available data points (or given features).*
    then :
        • Based on the given set of datapoints, what is the species of iris? i.e. a prediction: Based on measurements (x,x,x,x) for (sl, sw, pl and pw) what is the species of iris
        *This is essentially a Decision Tree. I came to learn later in the course of pythons capabilities with regards to prediction algorithms in the sense that a prediction algorithm that can be utilised from sklearn which is a form of supervised learning available in pythons library. What I modelled in this assignment was a humanistic approach to prediction based off of observations I instinctively arrived at from viewing the plots when it came to the easiest way to try and predict the species based off of the features.*

# Summary - Decision Tree
    Looking at the histograms and scatterplots for petal length and petal width, we can see that:
    Either of the below statements will differentiate the setosa iris type
    • Any petal length less than 2cm means the iris type is setosa
    • Any petal width less than 1cm means the iris type is setosa
    PW vs PL chart.
    • Petal Length less than ~4.95cm AND Petal Width less than 1.7 cm means Versicolor iris type for definite but there's still some data points outside of this range, so add another AND.
        • Petal Length greater than 4.9cm AND less than 5.1cm, AND Petal Width greater than 1.5cm and less than 1.65cm means Versicolor
    • Everything else is Virginica.
    Write this IF statement.
    Have the programme predict the species type for each set of datapoints.

    The If statement was not working (got a little complicated when I was trying to build the for loop to run through the dataset then output the prediction to a new column in the pandas dataframe) so I went with a Numpy Select to set values using multiple conditions. I created an additional column in the Pandas Dataframe for 'predicted_name' and using conditions observed in the scatter plots and histograms I was able to define parameters to best assign a prediction to a set of datapoints. The datapoints used were the datapoints in the iris dataset. These could then be compared against the targets. With this in mind an accuracy of 99.3% was achieved for the parameters available, with only 1 dataset (line 70) being assigned incorrectly.
        ref: https://datagy.io/pandas-conditional-column/

    This code can be taken even further to receive an input from a user and will then best 'predict' or assign an iris type to the 4 parameters inputted. 99.3% accuracy is good enough in that it still leaves a margin for error. Considering the significant amount of overlap this 99.3% might seem to be too good although the logic is sound.

    While there were a number of other ways this final task could have been completed (using functions as opposed to Numpy Select, machine learning/ logical regression etc.) I finally decided to go with what I felt was the simplest method. Though I was technically assigning a species to data in the end and not exactly predicting the species type this project can still be improved, it will just requrie more effort, research and time on my part but the scope is there for further learning which I hope I will achieve in the near future.
