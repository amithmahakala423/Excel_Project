import pandas as pd
import matplotlib.pyplot as plt


class Scatterplot_framingham():

    def __init__(self):
        #reading the whole data into framingham object
        self.framingham = pd.read_csv('framingham.csv')

    #this method will plot the scatter plot for framingham date
    #covered all variables
    def scatter_framingham(self, xvariable, yvariable, title, xlabel, ylabel):    
        #scatter is plotted using mentioned mentioned two variables
        plt.scatter(self.framingham[xvariable], self.framingham[yvariable])
        plt.title(title)
        #x-axis and y-axis label
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        #plotted in a grid
        plt.grid(True)
        plt.show()


    #correlation coefficient
    def correlation_coef(self):
        #this will return the data in the form of dataframe
        print (self.framingham.corr())

scatterplot_framingham = Scatterplot_framingham()

#correlation coefficient
scatterplot_framingham.correlation_coef()

#scatter plots
scatterplot_framingham.scatter_framingham('male','totChol', "Shows framingham for male/female with totChol", "male/female", "totChol")
scatterplot_framingham.scatter_framingham('cigsPerDay','heartRate', "Shows framingham for cigsPerDay with heartRate", "cigsPerDay", "heartRate")
scatterplot_framingham.scatter_framingham('cigsPerDay','glucose', "Shows framingham for cigsPerDay with glucose", "cigsPerDay", "glucose")
scatterplot_framingham.scatter_framingham('age','sysBP', "Shows framingham for age with sysBP", "age", "sysBP")
scatterplot_framingham.scatter_framingham('age','diaBP', "Shows framingham for age with diaBP", "age", "diaBP")
scatterplot_framingham.scatter_framingham('age','BMI', "Shows framingham for age with BMI", "age", "BMI")
scatterplot_framingham.scatter_framingham('age','heartRate', "Shows framingham for age with heartRate", "age", "heartRate")
scatterplot_framingham.scatter_framingham('male','education', "Shows framingham for male/female with education", "male/female", "education")
scatterplot_framingham.scatter_framingham('male','currentSmoker', "Shows framingham for male/female with smoking", "male/female", "currentSmoker")
scatterplot_framingham.scatter_framingham('education','currentSmoker', "Shows framingham for education and currentSmoker", "education", "currentSmoker")
scatterplot_framingham.scatter_framingham('male','cigsPerDay', "Shows framingham for male/female with  cigsPerDay", "male/female", "cigsPerDayss")



