import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Scatterplot_wine():

    def __init__(self):
        #reading the whole data into wine object
        self.wine = pd.read_csv('wine.csv')

    #this method will plot the scatter plot against price
    #covered all variables
    def scatter_against_price(self, xvariable, yvariable, title, xlabel, ylabel):    
        #scatter is plotted using mentioned two components AGST and Price
        plt.scatter(self.wine[xvariable], self.wine[yvariable])
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
        print (self.wine.corr())


scatterplot_wine = Scatterplot_wine()
#finding correlation coefficient
scatterplot_wine.correlation_coef()

#scatter plots
scatterplot_wine.scatter_against_price('AGST','Price', "Shows wine price according to the temperature", "AGST(Celsius)", "Price")
scatterplot_wine.scatter_against_price('WinterRain','Price', "Shows wine price according to the WinterRain", "WinterRain", "Price")
scatterplot_wine.scatter_against_price('HarvestRain','Price', "Shows wine price according to the HarvestRain", "HarvestRain", "Price")
scatterplot_wine.scatter_against_price('Age','Price', "Shows wine price according to the Age of wint bottles", "Age", "Price")
scatterplot_wine.scatter_against_price('Year','Price', "Shows wine price according to year", "Year", "Price")






