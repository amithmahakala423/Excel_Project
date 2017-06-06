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


    def linear_regression(self):
        y_bottom = 6
        y_top = 9
        y_range = y_top - y_bottom

        plt.ylim(y_bottom, y_top)
        plt.scatter(wine.AGST, wine.Price) # the actual points
        plt.plot(x,y, label="Simple linear regression") # the regression line

            # now let's plot the residuals
        for i in range(0, len(wine)):
                    # first we need the coordinates of the actual point
            x_point = wine.AGST[i]
            y_point = wine.Price[i]
                    # then we need the say how long is the vertical line
                    # the vertical line must be between 0 and 1
            y1 = (y_point - y_bottom) / y_range  # scale
            y2 = ((0.5 * x_point - 1.25) - y_bottom) / y_range  # scale
                    # now we can plot the vertical RED residual line
            plt.axvline(x_point, ymin=y1, ymax=y2, color="red") 

        plt.title("Residualsimple LR")
        plt.xlabel("Temperature [Celsius degrees]")
        plt.ylabel("Log of Price")
        plt.grid()
        
        

scatterplot_wine = Scatterplot_wine()
#finding correlation coefficient
scatterplot_wine.correlation_coef()

#scatter plots
scatterplot_wine.scatter_against_price('AGST','Price', "Shows wine price according to the temperature", "AGST(Celsius)", "Price")
scatterplot_wine.scatter_against_price('WinterRain','Price', "Shows wine price according to the WinterRain", "WinterRain", "Price")
scatterplot_wine.scatter_against_price('HarvestRain','Price', "Shows wine price according to the HarvestRain", "HarvestRain", "Price")
scatterplot_wine.scatter_against_price('Age','Price', "Shows wine price according to the Age of wint bottles", "Age", "Price")
scatterplot_wine.scatter_against_price('Year','Price', "Shows wine price according to year", "Year", "Price")

#







