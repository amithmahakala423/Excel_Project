import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Linear_Regression():

    def __init__(self):
        #reading the whole data into wine object
        self.framingham = pd.read_csv('framingham.csv')

    def linear_regression(self, xvalue, yvalue, title, xlabel, ylabel):
        plt.scatter(self.framingham[xvalue], self.framingham[yvalue])
        plt.plot(self.framingham[xvalue], 0.5 * self.framingham[xvalue] - 1.25  , label= title)
        for i in range(0, len(self.framingham)):
                    # first we need the coordinates of the actual point
                    x_point = self.framingham[xvalue][i]
                    y_point = self.framingham[yvalue][i]
                    X = np.linspace(0, 100, 200)
                    Y = 1 / (1 + np.exp(-X))
        plt.show()


lin_reg = Linear_Regression()
#finding correlation coefficient
lin_reg.linear_regression('male', 'totChol', 'simple linear regression for male/female and totChol', 'male/female', 'totChol')
lin_reg.linear_regression('cigsPerDay','heartRate', "Shows framingham for cigsPerDay with heartRate", "cigsPerDay", "heartRate")
lin_reg.linear_regression('cigsPerDay','glucose', "Shows framingham for cigsPerDay with glucose", "cigsPerDay", "glucose")
lin_reg.linear_regression('age','sysBP', "Shows framingham for age with sysBP", "age", "sysBP")
lin_reg.linear_regression('age','diaBP', "Shows framingham for age with diaBP", "age", "diaBP")
lin_reg.linear_regression('age','BMI', "Shows framingham for age with BMI", "age", "BMI")
lin_reg.linear_regression('cigsPerDay','glucose', "Shows framingham for cigsPerDay with glucose", "cigsPerDay", "glucose")
lin_reg.linear_regression('age','sysBP', "Shows framingham for age with sysBP", "age", "sysBP")
lin_reg.linear_regression('age','diaBP', "Shows framingham for age with diaBP", "age", "diaBP")
lin_reg.linear_regression('age','BMI', "Shows framingham for age with BMI", "age", "BMI")
lin_reg.linear_regression('age','heartRate', "Shows framingham for age with heartRate", "age", "heartRate")
lin_reg.linear_regression('male','education', "Shows framingham for male/female with education", "male/female", "education")
lin_reg.linear_regression('male','currentSmoker', "Shows framingham for male/female with smoking", "male/female", "currentSmoker")
lin_reg.linear_regression('education','currentSmoker', "Shows framingham for education and currentSmoker", "education", "currentSmoker")
lin_reg.linear_regression('male','cigsPerDay', "Shows framingham for male/female with  cigsPerDay", "male/female", "cigsPerDayss")

