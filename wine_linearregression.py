import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Linear_Regression():

    def __init__(self):
        #reading the whole data into wine object
        self.wine = pd.read_csv('wine.csv')

    def linear_regression(self, xvalue, yvalue, title, xlabel, ylabel):
        y_bottom = 5
        y_top = 9
        y_range = y_top - y_bottom

        plt.ylim(y_bottom, y_top)
        #actual plotting of points, scatter plot
        plt.scatter(self.wine[xvalue], self.wine[yvalue])
        #regression line which is marked
        plt.plot(self.wine[xvalue], 0.5 * self.wine[xvalue] - 1.25  , label= title)

            #for plotting residual
        for i in range(0, len(self.wine)):
                    # first we need the coordinates of the actual point
            x_point = self.wine[xvalue][i]
            y_point = self.wine[yvalue][i]
                    # then we need the say how long is the vertical line
                    # the vertical line must be between 0 and 1
            y1 = (y_point - y_bottom) / y_range  # scale
            y2 = ((0.5 * x_point - 1.25) - y_bottom) / y_range  # scale
                    # now we can plot the vertical RED residual line
            plt.axvline(x_point, ymin=y1, ymax=y2, color="red") 

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.show()
        
lin_reg = Linear_Regression()
#finding correlation coefficient
lin_reg.linear_regression('AGST', 'Price', 'simple linear regression for temp and price', 'Temperature [Celsius]', 'Price')
#in linear regression we can  eliminate WinterRain and HarvestRain and Year when we want to decide the price
#so not plotting the regression model for mentioned attributes. But including the screen shots
lin_reg.linear_regression('WinterRain','Price', "simple linear regression for WinterRain and price", "WinterRain", "Price")
lin_reg.linear_regression('HarvestRain','Price', "simple linear regression for HarvestRain and price", "HarvestRain", "Price")
lin_reg.linear_regression('Age','Price', "simple linear regression for Age  and Price", "Age", "Price")
lin_reg.linear_regression('Year','Price', "simple linear regression for Year and Price", "Year", "Price")



